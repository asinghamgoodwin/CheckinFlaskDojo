from flask import flash, redirect
from flask import render_template
from forms import LoginForm
from app import app, db, manager
from models import *

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    WEEK = 'Oct-05-15'
    if form.validate_on_submit():
        newAssignment = Assignment(form.name.data, form.room.data, WEEK)
        db.session.add(newAssignment)
        db.session.commit()
        flash('Success! name="%s", room=%s' %
              (form.name.data, str(form.room.data)))
    else:
        flash('ERROR! You tried to do name="%s", room=%s' %
              (form.name.data, str(form.room.data)))
    return render_template("index.html", form=form)


@manager.command
def run():
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()
