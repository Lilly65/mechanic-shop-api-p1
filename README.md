# Mechanic Shop API

A REST API for managing a mechanic shop, built with Flask and SQLAlchemy. This first version establishes the core data model and full CRUD functionality for customers, mechanics, and service tickets.

## Features

- Full CRUD operations for customers, mechanics, and service tickets
- Many-to-many relationship between service tickets and mechanics, with routes to assign and remove mechanics from a ticket
- One-to-many relationship between customers and their service tickets
- Marshmallow schemas for serializing and deserializing data
- Application Factory Pattern with modular blueprints

## Tech Stack

- Flask
- Flask-SQLAlchemy (MySQL)
- Flask-Marshmallow / marshmallow-sqlalchemy

## Project Structure

```
mechanic_shop/
├── __init__.py            # create_app factory, blueprint registration
├── models/
│   └── schemas.py         # Customer, ServiceTicket, Mechanic models + junction table
└── blueprints/
    ├── customers/         # __init__.py, routes.py, schemas.py
    ├── mechanics/
    └── service_tickets/
app.py                     # entry point
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install flask flask-sqlalchemy mysql-connector-python flask-marshmallow marshmallow-sqlalchemy
```

Create the database in MySQL Workbench:

```sql
CREATE DATABASE service_db;
```

Set the connection string in `mechanic_shop/__init__.py`:

```
mysql+mysqlconnector://root:<password>@localhost/service_db
```

## Running

```bash
python app.py
```

The API runs at `http://127.0.0.1:5000`.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /customers/ | Create a customer |
| GET | /customers/ | Retrieve all customers |
| GET | /customers/<id> | Retrieve one customer |
| PUT | /customers/<id> | Update a customer |
| DELETE | /customers/<id> | Delete a customer |
| POST | /mechanics/ | Create a mechanic |
| GET | /mechanics/ | Retrieve all mechanics |
| PUT | /mechanics/<id> | Update a mechanic |
| DELETE | /mechanics/<id> | Delete a mechanic |
| POST | /service-tickets/ | Create a service ticket |
| GET | /service-tickets/ | Retrieve all service tickets |
| PUT | /service-tickets/<ticket_id>/assign-mechanic/<mechanic_id> | Assign a mechanic |
| PUT | /service-tickets/<ticket_id>/remove-mechanic/<mechanic_id> | Remove a mechanic |

## Testing

Endpoints are tested with a Postman collection included in the repository.
