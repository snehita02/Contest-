from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

class signup(FlaskForm):
    userid=StringField("ENTER USERNAME",validators=[DataRequired()])
    passwd=PasswordField("ENTER PASSWORD",validators=[DataRequired()])

class login(FlaskForm):
    userid=StringField("ENTER USERNAME",validators=[DataRequired()])
    passwd=PasswordField("ENTER PASSWORD",validators=[DataRequired()])

class post(FlaskForm):
    quoet=StringField("share ur thaughts",validators=[])