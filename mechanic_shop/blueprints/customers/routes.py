from flask import request, jsonify
from mechanic_shop import db
from mechanic_shop.models.schemas import Customer
from mechanic_shop.blueprints.customers import customers_bp
from mechanic_shop.blueprints.customers.schemas import customer_schema, customers_schema


@customers_bp.route('/', methods=['POST'])
def create_customer():
    try:
        customer_data = customer_schema.load(request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    new_customer = Customer(
        name=customer_data['name'],
        email=customer_data['email'],
        phone=customer_data['phone']
    )
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.jsonify(new_customer), 201


@customers_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers), 200


@customers_bp.route('/<int:id>', methods=['GET'])
def get_customer(id):
    customer = db.session.get(Customer, id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return customer_schema.jsonify(customer), 200


@customers_bp.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = db.session.get(Customer, id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    try:
        customer_data = customer_schema.load(request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    customer.name  = customer_data['name']
    customer.email = customer_data['email']
    customer.phone = customer_data['phone']
    db.session.commit()
    return customer_schema.jsonify(customer), 200


@customers_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = db.session.get(Customer, id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": f"Customer {id} deleted successfully"}), 200