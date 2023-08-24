from flask import Flask, requests, jsonify

app = Flask(__name__)

@app.route('/room', methods=['GET'])
def get_room():
    if requests.args.get('checkIn') and requests.args.get('checkOut'):
        rooms = get_rooms(requests.args.get('checkIn'), requests.args.get('checkOut'))



