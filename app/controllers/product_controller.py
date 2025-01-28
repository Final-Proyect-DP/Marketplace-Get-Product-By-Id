import base64
from flask import Blueprint, jsonify, request
from app.models.models import Product
from app.extensions.extensions import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/items/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    return jsonify({"message": "Product fetched successfully", "product": product.to_dict()}), 200



