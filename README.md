# TaskFlow

TaskFlow 🚀
A high-performance, real-time Task Management dashboard built with a Python (Flask) backend and a modern Vanilla JavaScript frontend. This project demonstrates a complete Client-Server architecture with persistent data storage.

🌟 Features

- Kanban Workflow: Organize tasks into To Do, In Process, and Done columns.

- Smart Entry: Choose the target column immediately upon task creation.

- State Management: Move tasks between columns using PATCH requests to update the database state dynamically.

- Rule-Based AI Assistant: A custom-coded "Brain" that handles natural language queries for productivity tips, jokes, and time-checks.

- Glassmorphism UI: A modern, high-energy interface built with Tailwind CSS and Animate.css for a professional feel.

🛠️ Tech Stack
= Backend: Python 3.12, Flask

- Frontend: HTML5, Tailwind CSS, JavaScript (ES6+ Fetch API)

- Database: SQLite3

- Animations: Animate.css

🚀 Getting Started
Prerequisites

- Python 3.x installed on your machine.

- A modern web browser.

Installation & Setup

1. Clone the repository:

Bash

git clone https://github.com/your-username/taskflow.git

cd taskflow

- Set up a Virtual Environment (Recommended):

python -m venv venv

# Windows

venv\Scripts\activate

# Mac/Linux

source venv/bin/activate

- Install Dependencies:

pip install flask

- Run the Application:

python app.py

- View the App:

Open your browser and navigate to http://127.0.0.1:5000

📁 Project Structure

Plaintext

taskflow/

├── app.py              # Flask Server & API Routes

├── tasks.db            # SQLite Database (Auto-generated)

├── static/             # Static assets (CSS/JS)

└── templates/
    
    └── index.html      # Frontend Interface

🧠 Key Learnings

- Implementing Asynchronous JavaScript (Async/Await) to handle API requests without page reloads.

- Managing Database Connections within a Flask context.

- Designing a professional User Experience using modern CSS frameworks and motion design principles.
