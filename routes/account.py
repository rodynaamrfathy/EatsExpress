from flask import render_template, session, redirect, url_for, flash
from app import app
from models import storage
from models.User import User
from models.Order import Order
from models.Restaurant import Restaurant

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
        
        # Fetch user's orders
        orders = [order for order in storage.all(Order).values() if order.user_id == user.id]
        
        # Convert orders to dictionaries for easy rendering in the template
        order_list = []
        for order in orders:
            restaurant = storage.get(Restaurant, order.restaurant_id)
            order_dict = {
            'id': order.id,  # Include the order ID
            'restaurant_name': restaurant.name if restaurant else "Unknown Restaurant",
            'total_price': order.total_price,
            'address': order.address,
            'delivery_time': order.delivery_time,
            'created_at': order.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'status': order.status
            }
            order_list.append(order_dict)
        
        # Convert user to a dictionary
        user_dict = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
        }
        
        return render_template('accountdetails.html', user=user_dict, orders=order_list, title="Account Details")
    else:
        flash('You need to log in to view your account.', 'danger')
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('email', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('main'))

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

@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    if user_id:
        user = storage.get(User, user_id)
        return dict(user=user)
    return dict(user=None)



@app.route('/addaddress')
def addaddress():
    return render_template('add_address.html', title="EatsExpress - add address")
