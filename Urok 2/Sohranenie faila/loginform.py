from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
 
 
class LoginForm(FlaskForm):
    file_load = FileField('Загрузите файл', validators=[DataRequired()])
    submit = SubmitField('Отправить')
