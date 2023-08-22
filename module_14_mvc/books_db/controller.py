from typing import List, Dict

from models import get_all_books, get_all_books_of_author, count_books
from flask import Flask

app = Flask(__name__)

BOOKS = [
    {'id': 0, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 2, 'title': 'War and Peace', 'author': 'Leo Tolstoy'}
]

def get_html_table_for_books(books: List[Dict]) -> str:
    table = """
        <table>
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
    return """
        <html>
            <head>
            </head>
            <body>
                <h1>Total books {total_num}</h1>
                {table}
            </body>
            </html>
    """.format(total_num=count_books(), table=get_html_table_for_books(get_all_books()))

@app.route('/author/<author>')
def all_books_of_author(author) ->str:
    return """
        <html>
            <head>
            </head>
            <body>
                <h1>Books:</h1>
                {table}
            </body>
            </html>
    """.format(table=get_html_table_for_books(get_all_books_of_author(author)))


if __name__ == "__main__":
    app.run(debug=True)

