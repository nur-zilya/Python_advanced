from flask import Flask, jsonify, request
from my_lib import Book, ReceivingBook, Reader
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route('/return_all_books', methods=['GET'])
def return_all_books():
    books = Book.get_all_books()
    return jsonify([book.to_dict() for book in books])

@app.route('/readers', methods=['GET'])
def get_delayed_readers():
    readers = ReceivingBook.get_delayed_readers()
    return jsonify([reader.to_dict() for reader in readers])

@app.route('/borrow', methods=['POST'])
def borrow_book():
    book_id = request.json['book_id']
    student_id = request.json['student_id']
    date_of_issue = datetime.now()

@app.route('/return', methods=['POST'])
def return_book():
    book_id = request.json['book_id']
    student_id = request.json['student_id']
    date_of_return = datetime.now()

if __name__ == "__main__":
    app.run(debug=True)