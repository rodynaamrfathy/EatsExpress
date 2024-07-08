from flask import render_template, request, redirect, url_for, flash, session
from app import app
from models import storage
from models.User import User


@app.route('/')
def main():
    return render_template('main.html', title="EatsExpress - Home")

@app.route('/home')
def home():
    user_id = session.get('user_id')
    if user_id:
        user = storage.get(User, user_id)
        return render_template('main_loggedin.html', title="EatsExpress - Home", user=user)
    else:
        flash('You need to log in to access this page.', 'danger')
        return redirect(url_for('login'))