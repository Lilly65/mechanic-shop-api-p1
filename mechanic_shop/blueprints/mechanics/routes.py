from flask import request, jsonify
from mechanic_shop import db
from mechanic_shop.models.schemas import Mechanic
from mechanic_shop.blueprints.mechanics import mechanics_bp
from mechanic_shop.blueprints.mechanics.schemas import mechanic_schema, mechanics_schema


@mechanics_bp.route('/', methods=['POST'])
def create_mechanic():
    try:
        mechanic_data = mechanic_schema.load(request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    new_mechanic = Mechanic(
        name=mechanic_data['name'],
        email=mechanic_data['email'],
        phone=mechanic_data['phone'],
        salary=mechanic_data['salary']
    )
    db.session.add(new_mechanic)
    db.session.commit()
    return mechanic_schema.jsonify(new_mechanic), 201


@mechanics_bp.route('/', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return mechanics_schema.jsonify(mechanics), 200


@mechanics_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = db.session.get(Mechanic, id)
    if not mechanic:
        return jsonify({"error": "Mechanic not found"}), 404
    try:
        mechanic_data = mechanic_schema.load(request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    mechanic.name   = mechanic_data['name']
    mechanic.email  = mechanic_data['email']
    mechanic.phone  = mechanic_data['phone']
    mechanic.salary = mechanic_data['salary']
    db.session.commit()
    return mechanic_schema.jsonify(mechanic), 200


@mechanics_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = db.session.get(Mechanic, id)
    if not mechanic:
        return jsonify({"error": "Mechanic not found"}), 404
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({"message": f"Mechanic {id} deleted successfully"}), 200