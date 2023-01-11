from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import EmailField


class LoginForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Не выходить из системы')
    submit = SubmitField('Войти')
