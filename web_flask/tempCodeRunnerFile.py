@app.route('/track_order/<order_id>')
def track_order(order_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        order = storage.get(Order, order_id)
        if order and order.user_id == user.id:
            return render_template('track_order.html', order=order, title="Track Order")
        else:
            flash('Order not found or you do not have permission to view this order.', 'danger')
            return redirect(url_for('accountdetails'))
    else:
        flash('You need to log in to track your order.', 'danger')
        return redirect(url_for('login'))