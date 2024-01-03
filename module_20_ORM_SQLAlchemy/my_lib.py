from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.orm import sessionmaker, mapper, declarative_base
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
# from flask import Flask, jsonify

# app = Flask(__name__)

engine = create_engine("sqlite:///library.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Reader(Base):
    __tablename__ = 'reader'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    surname = Column(String(60), nullable=False)
    phone = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.phone}, {self.email}, {self.average_score}, {self.scholarship}"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_all_students_with_scholarship(cls, scholarship=True):
        return session.query(Reader).filter(Reader.scholarship == scholarship).all()

    @classmethod
    def get_students_by_score(cls, score: float):
        return session.query(Reader).filter(Reader.average_score > score).all()


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(String, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.count}, {self.release_date.strftime('%d %b %Y')}, {self.author_id}"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_all_books(cls):
        return session.query(Book).all()

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.surname}"


class ReceivingBook(Base):
    __tablename__ = 'receiving_book'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)
    count_date_with_book = hybrid_property(lambda self: (datetime.now() - self.date_of_issue).days if self.date_of_return is None else (
                    self.date_of_return - self.date_of_issue).days)

    def __repr__(self):
        return f"{self.book_id}, {self.student_id}, {self.date_of_issue}, {self.date_of_return}, {self.count_date_with_book}"

    @classmethod
    def get_delayed_readers(cls):
        return session.query(ReceivingBook).filter((datetime.now() - ReceivingBook.date_of_issue).days > 14).all()


Base.metadata.create_all(engine)

# @app.route('/return_all_books')
# def return_all_books():
#     books = session.query(Book).all()
#     return jsonify([book.to_dict() for book in books])
#
# @app.route('/borrow')
# def get_delayed_readers():
#     readers = session.query(ReceivingBook).filter((datetime.now() - ReceivingBook.date_of_issue).days > 14).all()
#     return jsonify([reader.to_dict() for reader in readers])
#
#
# if __name__ == "__main__":
#     app.run(debug=True)