from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '7453751bde3aff9e8c9856039a13bce9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(15), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    post = db.relationship("Post", backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Patrick Thomas',
        'title': 'Bull Post 1',
        'content': '    Lorem ipsum dolor sit amet, consectetur '
                   'adipiscing elit, sed do eiusmod tempor incididunt '
                   'ut labore et dolore magna aliqua. Ut enim ad minim '
                   'veniam, quis nostrud exercitation ullamco laboris nisi '
                   'ut aliquip ex ea commodo consequat. Duis aute irure dolor '
                   'in reprehenderit in voluptate velit esse cillum dolore eu fugiat'
                   ' nulla pariatur. Excepteur sint occaecat cupidatat non proident, '
                   'sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted': 'June 8, 2019'
    },
    {
        'author': 'Gloria Borger',
        'title': 'Bull Post 1',
        'content': '    Lorem ipsum dolor sit amet, consectetur '
                   'adipiscing elit, sed do eiusmod tempor incididunt '
                   'ut labore et dolore magna aliqua. Ut enim ad minim '
                   'veniam, quis nostrud exercitation ullamco laboris nisi '
                   'ut aliquip ex ea commodo consequat. Duis aute irure dolor '
                   'in reprehenderit in voluptate velit esse cillum dolore eu fugiat'
                   ' nulla pariatur. Excepteur sint occaecat cupidatat non proident, '
                   'sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted': 'June 8, 2019'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home Page')


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

