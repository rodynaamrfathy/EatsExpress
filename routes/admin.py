from flask import render_template, request, redirect, url_for, flash, session
from app import app
from models import storage
from models.Restaurant import Restaurant
from models.MenuItem import MenuItem
from models.Order import Order
from models.User import User
import os
from werkzeug.utils import secure_filename
from helper_functions import allowed_file, ensure_upload_folder_exists

@app.route('/adminpage')
def adminpage():
    user_id = session.get('user_id')
    if not user_id:
        flash('You need to log in to access this page.', 'danger')
        return redirect(url_for('login'))

    user = storage.get(User, user_id)
    if not user or not user.email.endswith("@eatsexpress.com"):
        flash('Unauthorized access. Only admins can view this page.', 'danger')
        return redirect(url_for('home'))

    filter_status = request.args.get('status', 'all')
    orders = storage.all(Order).values()
    if filter_status != 'all':
        orders = [order for order in orders if order.status == filter_status]
    else:
        orders = [order for order in orders if order.status != 'delivered']

    is_general_admin = user.email == "Admin@eatsexpress.com"
    restaurant_id = None if is_general_admin else user.restaurant_id

    order_list = [{
        'id': order.id,
        'restaurant_name': storage.get(Restaurant, order.restaurant_id).name if storage.get(Restaurant, order.restaurant_id) else "Unknown Restaurant",
        'total_price': order.total_price,
        'address': order.address,
        'delivery_time': order.delivery_time,
        'created_at': order.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'status': order.status
    } for order in orders]

    # If not a general admin, filter orders to include only those from the admin's restaurant
    if not is_general_admin:
        order_list = [order for order in order_list if order['restaurant_name'] == storage.get(Restaurant, restaurant_id).name]

    return render_template('adminpage.html', title="Choose Action", orders=order_list, email=user.email)


@app.route('/create_restaurant', methods=['GET', 'POST'])
def create_restaurant():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        cuisines = request.form['cuisines']
        categories = request.form['categories']
        breakfast = request.form['breakfast']
        beverages = request.form['beverages']
        delivery_time = request.form['delivery_time']
        delivery_fee = float(request.form['delivery_fee'])
        image = request.files['image']

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            ensure_upload_folder_exists()
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        else:
            flash('Invalid image file.', 'danger')
            return redirect(url_for('create_restaurant'))

        existing_restaurant = next((r for r in storage.all(Restaurant).values() if r.name == name), None)
        if existing_restaurant:
            flash('Restaurant already exists. Please try a different name.', 'warning')
            return redirect(url_for('create_restaurant'))

        new_restaurant = Restaurant(
            name=name,
            location=location,
            cuisines=cuisines,
            categories=categories,
            breakfast=breakfast,
            beverages=beverages,
            delivery_time=delivery_time,
            delivery_fee=delivery_fee,
            image=image_path
        )
        storage.new(new_restaurant)
        storage.save()
        flash('Restaurant created successfully!', 'success')
        return redirect(url_for('viewall'))
    
    user_id = session.get('user_id')
    if user_id:
        user = storage.get(User, user_id)
        if user and user.username == "Admin" and user.email == "Admin@eatsexpress.com":
            return render_template('create_restaurant.html', title="Create New Restaurant")
    flash('Only admins have access to this page.', 'danger')
    return redirect(url_for('home'))

@app.route('/add_menu_item', methods=['GET', 'POST'])
def add_menu_item():
    user_id = session.get('user_id')
    if not user_id:
        flash('You need to log in to access this page.', 'danger')
        return redirect(url_for('login'))
    
    user = storage.get(User, user_id)
    if not user or not user.email.endswith("@eatsexpress.com"):
        flash('Unauthorized access. Only admins can view this page.', 'danger')
        return redirect(url_for('home'))

    # Determine if the user is a general admin or a restaurant-specific admin
    is_general_admin = user.email == "Admin@eatsexpress.com"
    restaurant = None if is_general_admin else storage.get(Restaurant, user.restaurant_id)
    restaurant_name = None if is_general_admin else restaurant.name

    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name'] if is_general_admin else restaurant_name
        menu_item_name = request.form['menu_item_name']
        menu_item_price = request.form['menu_item_price']
        menu_item_description = request.form['menu_item_description']
        image = request.files['image']

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            ensure_upload_folder_exists()
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        else:
            flash('Invalid image file.', 'danger')
            return redirect(url_for('add_menu_item'))

        restaurant = next((r for r in storage.all(Restaurant).values() if r.name == restaurant_name), None)
        if not restaurant:
            flash('Restaurant not found. Please try again.', 'danger')
            return redirect(url_for('add_menu_item'))

        new_menu_item = MenuItem(
            name=menu_item_name,
            price=float(menu_item_price),
            description=menu_item_description,
            restaurant_id=restaurant.id,
            image=image_path
        )
        storage.new(new_menu_item)
        storage.save()
        flash('Menu item added successfully!', 'success')
        return redirect(url_for('viewall'))

    # Render the page differently based on the type of admin
    return render_template('add_menu_item.html', title="Create New Item", 
                           restaurant_name=restaurant_name, is_general_admin=is_general_admin)

@app.route('/cancelorder', methods=['POST'])
def cancelorder():
    order_id = request.form.get('order_id')
    order = storage.get(Order, order_id)
    if order:
        order.status = 'cancelled'
        storage.save()
        flash('Order cancelled.', 'success')
    else:
        flash('Order not found.', 'danger')

    return redirect(url_for('adminpage'))

@app.route('/confirmorder', methods=['POST'])
def confirmorder():
    order_id = request.form.get('order_id')
    order = storage.get(Order, order_id)
    if order:
        order.status = 'confirmed'
        storage.save()
        flash('Order confirmed.', 'success')
    else:
        flash('Order not found.', 'danger')

    return redirect(url_for('adminpage'))

@app.route('/orderprepared', methods=['POST'])
def orderprepared():
    order_id = request.form.get('order_id')
    order = storage.get(Order, order_id)
    if order:
        order.status = 'prepared'
        storage.save()
        flash('Order confirmed.', 'success')
    else:
        flash('Order not found.', 'danger')

    return redirect(url_for('adminpage'))

@app.route('/outfordelivery', methods=['POST'])
def outfordelivery():
    order_id = request.form.get('order_id')
    order = storage.get(Order, order_id)
    if order:
        order.status = 'out for delivery'
        storage.save()
        flash('Order confirmed.', 'success')
    else:
        flash('Order not found.', 'danger')

    return redirect(url_for('adminpage'))