import sqlite3

def delete_wrong_fees(
        cursor: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    query = """
        DELETE FROM table_fees
        WHERE truck_number = ? AND timestamp = ?
    """
    with open(wrong_fees_file, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            number, time = line.split(',')
            cursor.execute(query, (number, time))
        cursor.connection.commit()


if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor,'./wrong_fees.csv')
