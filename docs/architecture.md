# LearnIQ – Architecture

## 1. Overview

LearnIQ is an adaptive learning platform designed to personalize the learning experience according to each student's learning style and current knowledge level.

The system adapts the presentation of learning content using two inputs:

* Learning Archetype: Visualizer, Explorer, Challenger, or Storyteller
* Knowledge Level: Beginner, Intermediate, or Advanced

The platform then provides personalized learning content, an AI tutor, a final quiz, and progress feedback.

## 2. System Architecture

The application follows a simple client-server architecture.

### Frontend

The frontend is built using:

* HTML
* CSS
* JavaScript

It contains the registration, archetype quiz, diagnostic quiz, learning-content pages, AI tutor, final quiz, feedback, and progress pages.

### Backend

The backend is built using:

* Python
* Flask
* Flask-CORS
* SQLite

The Flask backend provides API endpoints for registration, learning preferences, diagnostic assessment, AI tutoring, final quizzes, feedback, and progress tracking.

### Database

SQLite is used as the database.

It stores student information, learning preferences, diagnostic results, learning progress, quiz results, and feedback.

## 3. Adaptive Learning Flow

```text
Student Registration
        ↓
Learning Archetype Quiz
        ↓
Visualizer / Explorer / Challenger / Storyteller
        ↓
Diagnostic Quiz
        ↓
Beginner / Intermediate / Advanced
        ↓
Personalized Learning Content
        ↓
AI Tutor
        ↓
Final Quiz
        ↓
Feedback & Progress
```

## 4. Personalization Logic

LearnIQ combines the student's learning archetype and knowledge level.

For example:

* Visualizer + Beginner → visual explanations with detailed basics
* Explorer + Intermediate → real-world examples with application-based learning
* Challenger + Advanced → challenging problems and advanced applications
* Storyteller + Beginner → story-based explanations with strong foundational concepts

This allows the same topic to be presented differently depending on the learner.

## 5. Learning Content

The platform currently demonstrates adaptive learning using Mathematics, specifically Trigonometry.

Available learning formats include:

* Animated lesson
* PDF
* Mind map
* Visual guide

Students can also select preferred video duration and language.

## 6. AI Tutor

The AI Tutor provides an interactive question-and-answer interface where students can ask questions related to the learning topic.

The tutor is integrated into the learning flow after the personalized learning content.

## 7. Quiz and Assessment

The diagnostic quiz determines the student's current level.

The final quiz evaluates learning after the personalized lesson.

The platform uses the following diagnostic thresholds:

* Below 50% → Beginner
* 50% to below 80% → Intermediate
* 80% and above → Advanced

## 8. Technology Stack

| Layer          | Technology                 |
| -------------- | -------------------------- |
| Frontend       | HTML, CSS, JavaScript      |
| Backend        | Python, Flask              |
| Database       | SQLite                     |
| API            | REST-style Flask endpoints |
| PDF Generation | ReportLab                  |
| Deployment     | Render                     |
| Source Control | GitHub                     |

## 9. Deployment

The project is deployed as a Python web service on Render.

The repository contains separate `frontend` and `backend` directories. The backend serves the frontend pages and provides the application APIs.

The project can be accessed through the deployed Render URL provided in the main README.

