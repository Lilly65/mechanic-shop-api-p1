from mechanic_shop import ma, db
from mechanic_shop.models.schemas import ServiceTicket

class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        sqla_session = db.session
        include_fk = True

service_ticket_schema  = ServiceTicketSchema()
service_tickets_schema = ServiceTicketSchema(many=True)1