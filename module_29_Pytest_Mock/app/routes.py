from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
    db.init_app(app)
    return app

app = create_app()

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{
        'id': client.id,
        'name': client.name,
        'surname': client.surname,
        'credit_card': client.credit_card,
        'car_number': client.car_number
    } for client in clients])

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get(client_id)
    if client:
        return jsonify({
            'id': client.id,
            'name': client.name,
            'surname': client.surname,
            'credit_card': client.credit_card,
            'car_number': client.car_number
        })
    else:
        return jsonify({'error': 'Client not found'}), 404

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client = Client(
        name=data['name'],
        surname=data['surname'],
        credit_card=data['credit_card'],
        car_number=data['car_number']
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Client created successfully'}), 201


if __name__ == '__main__':
    create_app()
    app.run(debug=True)
