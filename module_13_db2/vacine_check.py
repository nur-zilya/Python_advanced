import sqlite3

def check_if_vaccine_has_spoiled(
        cursor: sqlite3.Cursor,
        truck_number: str) -> bool:
    query = f"""
    SELECT COUNT(*) > 3 FROM table_truck_with_vaccine tb
        WHERE tb.truck_number = '{truck_number}' AND tb.temperature_in_celsius NOT BETWEEN 16 AND 20
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

if __name__ == '__main__':
    inp = input("Enter truck number: ")
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        spoil = check_if_vaccine_has_spoiled(cursor, inp)
        if spoil:
            print("Spoiled")
        else:
            print("Not spoiled")