from mechanic_shop import ma
from mechanic_shop.models.schemas import Customer
from mechanic_shop import db

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        sqla_session = db.session

customer_schema  = CustomerSchema()
customers_schema = CustomerSchema(many=True)