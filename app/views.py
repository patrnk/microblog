from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Paul'}  # fake user
    posts = [{'author': 'melevir', 'body': 'qweqwe'}, 
             {'author': 'kazauwa', 'body': 'asd' }]
    return render_template('index.html', title='title?', user=user, posts=posts)
