import sqlite3

def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
          name: str,
) -> None:
    query = """
        SELECT name, salary FROM `table_effective_manager`  
    """
    cursor.execute(query)
    res = cursor.fetchone()
    print (res)


if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, "Иван Совин")