from flask import render_template, session, redirect, url_for, flash, request
from app import app
from models import storage
from models.Restaurant import Restaurant
from models.MenuItem import MenuItem


@app.route('/filter_restaurants/<filter_by>/<filter_value>')
def filter_restaurants(filter_by, filter_value):
    """
    Route to filter restaurants based on a given criterion.

    Parameters:
        filter_by (str): The attribute to filter by (e.g., cuisines, categories, breakfast, beverages).
        filter_value (str): The value to filter by.

    Returns:
        Renders the filtered restaurants page with a list of restaurants matching the filter.
    """
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
    """
    Route to search for restaurants based on a query.

    Methods:
        GET: Processes the search query and retrieves matching restaurants.

    Returns:
        Renders the search results page with a list of matching restaurants.
    """
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
    """
    Route to view all restaurants.

    Returns:
        Renders the page with a list of all restaurants.
    """
    restaurants = storage.all(Restaurant).values()
    return render_template('all_restaurants.html', restaurants=restaurants, title="View All Restaurants")

@app.route('/restaurant_details/<restaurant_id>')
def restaurant_details(restaurant_id):
    """
    Route to view details of a specific restaurant.

    Parameters:
        restaurant_id (str): The ID of the restaurant to view.

    Returns:
        Renders the restaurant details page with the restaurant and its menu items.
    """
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        flash('Restaurant not found', 'danger')
        return redirect(url_for('viewall'))
    
    menu_items = [item for item in storage.all(MenuItem).values() if item.restaurant_id == restaurant_id]
    
    return render_template('restaurant_details.html', restaurant=restaurant, menu_items=menu_items, title=restaurant.name)



