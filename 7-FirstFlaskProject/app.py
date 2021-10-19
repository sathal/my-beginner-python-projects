from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



### Setting up our application
app = Flask(__name__) # Just referencing this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

### Create an index route so that when we browse to th URL we don't just immediately hit a 404
@app.route('/', methods=['POST','GET']) # URL String of our route
def index(): # Function for our route
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            ### Insert into database
            db.session.add(new_task)
            db.session.commit()
            return redirect('/') # Redirect back to index webpage
        except:
            return 'There was an issue adding your task'
    else:
        ### Look at all of database contents in order of date created and return them all
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks )

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/') # Redirect to homepage
    except:
        return 'There was a problem deleting the task'



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/') # Redirect to homepage
        except:
            return 'There was a problem updating the task'

    else:
        return render_template('update.html',  task=task )






if __name__ == "__main__":
    app.run(debug=True) # If we have any errors they should show up on the webpage
