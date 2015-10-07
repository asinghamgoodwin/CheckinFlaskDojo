from flask import flash, redirect
from flask import render_template
from forms import LoginForm
from app import app, db, manager
from models import *
from collections import defaultdict

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    WEEK = 'Oct-05-15'

    assignments = Assignment.query.all()
    rooms = set(a.room for a in assignments)
    roomDict = defaultdict(list)
    for a in assignments:
        roomDict[a.room]+=[a.name]

    #print assignments

    if form.validate_on_submit():
        newAssignment = Assignment(form.name.data, form.room.data, WEEK)
        db.session.add(newAssignment)
        db.session.commit()
        flash('Success! name="%s", room=%s' %
              (form.name.data, str(form.room.data)))
    else:
        flash('ERROR! You tried to do name="%s", room=%s' %
              (form.name.data, str(form.room.data)))
    return render_template("index.html", form=form, assignments=assignments, rooms=roomDict)

@manager.command
def run():
    app.run(debug=True)

@manager.command
def helloWorld():
    print "hello world"

if __name__ == "__main__":
    manager.run()
