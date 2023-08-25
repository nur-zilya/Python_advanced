import sqlite3
import datetime
from typing import Optional, List

class Room:
    def __init__(self, id: Optional[int], floor: int, beds: int, guestsNum: int, price: float):
        self.id = id
        self.floor = floor
        self.beds = beds
        self.guestsNum = guestsNum
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



def init_db():
    with sqlite3.connect('table_rooms.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `table_rooms` (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            floor INTEGER,
            beds INTEGER,
            guestsNum INTEGER,
            price FLOAT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `table_orsers` (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            checkIn DATETIME,
            checkOut DATETIME,
            firstName VARCHAR(255),
            surname VARCHAR(255),
            roomId INTEGER,
            FOREIGN KEY (roomId) REFERENCES table_rooms(id)            
            );
        """)


def get_rooms():
    with sqlite3.connect('table_rooms.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM `table_rooms`
        """)
        return [Room(*row) for row in cursor.fetchall()]

def add_room_to_db(room: Room):
    with sqlite3.connect('table_rooms.db') as conn:
        cursor = conn.cursor()
        query = f"""
            INSERT INTO `table_rooms` (floor, beds, guestNum, price) VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (room.floor, room.beds, room.guestsNum, room.price))
        conn.commit()