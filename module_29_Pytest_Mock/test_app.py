import pytest
from app import create_app, db
from app import Client, Parking

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_return_clients_list(app, client):
    # Добавляем тестовые данные в базу данных
    with app.app_context():
        client1 = Client(name='John', surname='Doe', credit_card='1234', car_number='ABC123')
        client2 = Client(name='Jane', surname='Doe', credit_card='5678', car_number='XYZ456')
        db.session.add(client1)
        db.session.add(client2)

        parking1 = Parking(address='123 Main St', opened=True, count_places=20, count_available_places=10)
        parking2 = Parking(address='456 Elm St', opened=True, count_places=15, count_available_places=5)
        db.session.add(parking1)
        db.session.add(parking2)

        db.session.commit()

    # Выполняем GET запрос на /clients
    response = client.get('/clients')

    # Проверяем, что получен корректный статус код
    assert response.status_code == 200

    # Проверяем, что в ответе есть ожидаемое количество клиентов
    assert len(response.json) == 2
