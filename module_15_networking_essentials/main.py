from flask import Flask, jsonify, request, Response
from models import get_rooms, init_db, add_room_to_db, Room

app = Flask(__name__)

@app.route('/room', methods=['GET'])
def get_room():
    check_in = request.args.get('checkIn')
    check_out = request.args.get('checkOut')

    if check_in and check_out:
        rooms = get_rooms(check_in, check_out)
    else:
        rooms = get_rooms()  # Assuming this is what you intended

    properties = {'rooms': []}
    for room in rooms:
        properties["rooms"].append({
            'roomId': room.id,
            'floor': room.floor,
            'beds': room.beds,
            'guestsNum': room.guestsNum,
            'price': room.price
        })
    return jsonify(properties)

@app.route('/add-room', methods=['POST'])
def add_room() -> Response:
    if request.method == "POST":
        data = request.get_json()
        room = Room(
            id=None,
            floor=data["floor"],
            beds=data["beds"],
            guestsNum=data["guestsNum"],
            price=data["price"]
        )
        add_room_to_db(room)
        return Response(status=200)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
