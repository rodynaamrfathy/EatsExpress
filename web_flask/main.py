from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys
from models.base_model import Base
from models.User import User
from models.Order import Order
from models.Review import Review
from models.Restaurant import Restaurant
from models.MenuItem import MenuItem
from models.Cart import Cart

# Adding the project root to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('main.html', title="EatsExpress - Home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home_loggedin'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="EatsExpress - Login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
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
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    menu_items = MenuItem.query.filter_by(restaurant_id=restaurant_id).all()
    return render_template('restaurant.html', restaurant=restaurant, menu_items=menu_items, title="EatsExpress - Restaurant")

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    item = MenuItem.query.get_or_404(item_id)
    if 'user_id' in session:
        new_cart_item = Cart(user_id=session['user_id'], item_id=item.id, quantity=1)
        db.session.add(new_cart_item)
        db.session.commit()
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

if __name__ == '__main__':
    with app.app_context():
        from models import init_db
        init_db()
    app.run(debug=True, port=5001)
