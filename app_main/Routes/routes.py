import json
from flask import Blueprint, jsonify, request
from app_main.Services.list_of_orders import get_list_of_orders

route_bp = Blueprint('route', __name__)


@route_bp.route('/get_list_of_orders', methods=['GET'])
def list_of_orders():
    data = get_list_of_orders()
    return json.dumps(data)
