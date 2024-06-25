#!/usr/bin/python3
""" Objects that handle all default RestFul API actions for Orders """
from models.Order import Order
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/orders', methods=['GET'], strict_slashes=False)
@swag_from('documentation/order/all_orders.yml')
def get_orders():
    """
    Retrieves the list of all order objects
    """
    all_orders = storage.all(Order).values()
    list_orders = []
    for order in all_orders:
        list_orders.append(order.to_dict())
    return jsonify(list_orders)

@app_views.route('/orders/<order_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/order/get_order.yml', methods=['GET'])
def get_order(order_id):
    """ Retrieves an order """
    order = storage.get(Order, order_id)
    if not order:
        abort(404)

    return jsonify(order.to_dict())

@app_views.route('/orders', methods=['POST'], strict_slashes=False)
@swag_from('documentation/order/post_order.yml', methods=['POST'])
def post_order():
    """
    Creates an order
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = Order(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/orders/<order_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/order/put_order.yml', methods=['PUT'])
def put_order(order_id):
    """
    Updates an order
    """
    order = storage.get(Order, order_id)
    if not order:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at', 'user_id']  # Preserving relationship fields and timestamps
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(order, key, value)
    order.save()
    return make_response(jsonify(order.to_dict()), 200)

@app_views.route('/orders/<order_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/order/delete_order.yml', methods=['DELETE'])
def delete_order(order_id):
    """
    Deletes an order
    """
    order = storage.get(Order, order_id)
    if not order:
        abort(404)

    storage.delete(order)
    storage.save()
    return make_response(jsonify({}), 200)
