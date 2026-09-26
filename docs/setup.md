# LearnIQ – Setup Guide

## 1. Requirements

The following software is required to run the project locally:

* Python 3.x
* A web browser
* GitHub repository access
* Internet connection

## 2. Clone the Repository

Clone the repository using:

```bash
git clone https://github.com/Nakshathra-17S/Adaptive-Learning.git
```

Move into the project directory:

```bash
cd Adaptive-Learning
```

## 3. Install Backend Dependencies

Open the backend directory:

```bash
cd backend
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 4. Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run on the local Flask server.

Open the displayed local URL in a web browser.

## 5. Project Structure

```text
Adaptive-Learning/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── create_pdf.py
│   ├── requirements.txt
│   └── adaptive_learning.db
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   ├── assets/
│   ├── pages/
│   └── pdf/
│
├── docs/
├── README.md
├── ai.md
└── resource.md
```

## 6. Database

The application uses SQLite.

The database is initialized by the backend when the application starts.

## 7. Running the Deployed Version

The project is also deployed on Render.

The live deployment URL is available in the main README under the Live Demo section.

## 8. Basic User Flow

After opening the application:

1. Register with a name or nickname.
2. Complete the learning archetype quiz.
3. Complete the diagnostic quiz.
4. Receive a personalized learning level.
5. Select a learning format.
6. Study the personalized Trigonometry content.
7. Use the AI Tutor if required.
8. Complete the final quiz.
9. View feedback and progress.

