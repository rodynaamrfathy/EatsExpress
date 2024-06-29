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

@app.route('/completeorder')
def completeorder():
    return render_template('complete_order.html', title="EatsExpress - complete order")

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

@app.route('/add_to_cart/<menu_item_id>', methods=['POST'])
def add_to_cart(menu_item_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        menu_item = storage.get(MenuItem, menu_item_id)
        restaurant = menu_item.restaurant

        # Check if the user already has a cart for this restaurant
        cart = storage.query(Cart).filter_by(user_id=user.id, menu_item_id=menu_item_id).first()
        if cart:
            # Update the quantity if the item already exists in the cart
            cart.quantity += 1
        else:
            # Create a new cart item
            cart = Cart(user_id=user.id, menu_item_id=menu_item_id, quantity=1)
            storage.new(cart)

        storage.save()
        flash('Item added to cart!', 'success')
        return redirect(url_for('view_cart'))
    else:
        flash('You need to log in to add items to the cart.', 'danger')
        return redirect(url_for('login'))


@app.route('/view_cart')
def view_cart():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        cart_items = storage.query(Cart).filter_by(user_id=user.id).all()
        if cart_items:
            restaurant = storage.get(Restaurant, cart_items[0].menu_item.restaurant_id)
            return render_template('viewcart.html', cart_items=cart_items, restaurant=restaurant, title="Cart")
        else:
            flash('Your cart is empty.', 'info')
            return redirect(url_for('main'))
    else:
        flash('You need to log in to view your cart.', 'danger')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
