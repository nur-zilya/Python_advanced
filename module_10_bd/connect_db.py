import sqlite3

sq_inq1= """ SELECT COUNT(*) FROM table_1"""

sq_inq2 = """SELECT COUNT(DISTINCT id) FROM table_1"""

sq_inq3 = """SELECT COUNT(id) FROM(SELECT id FROM table_1 
INTERSECT
SELECT id FROM table_2)
"""

if __name__ == "__main__":
    with sqlite3.connect('hw_3_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sq_inq3)
        res = cursor.fetchall()
        print(res)


