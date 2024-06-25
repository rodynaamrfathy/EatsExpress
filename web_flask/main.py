#!/usr/bin/python3
""" Starts a Flask Web Application """
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from hashlib import md5
from models import storage
from models.User import User
from models.Cart import Cart
from models.Restaurant import Restaurant
from models.MenuItem import MenuItem

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('main.html', title="EatsExpress - Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the entered password
        hashed_password = md5(password.encode()).hexdigest()

        user = None
        for u in storage.all(User).values():
            if u.username == username and u.password == hashed_password:
                user = u
                break
        if user:
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home_loggedin'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title="EatsExpress - Login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        address = request.form.get('address', '')

        # Check if email already exists
        for u in storage.all(User).values():
            if u.email == email:
                flash('Email already exists. Please log in.', 'warning')
                return redirect(url_for('login'))

        # Create a new user
        new_user = User(username=username, email=email, password=password, address=address)
        storage.new(new_user)
        storage.save()

        # Check if the user was saved
        if storage.get(User, new_user.id) is not None:
            print("User saved successfully:", new_user)
        else:
            print("Failed to save user:", new_user)

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('create_account.html', title="EatsExpress - Register")


@app.route('/home_loggedin')
def home_loggedin():
    return render_template('main_loggedin.html', title="EatsExpress - Home")


@app.route('/cart')
def cart():
    return render_template('viewcart.html', title="EatsExpress - Cart")


@app.route('/restaurant/<int:restaurant_id>')
def restaurant(restaurant_id):
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        flash('Restaurant not found', 'danger')
        return redirect(url_for('home_loggedin'))
    menu_items = storage.all(MenuItem).values()
    menu_items = [item for item in menu_items if item.restaurant_id == restaurant_id]
    return render_template('restaurant.html', restaurant=restaurant, menu_items=menu_items, title="EatsExpress - Restaurant")


@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    item = storage.get(MenuItem, item_id)
    if not item:
        flash('Item not found', 'danger')
        return redirect(url_for('home_loggedin'))
    if 'user_id' in session:
        new_cart_item = Cart(user_id=session['user_id'], item_id=item.id, quantity=1)
        storage.new(new_cart_item)
        storage.save()
        flash('Item added to cart', 'success')
        return redirect(url_for('cart'))
    else:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))


@app.route('/complete_order')
def complete_order():
    return render_template('complete_order.html', title="EatsExpress - Complete Order")


@app.route('/add_address')
def add_address():
    return render_template('add_address.html', title="EatsExpress - Add Address")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
