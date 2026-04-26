from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, content TEXT)')

@app.route('/')
def index():
    return render_template('index.html')

# API Endpoint: Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.execute('SELECT * FROM tasks')
        tasks = [{'id': row[0], 'content': row[1]} for row in cursor.fetchall()]
    return jsonify(tasks)

# API Endpoint: Add a task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.execute('INSERT INTO tasks (content) VALUES (?)', (data['content'],))
        new_id = cursor.lastrowid
    return jsonify({'id': new_id, 'content': data['content']}), 201
# API Endpoint: Delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    return jsonify({'result': 'success'}), 200
if __name__ == '__main__':
    init_db()
    app.run(debug=True)