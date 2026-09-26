# LearnIQ – Adaptive Learning Platform

> **Learning should adapt to the student, not the other way around.**

LearnIQ is a web-based adaptive learning platform designed to provide students with a more personalized learning experience.

Instead of giving every student the same learning material, LearnIQ first understands the student's preferred learning style and then evaluates their current knowledge level through a diagnostic quiz. Based on these results, the platform provides learning content suited to the student's needs.

For our hackathon prototype, we focused on:

- **Subject:** Mathematics
- **Topic:** Trigonometry

---

## 🌟 Key Idea

Every student learns differently.
Some students understand concepts better through diagrams and visual explanations, while others prefer stories, problem-solving, or real-world examples.
LearnIQ addresses this by combining:
**Learning Preference + Knowledge Level + Assessment Performance**
to create a more personalized learning journey.

---

# 🎯 Problem Statement

Traditional learning systems often provide the same content to every student regardless of their learning preference or current understanding.

This can make it difficult for students to:

- Understand concepts at their own pace
- Learn using a method that suits them
- Identify their weak areas
- Receive targeted practice
- Track their improvement

LearnIQ aims to make learning more adaptive by understanding the learner before delivering the learning content.

---

# 💡 Our Solution

LearnIQ follows a simple adaptive learning cycle.

```text
Student Registration
        ↓
Learning Style Assessment
        ↓
Learning Archetype
        ↓
Subject & Topic Selection
        ↓
Diagnostic Quiz
        ↓
Level Detection
        ↓
Personalized Learning
        ↓
Final Quiz
        ↓
Progress Tracking
        ↓
Feedback & Intervention


## 🧠 Learning Archetype System
One of the core features of LearnIQ is its **Learning Archetype Assessment**.
We believe that students do not all learn in the same way. Before providing personalized learning content, LearnIQ asks the student a short set of questions to understand how they prefer to learn.
The assessment contains **5 questions**, and each answer is mapped to one of four learning archetypes.

### 👁️ 1. Visualizer
**Learning preference:** Visual and structured learning.
Visualizers understand concepts better when information is presented using:
- Diagrams
- Pictures
- Charts
- Mind maps
- Visual summaries
For a Visualizer, LearnIQ focuses on making concepts easier to understand through visual representation.
**Example:**
Instead of only explaining a trigonometric ratio using text, the concept can be represented using a right-triangle diagram and a visual relationship between its sides.

---

### 📖 2. Storyteller
**Learning preference:** Learning through stories and context.
Storytellers understand concepts better when they are connected to:
- Characters
- Stories
- Situations
- Conflicts
- Realistic examples

For a Storyteller, LearnIQ presents concepts in a more narrative way.

**Example:**
Instead of directly introducing a trigonometric formula, a situation involving a character measuring the height of a building can be used to introduce the concept.
---

### 🧩 3. Challenger
**Learning preference:** Problem-solving and discovery.
Challengers prefer to:
- Try solving a problem first
- Explore different approaches
- Discover the required concept
- Use formulas as tools to solve problems

For a Challenger, LearnIQ encourages active problem-solving before providing the complete explanation.

**Example:**
The student may first be given a trigonometry problem and asked to attempt it. After the attempt, the relevant ratio or formula can be introduced as a tool for solving the problem.

---

### 🌍 4. Explorer

**Learning preference:** Real-world and practical learning.

Explorers understand concepts better when they can connect them to real-life situations.

They prefer:

- Practical examples
- Everyday applications
- Real-world problems
- Situational learning

For an Explorer, LearnIQ connects mathematical concepts to situations outside the classroom.

**Example:**

Trigonometry can be introduced through applications such as measuring the height of a building, calculating distances, or understanding angles of elevation.

---

## 🔄 How Archetype Detection Works

The student completes a 5-question learning-style assessment.

Each answer contributes to one of the four archetype categories.

```text
                Student
                   ↓
        5-Question Assessment
                   ↓
          Answer Preferences
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
   Visualizer  Storyteller  Challenger
        │          │          │
        └──────────┼──────────┘
                   ↓
               Explorer
                   ↓
        Dominant Archetype
                   ↓
       Personalized Learning
