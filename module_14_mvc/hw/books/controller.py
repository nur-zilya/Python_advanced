from flask import Flask, render_template
from typing import List, Dict
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

from models import Book, get_all_books, get_all_books_of_author, count_books, add_new_book

app = Flask(__name__)

BOOKS = [
    {'id': 0, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 2, 'title': 'War and Peace', 'author': 'Leo Tolstoy'}
]

def get_html_table_for_books(books: List[Dict]) -> str:
    table = """
        <table class="customTable">
            <thead>
                <tr>
                    <th>ID</td>
                    <th>Title</td>
                    <th>Author</td>
                </tr>
        </thead>
            <body>
                {books_rows}
            </tbody> 
        </table>                 
    """
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)

@app.route('/books')
def all_books() -> str:
    return render_template("index.html", books=get_all_books(), num=count_books())

@app.route('/author/<author>')
def all_books_of_author(author) ->str:
    # books = get_all_books_of_author(author)
    return render_template("authors_books.html", books=get_all_books_of_author(author))

class AddBookForm(FlaskForm):
    book_title = StringField(validators=[InputRequired()])
    author_name = StringField(validators=[InputRequired()])


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form() -> str:
    if request.method == 'GET':
        return render_template('add_book.html')
    elif request.method == "POST":
        form = AddBookForm(request.form)
        if form.validate_on_submit():
            book = Book(
                title=request.form["book_title"],
                author=request.form["author_name"],
                id=None
            )
            add_new_book(book)
            return render_template('add_book.html')
        else:
            return 418



if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

