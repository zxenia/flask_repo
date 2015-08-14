from flask import Flask, render_template, flash, redirect

from app import app

from .forms import LoginForm

@app.route('/')

@app.route('/index')

def index():
    user = {'nickname': 'Ksenia'}
    posts = [ #fake posts here
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Vienna!'
        },
        {
           'author': {'nickname': 'Martin'},
           'body': 'The Avengers movies was so cool!'
        }

    ]
    return render_template('index.html', title = 'My page', user = user, posts= posts)

@app.route('/login', methods=['GET', 'POST'])

def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.rememeber_me.data)))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])



