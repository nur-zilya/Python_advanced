import datetime
import sqlite3

def update_work_schedule() -> None:
    with sqlite3.connect("homework.db") as conn:
        cursor = conn.cursor()
        joined = """
                        SELECT * FROM `table_friendship_employees` te
                        JOIN `table_friendship_schedule` tsh ON te.id = tsh.employee_id
                        """
        cursor.execute(joined)
        joined_table = cursor.fetchall()
        hobbies = {'футбол': 'Monday', 'хоккей': 'Tuesday', 'шахматы': 'Wednesday',
                   'SUP сёрфинг': 'Thursday', 'бокс':'Friday', 'Dota2': 'Saturday', 'шах-бокс': 'Sunday'}
        records_to_del = []
        for row in joined_table:
            date = row[4]
            year, month, day = int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2])
            weekday = datetime.date(year, month, day).strftime("%A")
            hob = row[2]
            if weekday == hobbies[hob]:
                records_to_del.append(row)
        for row in records_to_del:
            delete_query = "DELETE FROM `table_friendship_schedule` WHERE employee_id = ? AND date = ?"
            cursor.execute(delete_query, (row[0], row[4]))
        conn.commit()


if __name__ == "__main__":
    update_work_schedule()
