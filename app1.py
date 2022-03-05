from crypt import methods
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thewaleed:123@localhost:5432/tododb'
db = SQLAlchemy(app)
class Todo(db.Model):
    __tablename__ = 'todooooo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    difficulty = db.Column(db.Integer, nullable=True)
db.create_all()
@app.route('/todos/addtask', methods=['POST'])
def create_todo():
  task = request.get_json()
#   difficulty = request.get_json()['difficulty']
  todo1 = Todo(description=task)
  db.session.add(todo1)
  db.session.commit()
  return jsonify({
        'task': todo1.description
        # 'difficultylevel':todo1.difficulty
     })
  
@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())
#always include this at the bottom of your code (port 3000 is only necessary in workspaces)
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)