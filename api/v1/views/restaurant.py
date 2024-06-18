#!/usr/bin/python3
""" Objects that handle all default RestFul API actions for Restaurants """
from models.restaurant import Restaurant
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/restaurants', methods=['GET'], strict_slashes=False)
@swag_from('documentation/restaurant/all_restaurants.yml')
def get_restaurants():
    """
    Retrieves the list of all restaurant objects
    """
    all_restaurants = storage.all(Restaurant).values()
    list_restaurants = []
    for restaurant in all_restaurants:
        list_restaurants.append(restaurant.to_dict())
    return jsonify(list_restaurants)

@app_views.route('/restaurants/<int:restaurant_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/restaurant/get_restaurant.yml', methods=['GET'])
def get_restaurant(restaurant_id):
    """ Retrieves a restaurant """
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        abort(404)

    return jsonify(restaurant.to_dict())

@app_views.route('/restaurants', methods=['POST'], strict_slashes=False)
@swag_from('documentation/restaurant/post_restaurant.yml', methods=['POST'])
def post_restaurant():
    """
    Creates a restaurant
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = Restaurant(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/restaurants/<int:restaurant_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/restaurant/put_restaurant.yml', methods=['PUT'])
def put_restaurant(restaurant_id):
    """
    Updates a restaurant
    """
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at', 'owner_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(restaurant, key, value)
    restaurant.save()
    return make_response(jsonify(restaurant.to_dict()), 200)

@app_views.route('/restaurants/<int:restaurant_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/restaurant/delete_restaurant.yml', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    """
    Deletes a restaurant
    """
    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        abort(404)

    storage.delete(restaurant)
    storage.save()
    return make_response(jsonify({}), 200)
