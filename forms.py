from flask.ext.wtf import Form
from wtforms import SelectField, StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    # TODO: form fields
    name = StringField('name', validators=[DataRequired()])
    room = SelectField('room', choices=[('hopper_1030', 'Hopper 10:30'), ('hopper_1300', 'Hopper 1:00p')],validators=[DataRequired()])