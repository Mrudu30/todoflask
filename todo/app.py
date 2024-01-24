from flask import Flask as f
from flask import flash, render_template, redirect,request,url_for,session
from module.database import Database

app = f(__name__)
app.secret_key='todosecret333'
db=Database()

# ---------HOME VIEW----------
@app.route('/')
def home():
    data=db.read(None)
    # print(data)
    return render_template('home.html',data=data)

# ----------TASK VIEW---------

@app.route('/view/<int:id>/')
def view(id):
    try:
        data=db.read(id)
        return render_template('task_render.html',data=data)
    except:
        return 'Tasknot found'

# ----------TADD TASK---------
@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addtask',methods=['POST'])
def addTask():
    if request.method == 'POST' and request.form['save']:
        if db.add(request.form):
            flash("A new task has been added")
        else:
            flash("A new task can not be added")

        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# ----------UPDATE TASK---------
@app.route('/updatetask/<int:id>/')
def updateTask(id):
    data = db.read(id)
    # print(data)

    if len(data) == 0:
        return redirect(url_for('home'))
    else:
        session['update'] = id
        return render_template('edit.html', data = data)

@app.route('/updatedtask',methods=['POST'])
def updatedTask():
    if request.method=='POST' and request.form['update']:
        if db.update(session['update'], request.form):
            flash('A task has been updated')

        else:
            flash('A task can not be updated')

        session.pop('update', None)

        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# ----------DELETE TASK---------
@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id)

    if len(data) == 0:
        return redirect(url_for('home'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deleteTask/',methods=['POST'])
def deleteTask():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A Task has been deleted')

        else:
            flash('A Task can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# Catch-all route for invalid URLs
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 2000,debug=True)