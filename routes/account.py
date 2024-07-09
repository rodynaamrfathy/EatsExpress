from flask import render_template, session, redirect, url_for, flash, request
from app import app
from models import storage
from models.User import User
from models.Order import Order
from models.Restaurant import Restaurant
from models.Address import Address

@app.route('/view_account')
def view_account():
    """
    Route to view the user's account information.

    Returns:
        Renders the account view page if the user is logged in, otherwise redirects to login.
    """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('viewaccount.html', user=user, title="View Account")
    else:
        flash('You need to log in to view your account.', 'danger')
        return redirect(url_for('login'))
    
@app.route('/accountdetails', methods=['GET', 'POST'])
def accountdetails():
    """
    Route to view detailed account information and orders.

    Returns:
        Renders the account details page with user, order, and address information if the user is logged in, otherwise redirects to login.
    """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])

        # Fetch user's orders
        orders = [order for order in storage.all(Order).values() if order.user_id == user.id]

        # Fetch user's addresses
        addresses = [address for address in storage.all(Address).values() if address.user_id == user.id]

        # Convert orders to dictionaries for easy rendering in the template
        order_list = []
        for order in orders:
            restaurant = storage.get(Restaurant, order.restaurant_id)
            address = storage.get(Address, order.address_id)  # Fetch the address using address_id
            order_dict = {
                'id': order.id,  # Include the order ID
                'restaurant_name': restaurant.name if restaurant else "Unknown Restaurant",
                'total_price': order.total_price,
                'address': address.full_address() if address else "Unknown Address",  # Use the address object
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

        return render_template('accountdetails.html', user=user_dict, orders=order_list, addresses=addresses, title="Account Details")
    else:
        flash('You need to log in to view your account.', 'danger')
        return redirect(url_for('login'))

@app.route('/delete_address/<address_id>', methods=['POST'])
def delete_address(address_id):
    """
    Route to delete an address.

    Parameters:
        address_id (str): The ID of the address to delete.

    Returns:
        Redirects to the account details page.
    """
    if 'user_id' in session:
        address = storage.get(Address, address_id)
        if address and address.user_id == session['user_id']:
            storage.delete(address)
            storage.save()
            flash('Address deleted successfully.', 'success')
        else:
            flash('Address not found or you do not have permission to delete it.', 'danger')
    else:
        flash('You need to log in to delete an address.', 'danger')
    return redirect(url_for('accountdetails'))


@app.route('/logout', methods=['POST'])
def logout():
    """
    Route to log out the user.

    Methods:
        POST: Logs out the user and clears the session.

    Returns:
        Redirects to the main page with a success message.
    """
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('email', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('main'))

@app.route('/delete_account', methods=['POST'])
def delete_account():
    """
    Route to delete the user's account.

    Methods:
        POST: Deletes the user's account and clears the session.

    Returns:
        Redirects to the main page with a success message or login page if not logged in.
    """
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
    """
    Context processor to inject user information into templates.

    Returns:
        A dictionary with the user object if logged in, otherwise None.
    """
    user_id = session.get('user_id')
    if user_id:
        user = storage.get(User, user_id)
        return dict(user=user)
    return dict(user=None)

@app.route('/addaddress', methods=['GET', 'POST'])
def addaddress():
    """
    Route to add a new address for the user.

    Methods:
        GET: Renders the add address page.
        POST: Processes the form to add a new address.

    Returns:
        Redirects to the cart view page with a success message or login page if not logged in.
    """
    if 'user_id' not in session:
        flash('You must be logged in to add an address.', 'danger')
        return redirect(url_for('login'))
    
    user_id = session.get('user_id')

    if request.method == 'POST':
        title = request.form['title']
        address_line1 = request.form['address_line1']
        address_line2 = request.form.get('address_line2', '')  # Optional field
        city = request.form['city']
        government = request.form['government']
        postal_code = request.form['postal_code']

        new_address = Address(
            title=title,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            government=government,
            postal_code=postal_code,
            country='Egypt',  # Assuming a default value if not provided
            user_id=user_id
        )
        storage.new(new_address)
        storage.save()  # Assuming this method commits the transaction

        flash('Address added successfully!', 'success')
        return redirect(url_for('view_cart'))

    return render_template('add_address.html', title="EatsExpress - Add Address")
