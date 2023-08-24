import sqlite3
import datetime
from typing import Optional, List

class Room:
    def __init__(self, id: Optional[int], floor: int, beds: int, guestsNum: int, price: float):
        self.id = id
        self.floor = floor
        self.beds = beds
        self.guestNum = guestsNum
        self.price = price

    def __getitem__(self, item):
        return getattr(self, item)


class Order:
    def __init__(self, id: Optional[int], checkIn: datetime, checkOut: datetime, firstname: str, surname: str, roomId: int):
        self.id = id
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.firstname = firstname
        self.surname = surname
        self.roomId = roomId


def get_rooms():


def init_db(initial_records: List):
    with sqlite3.connect('table_rooms.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `table_rooms` (
            id PRIMARY KEY AUTOINCREMENT,
            floor INTEGER,
            beds INTEGER,
            guestNum INTEGER,
            price FLOAT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `table_orsers` (
            id PRIMARY KEY AUTOINCREMENT,
            checkIn DATETIME,
            checkOut DATETIME,
            firstName VARCHAR(255),
            surname VARCHAR(255),
            roomId INTEGER
            FOREIGN KEY (roomId) REFERENCES table_rooms(id)            
            );
        """)
