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
def main():
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
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
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
        # Check if email already exists
        existing_user = next((u for u in storage.all(User).values() if u.email == email), None)
        if existing_user:
            flash('Email already exists. Please log in.', 'warning')
            return redirect(url_for('login'))
        # Create a new user
        hashed_password = md5(password.encode()).hexdigest()
        new_user = User(username=username, email=email, password=hashed_password)
        storage.new(new_user)
        storage.save()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('create_account.html', title="EatsExpress - Register")

@app.route('/add_to_cart')
def add_to_cart():
    return render_template("viewcart.html")


@app.route('/home')
def home():
    return render_template('main_loggedin.html', title="EatsExpress - Home")

@app.route('/search')
def search():
    return render_template('filter.html', title="EatsExpress - Search")

@app.route('/item')
def item():
    return render_template('add_item_to_cart.html', title="EatsExpress - item")

@app.route('/addaddress')
def addaddress():
    return render_template('add_address.html', title="EatsExpress - add address")

@app.route('/completeorder')
def completeorder():
    return render_template('complete_order.html', title="EatsExpress - complete order")

@app.route('/viewall')
def viewall():
    restaurants = storage.all(Restaurant).values()
    print(restaurants)  # This will print the list of restaurants to your console
    return render_template('all_restaurants.html', restaurants=restaurants, title="View All Restaurants")

@app.route('/restaurant_details/<int:restaurant_id>')
def restaurant_details(restaurant_id):
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        flash('Restaurant not found', 'danger')
        return redirect(url_for('viewall'))
    menu_items = storage.all(MenuItem).filter_by(restaurant_id=restaurant.id).all()  # Assuming this fetches related menu items
    return render_template('restaurant_details.html', restaurant=restaurant, menu_items=menu_items, title=restaurant.name)


if __name__ == '__main__':
    app.run(debug=True, port=5001)