from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/service_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    from mechanic_shop.blueprints.customers import customers_bp
    from mechanic_shop.blueprints.mechanics import mechanics_bp
    from mechanic_shop.blueprints.service_tickets import service_tickets_bp

    app.register_blueprint(customers_bp)
    app.register_blueprint(mechanics_bp)
    app.register_blueprint(service_tickets_bp)

    return app