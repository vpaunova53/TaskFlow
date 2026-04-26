from flask import Flask, render_template, request, jsonify
import sqlite3
import datetime
import random

app = Flask(__name__)

# Database initialization
def init_db():
    with sqlite3.connect('tasks.db') as conn:
        # Create table with 'status' to support multiple columns
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks 
                     (id INTEGER PRIMARY KEY, content TEXT, status TEXT)''')

@app.route('/')
def index():
    return render_template('index.html')

# --- TASK API ---

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.execute('SELECT * FROM tasks')
        tasks = [{'id': row[0], 'content': row[1], 'status': row[2]} for row in cursor.fetchall()]
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    content = data.get('content')
    status = data.get('status', 'todo') # Default to todo if not provided
    
    if not content:
        return jsonify({'error': 'No content provided'}), 400
        
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.execute('INSERT INTO tasks (content, status) VALUES (?, ?)', (content, status))
        new_id = cursor.lastrowid
    return jsonify({'id': new_id, 'content': content, 'status': status}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PATCH'])
def update_task_status(task_id):
    data = request.json
    new_status = data.get('status')
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
    return jsonify({'result': 'success'}), 200

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    return jsonify({'result': 'success'}), 200

# --- CHATBOT BRAIN ---

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '').lower()
    
    if "hello" in user_msg or "hi" in user_msg:
        reply = "Hi! I'm your Kanban assistant. Which column are we working on today?"
    elif "joke" in user_msg:
        jokes = [
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "How do you comfort a JavaScript bug? You console it.",
            "A SQL query walks into a bar and asks two tables... 'Can I join you?'"
        ]
        reply = random.choice(jokes)
    elif "time" in user_msg:
        reply = f"It's {datetime.datetime.now().strftime('%H:%M')}. Let's get to work!"
    else:
        reply = "I'm still learning! Ask me for the 'time', a 'joke', or a 'tip'!"
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)