from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7453751bde3aff9e8c9856039a13bce9'

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

