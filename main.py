from flask import Flask, render_template, redirect
from registrform import RegisterForm
from loginForm import LoginForm
from data import db_session
from data.__all_models import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TEXT'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init('db/site.sqlite')
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lich')
def lich():
    return render_template('lich.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registration.html',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('registration.html',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route('/about')
def courses():
    return render_template("about.html")


@app.route('/lk')
def lk():
    return render_template('registration.html')


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/product2')
def product2():
    return render_template('product2.html')


@app.route('/product3')
def product3():
    return render_template('product3.html')
@app.route('/kurs')
def kurs():
    return render_template('kurs.html')





if __name__ == '__main__':
    main()
