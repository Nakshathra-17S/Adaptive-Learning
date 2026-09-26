async function continueToStyle() {

    const nameInput = document.getElementById("studentName");
    const name = nameInput.value.trim();
    const error = document.getElementById("errorMessage");

    if (name === "") {
        error.textContent = "Please enter your name to continue.";
        return;
    }

    try {

        const response = await fetch("/api/register", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                learning_style: ""
            })
        });

        const data = await response.json();

        console.log("Backend response:", data);

        if (data.success) {

            localStorage.setItem(
                "studentId",
                data.student_id
            );

            localStorage.setItem(
                "studentName",
                name
            );

            window.location.href = "pages/archetype.html";

        } else {

            error.textContent =
                data.message || "Registration failed.";

        }

    } catch (error) {

        console.error("Registration error:", error);

        error.textContent =
            "Unable to connect to the server. Please try again.";

    }
}