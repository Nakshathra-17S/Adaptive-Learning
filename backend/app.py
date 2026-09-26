from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import get_db, init_db
import os

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FRONTEND_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "frontend")
)

PAGES_DIR = os.path.join(FRONTEND_DIR, "pages")


# --------------------------------------------------
# FLASK APP
# --------------------------------------------------

app = Flask(__name__)
CORS(app)

init_db()


# --------------------------------------------------
# FRONTEND ROUTES
# --------------------------------------------------
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/pages/<path:filename>")
def pages(filename):
    return send_from_directory(PAGES_DIR, filename)


@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(
        os.path.join(FRONTEND_DIR, "assets"),
        filename
    )


@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)


# --------------------------------------------------
# REGISTER STUDENT
# --------------------------------------------------

@app.route("/api/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name", "").strip()
    learning_style = data.get("learning_style", "")

    if not name:
        return jsonify({
            "success": False,
            "message": "Name is required"
        }), 400

    conn = get_db()

    cursor = conn.execute(
        """
        INSERT INTO students (name, learning_style)
        VALUES (?, ?)
        """,
        (name, learning_style)
    )

    student_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "student_id": student_id,
        "message": "Student registered successfully"
    })


# --------------------------------------------------
# SAVE LEARNING STYLE
# --------------------------------------------------

@app.route("/api/learning-style", methods=["POST"])
def save_learning_style():

    data = request.get_json()

    student_id = data.get("student_id")
    style = data.get("learning_style", "")

    if not student_id or not style:
        return jsonify({
            "success": False,
            "message": "Student ID and learning style are required"
        }), 400

    conn = get_db()

    conn.execute(
        """
        UPDATE students
        SET learning_style = ?
        WHERE id = ?
        """,
        (style, student_id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Learning style saved successfully"
    })


# --------------------------------------------------
# DIAGNOSTIC QUIZ
# --------------------------------------------------

@app.route("/api/diagnostic", methods=["POST"])
def diagnostic():

    data = request.get_json()

    student_id = data.get("student_id")
    topic = data.get("topic", "Trigonometry")
    score = int(data.get("score", 0))

    if score < 50:
        level = "Beginner"

    elif score < 80:
        level = "Intermediate"

    else:
        level = "Advanced"

    conn = get_db()

    cursor = conn.execute(
        """
        INSERT INTO sessions
        (student_id, topic, level, diagnostic_score)
        VALUES (?, ?, ?, ?)
        """,
        (student_id, topic, level, score)
    )

    session_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "session_id": session_id,
        "score": score,
        "level": level
    })


# --------------------------------------------------
# GET LEVEL
# --------------------------------------------------

@app.route("/api/level/<int:student_id>")
def get_level(student_id):

    conn = get_db()

    session = conn.execute(
        """
        SELECT *
        FROM sessions
        WHERE student_id = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (student_id,)
    ).fetchone()

    conn.close()

    if not session:
        return jsonify({
            "success": False,
            "message": "No diagnostic result found"
        }), 404

    return jsonify({
        "success": True,
        "level": session["level"],
        "score": session["diagnostic_score"],
        "topic": session["topic"]
    })


# --------------------------------------------------
# LEARNING PREFERENCES
# --------------------------------------------------

@app.route("/api/learning-preferences", methods=["POST"])
def learning_preferences():

    data = request.get_json()

    student_id = data.get("student_id")
    duration = data.get("duration", 10)
    language = data.get("language", "English")
    learning_format = data.get("format", "Video")

    conn = get_db()

    conn.execute(
        """
        UPDATE sessions
        SET learning_duration = ?,
            learning_language = ?,
            learning_format = ?
        WHERE id = (
            SELECT id
            FROM sessions
            WHERE student_id = ?
            ORDER BY id DESC
            LIMIT 1
        )
        """,
        (
            duration,
            language,
            learning_format,
            student_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Learning preferences saved"
    })


# --------------------------------------------------
# AI TUTOR
# --------------------------------------------------

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "success": False,
            "message": "Please enter a question"
        }), 400

    question = message.lower()

    if "sin 30" in question:
        answer = "sin 30° = 1/2."

    elif "cos 60" in question:
        answer = "cos 60° = 1/2."

    elif "tan 45" in question:
        answer = "tan 45° = 1."

    elif "sin 90" in question:
        answer = "sin 90° = 1."

    elif "cos 0" in question:
        answer = "cos 0° = 1."

    elif "tan" in question:
        answer = "Tangent is the ratio of sine to cosine.\ntan θ = sin θ / cos θ."

    elif "sin" in question or "sine" in question:
        answer = "Sine is a trigonometric ratio.\nsin θ = Opposite / Hypotenuse."

    elif "cos" in question or "cosine" in question:
        answer = "Cosine is a trigonometric ratio.\ncos θ = Adjacent / Hypotenuse."

    else:
        answer = (
            "I am your LearnIQ Trigonometry tutor. "
            "You can ask me about sine, cosine, "
            "tangent or basic Trigonometry."
        )

    return jsonify({
        "success": True,
        "answer": answer
    })


# --------------------------------------------------
# FINAL QUIZ
# --------------------------------------------------

@app.route("/api/final-quiz", methods=["POST"])
def final_quiz():

    data = request.get_json()

    student_id = data.get("student_id")
    score = int(data.get("score", 0))

    points = score * 20

    conn = get_db()

    conn.execute(
        """
        UPDATE sessions
        SET final_score = ?,
            points = ?
        WHERE id = (
            SELECT id
            FROM sessions
            WHERE student_id = ?
            ORDER BY id DESC
            LIMIT 1
        )
        """,
        (
            score,
            points,
            student_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "score": score,
        "points": points
    })


# --------------------------------------------------
# FEEDBACK
# --------------------------------------------------

@app.route("/api/feedback", methods=["POST"])
def feedback():

    data = request.get_json()

    student_id = data.get("student_id")
    rating = int(data.get("rating", 0))
    comment = data.get("comment", "")

    conn = get_db()

    conn.execute(
        """
        INSERT INTO feedback
        (student_id, rating, comment)
        VALUES (?, ?, ?)
        """,
        (
            student_id,
            rating,
            comment
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Feedback saved successfully"
    })


# --------------------------------------------------
# PROGRESS
# --------------------------------------------------

@app.route("/api/progress/<int:student_id>")
def progress(student_id):

    conn = get_db()

    student = conn.execute(
        """
        SELECT *
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    ).fetchone()

    session = conn.execute(
        """
        SELECT *
        FROM sessions
        WHERE student_id = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (student_id,)
    ).fetchone()

    conn.close()

    if not student or not session:

        return jsonify({
            "success": False,
            "message": "Progress not found"
        }), 404

    diagnostic = session["diagnostic_score"]

    final_percentage = session["final_score"] * 20

    improvement = final_percentage - diagnostic

    if improvement < 0:
        improvement = 0

    return jsonify({

        "success": True,

        "student": {
            "id": student["id"],
            "name": student["name"],
            "learning_style": student["learning_style"]
        },

        "progress": {

            "topic": session["topic"],

            "level": session["level"],

            "diagnostic_score": diagnostic,

            "final_score": session["final_score"],

            "final_percentage": final_percentage,

            "improvement": improvement,

            "points": session["points"],

            "duration": session["learning_duration"],

            "language": session["learning_language"],

            "format": session["learning_format"]
        }
    })


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.route("/api/health")
def health():

    return jsonify({
        "success": True,
        "message": "Adaptive Learning backend is running!"
    })


# --------------------------------------------------
# START SERVER
# --------------------------------------------------

if __name__ == "__main__":

    import os

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )