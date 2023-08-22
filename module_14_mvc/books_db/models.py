from typing import List, Dict
import sqlite3

DATA = [
    {'id': 0, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 2, 'title': 'War and Peace', 'author': 'Leo Tolstoy'}
]

class Book:

    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author

    def __getitem__(self, item):
        return getattr(self, item)

def init_db(initial_records: List[dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='table_books';"
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                'CREATE TABLE `table_books` '
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT);'
            )
            cursor.executemany(
                'INSERT INTO `table_books` '
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
            )

def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM `table_books`')
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]

def get_all_books_of_author(author) -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM `table_books` WHERE author=?', (author,))
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]

def count_books():
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM `table_books`')
        num = cursor.fetchone()
        return num[0]

if __name__ == '__main__':
    init_db(DATA)
