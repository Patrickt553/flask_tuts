from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def hello_world():
    return render_template('home.html.py', posts=posts, title='FUCK YOU')


@app.route('/about')
def about():
    return render_template('about.html.py', title='About')


if __name__ == '__main__':
    app.run(debug=True)

