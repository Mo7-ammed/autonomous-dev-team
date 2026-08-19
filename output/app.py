from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
tasks = {}
task_id_counter = 1
ALLOWED_STATUSES = {"pending", "in-progress", "done"}

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json() or {}
    title = data.get('title')
    
    if not title or not str(title).strip():
        return jsonify({"error": "Title is required and cannot be empty"}), 400
        
    task = {
        "id": task_id_counter,
        "title": title,
        "description": data.get('description', ''),
        "status": "pending"
    }
    tasks[task_id_counter] = task
    task_id_counter += 1
    
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(list(tasks.values())), 200

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
        
    data = request.get_json() or {}
    status = data.get('status')
    
    if status not in ALLOWED_STATUSES:
        return jsonify({"error": "Invalid status. Allowed values are 'pending', 'in-progress', 'done'"}), 400
        
    tasks[task_id]['status'] = status
    return jsonify(tasks[task_id]), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
        
    del tasks[task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
