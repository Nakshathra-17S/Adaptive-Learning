# LearnIQ – Constraints

## 1. Project Scope

LearnIQ is currently developed as a working MVP demonstrating adaptive learning for Mathematics, with Trigonometry used as the primary demonstration topic.

The current implementation focuses on demonstrating the adaptive learning workflow rather than covering every school subject.

## 2. Time Constraint

The project was developed within the limited time available during the hackathon.

Therefore, the MVP prioritizes the core adaptive learning flow:

Registration → Learning Style → Diagnostic Assessment → Personalized Learning → AI Tutor → Final Quiz → Feedback.

## 3. Technology Constraints

The project uses lightweight and accessible technologies:

* HTML, CSS and JavaScript for the frontend
* Python and Flask for the backend
* SQLite for data storage
* Render for deployment

The application avoids requiring complex infrastructure so that the MVP can be easily deployed and demonstrated.

## 4. Data Constraints

The MVP uses a limited dataset and predefined learning content for demonstration.

The current Trigonometry content is designed to demonstrate personalization rather than provide a complete Mathematics curriculum.

## 5. Personalization Constraints

Personalization is currently based on:

* Learning archetype
* Diagnostic performance
* Selected learning preferences

The MVP does not yet use long-term behavioral data, historical academic records, or continuous learning analytics.

## 6. AI Constraints

The AI Tutor depends on the availability of the configured AI service.

AI-generated responses may require verification and are intended to support learning rather than replace teachers or official educational material.

## 7. Authentication Constraint

The MVP uses simple student registration for demonstration purposes.

It does not currently implement full authentication, password management, or institutional identity verification.

## 8. Deployment Constraints

The application is deployed using a free hosting environment.

Performance, startup time, storage capacity, and availability may therefore be limited compared with a production-grade deployment.

## 9. Scalability

SQLite is sufficient for the current MVP and demonstration.

For a large number of concurrent students, the database would need to be migrated to a production-grade database system and the backend infrastructure would need to be scaled.

## 10. Future Expansion

The architecture is designed so that additional subjects, topics, learning formats, languages, and personalization signals can be added in future versions.

