from flask import render_template, session, redirect, url_for, flash
from app import app
from models.Cart import Cart
from models.User import User
from models import storage
from models.MenuItem import MenuItem
from flask import request
from models.Restaurant import Restaurant


@app.route('/add_item_to_cart/<menu_item_id>', methods=['GET', 'POST'])
def add_item_to_cart(menu_item_id):
    """
    Route to add an item to the user's cart.

    Parameters:
        menu_item_id (str): The ID of the menu item to add to the cart.

    Methods:
        GET: Renders the add item to cart page.
        POST: Processes the form to add an item to the cart.

    Returns:
        Renders the add item to cart page, confirms deletion of existing cart, or redirects based on form submission status.
    """
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
    """
    Route to view the user's cart.

    Returns:
        Renders the cart view page if the user is logged in and the cart has items, otherwise redirects to home or login.
    """
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

@app.route('/update_cart_item/<item_id>/<action>', methods=['POST'])
def update_cart_item(item_id, action):
    """
    Route to update the quantity of an item in the cart.

    Parameters:
        item_id (str): The ID of the item to update.
        action (str): The action to perform (increase or decrease).

    Methods:
        POST: Processes the form to update the item quantity.

    Returns:
        Redirects to the cart view page or displays an error message.
    """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        cart = next((c for c in storage.all(Cart).values() if c.user_id == user.id), None)

        if cart:
            item = next((i for i in cart.menu_items if str(i['id']) == item_id), None)

            if item:
                if action == 'increase':
                    item['quantity'] += 1
                elif action == 'decrease':
                    if item['quantity'] > 1:
                        item['quantity'] -= 1
                    else:
                        cart.menu_items.remove(item)
                        flash('Item was deleted from the cart', 'warning')

                storage.save()
                return redirect(url_for('view_cart'))

    flash('Something went wrong. Please try again.', 'danger')
    return redirect(url_for('view_cart'))
