from flask import Flask, render_template, request, redirect, url_for, flash, session
from hashlib import md5
from models import storage
from models.User import User
from models.Cart import Cart
from models.Restaurant import Restaurant
from models.MenuItem import MenuItem
from models.Order import Order


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def main():
    return render_template('main.html', title="EatsExpress - Home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_id = request.form['login_id']
        password = request.form['password']
        hashed_password = md5(password.encode()).hexdigest()
        user = None
        for u in storage.all(User).values():
            if (u.username == login_id or u.email == login_id) and u.password == hashed_password:
                user = u
                break
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            flash('Logged in successfully!', 'success')
            if user.username == 'Admin':
                return redirect(url_for('choice'))
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

        if email != confirm_email:
            flash('Emails do not match. Please try again.', 'danger')
            return redirect(url_for('register'))

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

@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    if user_id:
        user = storage.get(User, user_id)
        return dict(user=user)
    return dict(user=None)

@app.route('/home')
def home():
    user_id = session.get('user_id')
    if user_id:
        user = storage.get(User, user_id)
        return render_template('main_loggedin.html', title="EatsExpress - Home", user=user)
    else:
        flash('You need to log in to access this page.', 'danger')
        return redirect(url_for('login'))

@app.route('/search')
def search():
    return render_template('filter.html', title="EatsExpress - Search")

@app.route('/item')
def item():
    return render_template('add_item_to_cart.html', title="EatsExpress - item")

@app.route('/addaddress')
def addaddress():
    return render_template('add_address.html', title="EatsExpress - add address")

@app.route('/viewall')
def viewall():
    restaurants = storage.all(Restaurant).values()
    return render_template('all_restaurants.html', restaurants=restaurants, title="View All Restaurants")

@app.route('/restaurant_details/<restaurant_id>')
def restaurant_details(restaurant_id):
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        flash('Restaurant not found', 'danger')
        return redirect(url_for('viewall'))
    
    menu_items = [item for item in storage.all(MenuItem).values() if item.restaurant_id == restaurant_id]
    
    return render_template('restaurant_details.html', restaurant=restaurant, menu_items=menu_items, title=restaurant.name)

@app.route('/choice')
def choice():
    return render_template('choice.html', title="Choose Action")

@app.route('/create_restaurant', methods=['GET', 'POST'])
def create_restaurant():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        existing_restaurant = next((r for r in storage.all(Restaurant).values() if r.name == name), None)
        if existing_restaurant:
            flash('Restaurant already exists. Please try a different name.', 'warning')
            return redirect(url_for('create_restaurant'))

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

        restaurant = next((r for r in storage.all(Restaurant).values() if r.name == restaurant_name), None)
        if not restaurant:
            flash('Restaurant not found. Please try again.', 'danger')
            return redirect(url_for('add_menu_item'))

        new_menu_item = MenuItem(name=item_name, price=float(item_price), description=item_description, restaurant_id=restaurant.id)
        storage.new(new_menu_item)
        storage.save()
        flash('Menu item added successfully!', 'success')
    return render_template('add_menu_item.html', title="Create New item")

@app.route('/view_account')
def view_account():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('viewaccount.html', user=user, title="View Account")
    else:
        flash('You need to log in to view your account.', 'danger')
        return redirect(url_for('login'))

@app.route('/accountdetails')
def accountdetails():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('accountdetails.html', user=user, title="Account Details")
    else:
        flash('You need to log in to view your account.', 'danger')
        return redirect(url_for('login'))

@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            storage.delete(user)
            storage.save()
            session.pop('user_id', None)
            flash('Your account has been deleted.', 'success')
            return redirect(url_for('main'))
        else:
            flash('User not found.', 'danger')
    else:
        flash('You need to log in to delete your account.', 'danger')
        return redirect(url_for('login'))

@app.route('/add_item_to_cart/<menu_item_id>', methods=['GET', 'POST'])
def add_item_to_cart(menu_item_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        menu_item = storage.get(MenuItem, menu_item_id)
        restaurant = storage.get(Restaurant, menu_item.restaurant_id)
        
        # Check for existing carts from other restaurants
        existing_cart = None
        for cart in storage.all(Cart).values():
            if cart.user_id == user.id:
                if cart.restaurant_id != restaurant.id:
                    existing_cart = cart
                    break

        if existing_cart and request.method == 'POST' and 'confirm' not in request.form:
            quantity = int(request.form['quantity'])
            message = 'You already have items in your cart from another restaurant. Adding this item will remove items from the other restaurant. Do you want to proceed?'
            return render_template('confirm_delete_cart.html', menu_item=menu_item, title="Confirm Delete Cart", restaurant=restaurant, existing_cart=existing_cart, message=message, quantity=quantity)

        if request.method == 'POST':
            quantity = int(request.form['quantity'])

            if existing_cart and 'confirm' in request.form and request.form['confirm'] == 'yes':
                storage.delete(existing_cart)
                storage.save()

            cart = next((c for c in storage.all(Cart).values() if c.user_id == user.id and c.restaurant_id == restaurant.id), None)

            if not cart:
                # Create a new cart if it doesn't exist
                cart = Cart(user_id=user.id, restaurant_id=restaurant.id)
                storage.new(cart)
                storage.save()

            # Add item to cart
            cart.add_item(menu_item_id=menu_item.id, menu_item_name=menu_item.name, quantity=quantity, price=menu_item.price)

            storage.save()
            flash('Item added to cart!', 'success')
            return redirect(url_for('view_cart'))
        
        return render_template('add_item_to_cart.html', menu_item=menu_item, title="Add Item to Cart")
    else:
        flash('You need to log in to add items to the cart.', 'danger')
        return redirect(url_for('login'))


@app.route('/view_cart')
def view_cart():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        carts = storage.all(Cart).values()
        cart = next((c for c in carts if c.user_id == user.id), None)

        if cart and cart.menu_items:
            restaurant = storage.get(Restaurant, cart.restaurant_id)
            return render_template('viewcart.html', cart_items=cart.menu_items, restaurant=restaurant, title="Cart")
        else:
            flash('Your cart is empty.', 'info')
            return redirect(url_for('home'))
    else:
        flash('You need to log in to view your cart.', 'danger')
        return redirect(url_for('login'))

@app.route('/completeorder', methods=['GET', 'POST'])
def completeorder():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        cart = next((c for c in storage.all(Cart).values() if c.user_id == user.id), None)  # Fetch cart for the user

        if cart:
            restaurant = storage.get(Restaurant, cart.restaurant_id)
            restaurant_delivery_time = restaurant.delivery_time  # Get the restaurant's delivery time
            delivery_time = restaurant_delivery_time + 10  # Add 10 minutes to the restaurant's delivery time
            total_price = sum(item['price'] for item in cart.menu_items)

            if request.method == 'POST':
                address = request.form['address']

                # Create a new order
                new_order = Order(
                    user_id=user.id,
                    restaurant_id=cart.restaurant_id,
                    total_price=total_price,
                    address=address,
                    delivery_time=f"{delivery_time} minutes"
                )

                # Add menu items to the order
                for item in cart.menu_items:
                    new_order.menu_items.append(item)

                storage.new(new_order)
                storage.save()

                # Delete the cart after placing the order
                storage.delete(cart)
                storage.save()

                flash('Order placed successfully!', 'success')
                return redirect(url_for('home'))

            return render_template('complete_order.html', title="Complete Order", cart_items=cart.menu_items, total_price=total_price, delivery_time=delivery_time)
        else:
            flash('Your cart is empty.', 'info')
            return redirect(url_for('main'))
    else:
        flash('You need to log in to complete your order.', 'danger')
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
