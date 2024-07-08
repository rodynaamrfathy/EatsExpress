from flask import render_template, request, redirect, url_for, flash, session
from app import app
from hashlib import md5
from models import storage
from models.User import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_id = request.form['login_id']
        password = request.form['password']
        hashed_password = md5(password.encode()).hexdigest()
        user = None
        
        # Check user credentials
        for user_obj in storage.all(User).values():
            if (user_obj.username == login_id or user_obj.email == login_id) and user_obj.password == hashed_password:
                user = user_obj
                break

        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            flash('Logged in successfully!', 'success')
            if user.username == 'Admin':
                return redirect(url_for('adminpage'))
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title="EatsExpress - Login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        phone_number = request.form['phone_number']
        country_code = request.form['country_code']
        email = request.form['email']
        confirm_email = request.form['confirm_email']
        password = request.form['password']
        username = request.form['username']

        # Check if email and confirm email match
        if email != confirm_email:
            flash('Emails do not match. Please try again.', 'danger')
            return redirect(url_for('register'))

        # Check if user already exists by email or username
        existing_user_by_email = next((u for u in storage.all(User).values() if u.email == email), None)
        existing_user_by_username = next((u for u in storage.all(User).values() if u.username == username), None)
        
        if existing_user_by_email:
            flash('Email already exists. Please log in.', 'warning')
            return redirect(url_for('login'))
        
        if existing_user_by_username:
            flash('Username already exists. Please choose a different username.', 'warning')
            return redirect(url_for('register'))
        
        hashed_password = md5(password.encode()).hexdigest()
        new_user = User(
            username=username,
            email=email,
            password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            phone_number=f"{country_code} {phone_number}"
        )
        storage.new(new_user)
        storage.save()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    
    return render_template('create_account.html', title="EatsExpress - Register")
