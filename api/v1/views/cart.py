#!/usr/bin/python3
"""API actions for Cart management"""
from models.Cart import Cart
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/carts/<int:user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/cart/get_cart.yml')
def get_cart(user_id):
    """Retrieves the cart for a specific user."""
    cart = storage.get(Cart, user_id)
    if not cart:
        abort(404)
    return jsonify(cart.to_dict())

@app_views.route('/carts', methods=['POST'], strict_slashes=False)
@swag_from('documentation/cart/post_cart.yml')
def post_cart():
    """Creates or updates a cart."""
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    cart = Cart(**data)
    cart.save()
    return make_response(jsonify(cart.to_dict()), 201)

@app_views.route('/carts/<int:cart_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/cart/delete_cart.yml')
def delete_cart(cart_id):
    """Deletes a cart."""
    cart = storage.get(Cart, cart_id)
    if not cart:
        abort(404)
    storage.delete(cart)
    storage.save()
    return make_response(jsonify({}), 200)
