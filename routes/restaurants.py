from flask import render_template, session, redirect, url_for, flash, request
from app import app
from models import storage
from models.Restaurant import Restaurant
from models.MenuItem import MenuItem


@app.route('/filter_restaurants/<filter_by>/<filter_value>')
def filter_restaurants(filter_by, filter_value):
    restaurants = []
    for restaurant in storage.all(Restaurant).values():
        if filter_by == 'cuisines' and filter_value in restaurant.cuisines:
            restaurants.append(restaurant)
        elif filter_by == 'categories' and filter_value in restaurant.categories:
            restaurants.append(restaurant)
        elif filter_by == 'breakfast' and filter_value in restaurant.breakfast:
            restaurants.append(restaurant)
        elif filter_by == 'beverages' and filter_value in restaurant.beverages:
            restaurants.append(restaurant)
    if restaurants == []:
        flash('No restaurants found.', 'danger')
    return render_template('filtered_restaurants.html', restaurants=restaurants, title=f"Restaurants - {filter_value}")

@app.route('/search_restaurants', methods=['GET'])
def search_restaurants():
    query = request.args.get('query', '').lower()
    if not query:
        flash('Please enter a search query.', 'warning')
        return redirect(url_for('home'))
    
    restaurants = []
    for restaurant in storage.all(Restaurant).values():
        if (query in restaurant.location.lower() or
            query in restaurant.cuisines.lower() or
            query in restaurant.categories.lower() or
            query in restaurant.breakfast.lower() or
            query in restaurant.beverages.lower()):
            restaurants.append(restaurant)
    if restaurants == []:
        flash('No restaurants found.', 'danger')
    return render_template('filtered_restaurants.html', restaurants=restaurants, title=f"Search Results for '{query}'")


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


@app.route('/item')
def item():
    return render_template('add_item_to_cart.html', title="EatsExpress - item")


