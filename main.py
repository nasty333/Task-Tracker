from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample initial tasks
tasks = [
    {"id": 1, "title": "Task 1", "description": "Complete task 1"},
    {"id": 2, "title": "Task 2", "description": "Finish task 2"},
    {"id": 3, "title": "Task 3", "description": "Submit task 3"},
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_task = {"id": len(tasks) + 1, "title": title, "description": description}
        tasks.append(new_task)
        return redirect('/')
    return render_template('add_task.html')

@app.route('/task/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
