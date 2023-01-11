from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import EmailField


class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторить пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

