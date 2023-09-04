import sqlite3

def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    generate_table = """
        CREATE TABLE IF NOT EXISTS `table_birds` (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bird_name VARCHAR(255) NOT NULL,
        date_time DATE NOT NULL
        )
    """
    if not check_if_such_bird_already_seen(cursor, bird_name):
        cursor.executescript(generate_table)
        cursor.execute(
            """
            INSERT INTO `table_birds`(bird_name, date_time)
            VALUES(?, ?) """, (bird_name, date_time))
        cursor.connection.commit()
    else:
        print("Has seen!")

def check_if_such_bird_already_seen(
        cursor: sqlite3.Cursor,
        bird_name: str
) -> bool:
    query = """
        SELECT bird_name
        FROM `table_birds` tb
        WHERE bird_name = ?
    """
    cursor.execute(query, (bird_name,))
    result = cursor.fetchone()
    return result is not None

if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        # Create the table if it doesn't exist
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS `table_birds` (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bird_name VARCHAR(255) NOT NULL,
            date_time DATE NOT NULL
            )
        """)
        # Now log the bird
        log_bird(cursor, "Nevelichka", "08082023")

