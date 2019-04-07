from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField,\
     RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
 
class LoginForm(FlaskForm):
    username_first = StringField('Логин', validators=[DataRequired()])
    real_name = StringField('Реальное имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    sex = RadioField('Пол', choices=[('m','Мужской'),('f','Женский')], validators=[DataRequired()])
    commentary = TextAreaField('Немного о себе')
    language = SelectField('Язык', choices=[('en', 'English'), ('ru', 'Русский')], validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Отправить')
