from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    user = {'nickname' : 'Jace'}
    posts = [
        {
            'author': {'nickname':'Jace'},
            'body':'Beautiful day in NYP'
        },
        {
            'author': {'nickname':'Susan'},
            'body': 'Bad day in MRT train'
        }
    ]
    return render_template('index.html', u=user, p=posts)


if __name__ == '__main__':
    app.run()
