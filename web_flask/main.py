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
        ){
  "Restaurant.156d856e-ae28-4a79-b718-8f90619ab607": {
    "name": "Garnell's Sushi",
    "location": "123 Ocean View Blvd, Santa Monica",
    "created_at": "2024-06-27T22:36:10.415459",
    "updated_at": "2024-06-27T22:36:10.415461",
    "id": "156d856e-ae28-4a79-b718-8f90619ab607",
    "__class__": "Restaurant"
  },
  "Restaurant.fabe3d7e-ad26-4ef3-bea5-e8e14d0317d1": {
    "name": "Vinny's Pizzeria",
    "location": "789 River St, New York",
    "created_at": "2024-06-27T22:38:03.890902",
    "updated_at": "2024-06-27T22:38:03.890906",
    "id": "fabe3d7e-ad26-4ef3-bea5-e8e14d0317d1",
    "__class__": "Restaurant"
  },
  "MenuItem.f840de6d-3016-45bd-a9d1-8c11e1c9f58d": {
    "name": "Salmon Nigiri",
    "price": 10.0,
    "description": "Fresh salmon over a bed of sushi rice.",
    "restaurant_id": "156d856e-ae28-4a79-b718-8f90619ab607",
    "created_at": "2024-06-27T22:40:54.035820",
    "updated_at": "2024-06-27T22:40:54.035839",
    "id": "f840de6d-3016-45bd-a9d1-8c11e1c9f58d",
    "__class__": "MenuItem"
  },
  "MenuItem.585c3e41-6b04-4d03-8f33-89b0d0225631": {
    "name": "Miso Soup",
    "price": 25.0,
    "description": "Traditional Japanese miso soup with tofu and seaweed.",
    "restaurant_id": "156d856e-ae28-4a79-b718-8f90619ab607",
    "created_at": "2024-06-27T23:01:22.191478",
    "updated_at": "2024-06-27T23:01:22.191483",
    "id": "585c3e41-6b04-4d03-8f33-89b0d0225631",
    "__class__": "MenuItem"
  },
  "User.e271aaf3-e21c-4fa8-bc64-e32d49c0aa93": {
    "username": "roddy",
    "email": "rodyna@gmail.com",
    "password": "202cb962ac59075b964b07152d234b70",
    "created_at": "2024-06-27T23:17:25.511937",
    "updated_at": "2024-06-27T23:17:25.511961",
    "id": "e271aaf3-e21c-4fa8-bc64-e32d49c0aa93",
    "__class__": "User"
  },
  "Restaurant.8df97267-4799-4d09-afca-819d09d069db": {
    "name": "Roma Pizza",
    "location": "456 Mountain Rd, Denver",
    "created_at": "2024-06-28T00:11:49.321698",
    "updated_at": "2024-06-28T00:11:49.321703",
    "id": "8df97267-4799-4d09-afca-819d09d069db",
    "__class__": "Restaurant"
  },
  "MenuItem.8965bbe8-3e4c-481c-b818-103c94656b86": {
    "name": "Meat Lover's Pizza",
    "price": 15.0,
    "description": "Pepperoni, ham, sausage, bacon, and mozzarella.",
    "restaurant_id": "8df97267-4799-4d09-afca-819d09d069db",
    "created_at": "2024-06-28T00:12:23.899519",
    "updated_at": "2024-06-28T00:12:23.899521",
    "id": "8965bbe8-3e4c-481c-b818-103c94656b86",
    "__class__": "MenuItem"
  },
  "MenuItem.e401ce81-a861-4a54-b38d-5db246beae8a": {
    "name": "Garlic Bread",
    "price": 24.0,
    "description": "Crispy bread with garlic butter and herbs.",
    "restaurant_id": "8df97267-4799-4d09-afca-819d09d069db",
    "created_at": "2024-06-28T00:12:40.694386",
    "updated_at": "2024-06-28T00:12:40.694389",
    "id": "e401ce81-a861-4a54-b38d-5db246beae8a",
    "__class__": "MenuItem"
  },
  "MenuItem.f5ea5ff4-8511-47d0-abeb-036d6814103c": {
    "name": "Caesar Salad",
    "price": 160.0,
    "description": "Romaine lettuce with Caesar dressing, croutons, and parmesan cheese.",
    "restaurant_id": "8df97267-4799-4d09-afca-819d09d069db",
    "created_at": "2024-06-28T00:13:43.599231",
    "updated_at": "2024-06-28T00:13:43.599235",
    "id": "f5ea5ff4-8511-47d0-abeb-036d6814103c",
    "__class__": "MenuItem"
  },
  "User.39cda39d-8f7c-41e4-8899-5ed9cb2084c9": {
    "username": "Admin",
    "email": "Admin@eatsexpress.com",
    "password": "202cb962ac59075b964b07152d234b70",
    "created_at": "2024-06-28T20:56:29.966587",
    "updated_at": "2024-06-28T20:56:29.966627",
    "id": "39cda39d-8f7c-41e4-8899-5ed9cb2084c9",
    "__class__": "User"
  },
  "User.b3a36c97-b356-48ce-922f-c7c17646b36b": {
    "username": "moessam",
    "email": "moessam@gmail.com",
    "password": "202cb962ac59075b964b07152d234b70",
    "created_at": "2024-06-28T21:17:23.088303",
    "updated_at": "2024-06-28T21:17:23.088346",
    "id": "b3a36c97-b356-48ce-922f-c7c17646b36b",
    "__class__": "User"
  },
  "Restaurant.7d2405a7-9236-4b42-9278-15d355fb8635": {
    "name": "blabla",
    "location": "blabla",
    "created_at": "2024-06-28T22:17:32.646786",
    "updated_at": "2024-06-28T22:17:32.646788",
    "id": "7d2405a7-9236-4b42-9278-15d355fb8635",
    "__class__": "Restaurant"
  },
  "User.719be397-235a-44f2-a3be-6ca422ed353b": {
    "username": "rodynaamr",
    "email": "rodynaamr@gmail.com",
    "password": "4a7d1ed414474e4033ac29ccb8653d9b",
    "first_name": "rodyna",
    "last_name": "amr",
    "phone_number": "+20 01060840111",
    "created_at": "2024-06-29T06:25:24.488875",
    "updated_at": "2024-06-29T06:25:24.488878",
    "id": "719be397-235a-44f2-a3be-6ca422ed353b",
    "__class__": "User"
  },
  "User.4a2d9e6e-f8a3-49ee-864c-bbc481e602ce": {
    "username": "moyasser",
    "email": "mooyasser@gmail.com",
    "password": "202cb962ac59075b964b07152d234b70",
    "first_name": "mohamed",
    "last_name": "yaser",
    "phone_number": "+20 01060840111",
    "created_at": "2024-06-29T08:14:51.856989",
    "updated_at": "2024-06-29T08:14:51.856992",
    "id": "4a2d9e6e-f8a3-49ee-864c-bbc481e602ce",
    "__class__": "User"
  },
  "Cart.e4f55650-63c5-43bd-aba2-6938a94bcc5c": {
    "user_id": "4a2d9e6e-f8a3-49ee-864c-bbc481e602ce",
    "restaurant_id": "8df97267-4799-4d09-afca-819d09d069db",
    "created_at": "2024-06-30T21:27:11.299520",
    "updated_at": "2024-06-30T21:27:11.299522",
    "id": "e4f55650-63c5-43bd-aba2-6938a94bcc5c",
    "menu_items": [
      {
        "id": "8965bbe8-3e4c-481c-b818-103c94656b86",
        "name": "Meat Lover's Pizza",
        "quantity": 2,
        "price": 30.0
      },
      {
        "id": "f5ea5ff4-8511-47d0-abeb-036d6814103c",
        "name": "Caesar Salad",
        "quantity": 3,
        "price": 480.0
      }
    ],
    "__class__": "Cart"
  }
}
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
