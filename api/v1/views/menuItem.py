#!/usr/bin/python3
"""API actions for MenuItem management"""
from models.MenuItem import MenuItem
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/menu_items', methods=['GET'], strict_slashes=False)
@swag_from('documentation/menu_item/all_menu_items.yml')
def get_menu_items():
    """Retrieves the list of all menu items."""
    all_items = storage.all(MenuItem).values()
    list_items = [item.to_dict() for item in all_items]
    return jsonify(list_items)

@app_views.route('/menu_items/<int:item_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/menu_item/get_menu_item.yml')
def get_menu_item(item_id):
    """Retrieves a specific menu item by ID."""
    item = storage.get(MenuItem, item_id)
    if not item:
        abort(404)
    return jsonify(item.to_dict())

@app_views.route('/menu_items', methods=['POST'], strict_slashes=False)
@swag_from('documentation/menu_item/post_menu_item.yml')
def post_menu_item():
    """Creates a menu item."""
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    item = MenuItem(**data)
    item.save()
    return make_response(jsonify(item.to_dict()), 201)

@app_views.route('/menu_items/<int:item_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/menu_item/delete_menu_item.yml')
def delete_menu_item(item_id):
    """Deletes a specific menu item by ID."""
    item = storage.get(MenuItem, item_id)
    if not item:
        abort(404, description="Menu item not found.")
    storage.delete(item)
    storage.save()
    return make_response(jsonify({}), 200)
