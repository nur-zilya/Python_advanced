import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from wtforms import Form, StringField, validators


db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    return app


app = create_app()


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    credit_card = db.Column(db.String(50))
    car_number = db.Column(db.String(10))


class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    opened = db.Column(db.Boolean)
    count_places = db.Column(db.Integer, nullable=False)
    count_available_places = db.Column(db.Integer, nullable=False)


class ClientParking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'))
    time_in = db.Column(db.DateTime)
    time_out = db.Column(db.DateTime)

    client = db.relationship('Client', backref=db.backref('parkings'))
    parking = db.relationship('Parking', backref=db.backref('clients'))

class ClientForm(Form):
    name = StringField('Name', validators=[validators.InputRequired(), validators.Length(max=50)])
    surname = StringField('Surname', validators=[validators.InputRequired(), validators.Length(max=50)])
    credit_card = StringField('Credit Card', validators=[validators.InputRequired(), validators.Length(max=50)])
    car_number = StringField('Car Number', validators=[validators.InputRequired(), validators.Length(max=10)])


@app.route('/client', methods=['GET'])
def hi():
    return "Hi"

@app.route('/clients', methods=['GET'])
def return_clients_list():
    clients = Client.query.all()
    clients_list = []

    for client in clients:
        client_data = {
            'id' : client.id,
            'name' : client.name,
            'surname' : client.surname,
            'credit_card' : client.credit_card,
            'car_number' : client.car_number
        }

        clients_list.append(client_data)

    return jsonify(clients_list)


@app.route('/clients/<int:id>', methods=['GET'])
def return_client(id):
    client = Client.query.get(id)
    if client:
        client_data = {
            'id': client.id,
            'name': client.name,
            'surname': client.surname,
            'credit_card': client.credit_card,
            'car_number': client.car_number
        }
        return jsonify(client_data)
    else:
        return jsonify({'error': 'Client not found'}), 404



@app.route('/clients', methods=['POST'])
def create_client():
    # Parse JSON data from request
    data = request.json

    # Validate form data
    form = ClientForm(data=data)
    if form.validate():
        # Extract data from form
        name = data.get('name')
        surname = data.get('surname')
        credit_card = data.get('credit_card')
        car_number = data.get('car_number')

        # Create new client
        new_client = Client(name=name, surname=surname, credit_card=credit_card, car_number=car_number)
        db.session.add(new_client)
        db.session.commit()

        # Return success response
        return jsonify({'message': 'Client created successfully'}), 201
    else:
        # Return validation error response
        return jsonify({'error': 'Validation failed', 'errors': form.errors}), 400



@app.route('/client_parkings/<client_id>/<parking_id>', methods=['POST'])
def parking_car(client_id, parking_id):
    data = request.json
    client_id = data.get('client_id')
    parking_id = data.get('parking_id')

    parking = Parking.query.get(parking_id)
    if not parking.opened:
        return jsonify({'error': 'Parking is closed now'}), 400

    if parking.count_available - 1 < 0:
        return jsonify({'error': 'There is no parking places now'}), 400
    else:
        parking.count_available -= 1
    db.session.commit()

    time_in = datetime.now()

    client_parking = ClientParking(client_id=client_id, parking_id=parking_id, time_in=time_in)
    db.session.add(client_parking)
    db.session.commit()

    return jsonify({'message': 'Car parked successfully'}), 201


from datetime import datetime

@app.route('/client_parkings/<int:client_id>/<int:parking_id>', methods=['DELETE'])
def delete_parking(client_id, parking_id):
    data = request.json

    time_out = datetime.now()
    client_parking = ClientParking.query.filter_by(client_id=client_id, parking_id=parking_id).first()
    if client_parking:
        client_parking.time_out = time_out
        db.session.commit()

        parking = Parking.query.get(parking_id)
        parking.count_available_places += 1
        db.session.commit()

        return jsonify({'message': 'Car left the parking successfully'}), 200
    else:
        return jsonify({'error': 'No parking entry found for the specified client and parking'}), 404



if __name__ == '__main__':
    app = create_app()
    app.run()


