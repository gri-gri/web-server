from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
 
 
class LoginForm(FlaskForm):
    inputt = IntegerField('Введите число', validators=[DataRequired()])
    submit = SubmitField('Отправить')
