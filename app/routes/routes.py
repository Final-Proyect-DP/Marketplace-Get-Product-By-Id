import base64
from flask import Blueprint, jsonify, request
from app.models.models import Product
from app import db

read_bp = Blueprint('read', __name__)

@read_bp.route('/items', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    if not products:
        return jsonify({"message": "No products found"}), 404

    products_list = [product.to_dict() for product in products]
    return jsonify({"message": "Products fetched successfully", "products": products_list}), 200

