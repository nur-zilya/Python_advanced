from typing import List, Dict, Optional
from dataclasses import dataclass
import sqlite3

DATA = [
    {'id': 0, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'A bite of Python', 'author': 'Swaroop C. H.'},
    {'id': 2, 'title': 'War and Peace', 'author': 'Leo Tolstoy'}
]


@dataclass
class Book:
    title: str
    author: str
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Author:
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    id: Optional[int] = None

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


def _get_book_obj_from_row(row) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM `table_books`')
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


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


def add_new_book(book: Book) -> Book:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        query = f"""
                INSERT INTO table_books (title, author) VALUES 
                (?, ?)
                    """
        cursor.execute(query, (book.title, book.author))
        book.id = cursor.lastrowid
        return book


def get_book_by_id(book_id: int) -> Optional[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM table_books WHERE id = "%s"' % book_id)
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def get_book_by_title(book_title: str) -> Optional[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM table_books WHERE title = "%s"' % book_title)
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def update_book_by_id(book: Book):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE table_books
            SET title = ?,
                author = ?
            WHERE id = ?
        """, (book.title, book.author, book.id))
        conn.commit()


def delete_book_by_id(book: Book):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            DELETE table_books
            WHERE ID = ?
        """, (book.id,))
        conn.commit()


if __name__ == '__main__':
    init_db(DATA)
