import pytest
from routes import create_app, db
from models import Client, Parking, ClientParking


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_client(app):
    with app.app_context():
        client = Client(name='John', surname='Doe', credit_card='1234', car_number='ABC123')
        db.session.add(client)
        db.session.commit()
        return client

@pytest.fixture
def test_parking(app):
    with app.app_context():
        parking = Parking(address='123 Main St', opened=True, count_places=50, count_available_places=50)
        db.session.add(parking)
        db.session.commit()
        return parking

@pytest.fixture
def test_client_parking(app, test_client, test_parking):
    with app.app_context():
        client_parking = ClientParking(client_id=test_client.id, parking_id=test_parking.id)
        db.session.add(client_parking)
        db.session.commit()
        return client_parking

def test_get_clients(client):
    response = client.get('/clients')
    assert response.status_code == 200

def test_get_client(client, test_client):
    response = client.get(f'/clients/{test_client.id}')
    assert response.status_code == 200

def test_create_client(client):
    new_client = {
        'name': 'Jane',
        'surname': 'Doe',
        'credit_card': '5678',
        'car_number': 'XYZ789'
    }
    response = client.post('/clients', json=new_client)
    assert response.status_code == 201
