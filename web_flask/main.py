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
    return render_template('all_restaurants.html', restaurants=restaurants, title="View All Restaurants")

@app.route('/restaurant_details/<int:restaurant_id>')
def restaurant_details(restaurant_id):
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        flash('Restaurant not found', 'danger')
        return redirect(url_for('viewall'))
    menu_items = [item for item in storage.all(MenuItem).values() if item.restaurant_id == restaurant_id]  # Fetch related menu items
    return render_template('restaurant_details.html', restaurant=restaurant, menu_items=menu_items, title=restaurant.name)

@app.route('/choice')
def choice():
    return render_template('choice.html', title="Choose Action")

@app.route('/create_restaurant', methods=['GET', 'POST'])
def create_restaurant():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']

        # Check for existing restaurant
        existing_restaurant = next((r for r in storage.all(Restaurant).values() if r.name == name), None)
        if existing_restaurant:
            flash('Restaurant already exists. Please try a different name.', 'warning')
            return redirect(url_for('create_restaurant'))

        # Create restaurant object
        new_restaurant = Restaurant(name=name, location=location)
        storage.new(new_restaurant)
        storage.save()
        flash('Restaurant created successfully!', 'success')
        return redirect(url_for('viewall'))

    return render_template('create_restaurant.html', title="Create New Restaurant")

@app.route('/add_menu_item', methods=['GET', 'POST'])
def add_menu_item():
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']
        item_name = request.form['menu_item_name']
        item_price = request.form['menu_item_price']
        item_description = request.form['menu_item_description']

        # Find the restaurant
        restaurant = next((r for r in storage.all(Restaurant).values() if r.name == restaurant_name), None)
        if not restaurant:
            flash('Restaurant not found. Please try again.', 'danger')
            return redirect(url_for('add_menu_item'))

        # Create menu item object and add it to the restaurant
        new_menu_item = MenuItem(name=item_name, price=float(item_price), description=item_description, restaurant_id=restaurant.id)
        storage.new(new_menu_item)
        storage.save()
        flash('Menu item added successfully!', 'success')
    return render_template('add_menu_item.html', title="Create New item")

@app.route('/add_item_to_cart/<int:item_id>', methods=['GET', 'POST'])
def add_item_to_cart(item_id):
    menu_item = storage.get(MenuItem, item_id)
    if request.method == 'POST':
        # Logic for adding the item to the cart
        flash('Item added to cart successfully!', 'success')
        return redirect(url_for('restaurant_details', restaurant_id=menu_item.restaurant_id))
    
    return render_template('add_item_to_cart.html', menu_item=menu_item, title="Add Item to Cart")

if __name__ == '__main__':
    app.run(debug=True, port=5001)