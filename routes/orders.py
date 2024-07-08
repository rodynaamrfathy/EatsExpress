from flask import render_template, session, redirect, url_for, flash, request
from app import app
from models.Order import Order
from helper_functions import convert_to_float
from models import storage
from models.User import User
from models.Cart import Cart
from models.Restaurant import Restaurant
from datetime import datetime


@app.route('/track_order/<order_id>')
def track_order(order_id):
    order = storage.get(Order, order_id)
    if not order:
        flash('Order not found.', 'danger')
        return redirect(url_for('accountdetails'))

    # Calculate if the order should be marked as delivered
    if order.status == "out for delivery":
        delivery_time_elapsed = (datetime.utcnow() - order.updated_at).total_seconds() / 60  # in minutes
        if float(delivery_time_elapsed) > float(convert_to_float(order.delivery_time)):
            order.status = "delivered"
            storage.save()  # Assuming you have a method to save the changes

    return render_template('track_order.html', order=order, title="Track Order")

@app.route('/completeorder', methods=['GET', 'POST'])
def completeorder():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        cart = next((c for c in storage.all(Cart).values() if c.user_id == user.id), None)

        if cart:
            restaurant = storage.get(Restaurant, cart.restaurant_id)
            restaurant_delivery_time = int(restaurant.delivery_time.split()[0])
            delivery_time = restaurant_delivery_time + 10
            total_price = sum(item['price'] * item['quantity'] for item in cart.menu_items)
            total_price_with_delivery = total_price + restaurant.delivery_fee

            if request.method == 'POST':
                address = request.form['address']

                new_order = Order(
                    user_id=user.id,
                    restaurant_id=cart.restaurant_id,
                    total_price=total_price_with_delivery,
                    address=address,
                    delivery_time=f"{delivery_time} minutes"
                )

                for item in cart.menu_items:
                    new_order.menu_items.append(item)

                storage.new(new_order)
                storage.save()
                storage.delete(cart)
                storage.save()

                flash('Order placed successfully!', 'success')
                return redirect(url_for('home'))

            return render_template('complete_order.html', title="Complete Order", cart_items=cart.menu_items, total_price=total_price_with_delivery, delivery_time=f"{delivery_time} minutes")
        else:
            flash('Your cart is empty.', 'info')
            return redirect(url_for('main'))
    else:
        flash('You need to log in to complete your order.', 'danger')
        return redirect(url_for('login'))
