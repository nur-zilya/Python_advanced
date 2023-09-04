import sqlite3

def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
          name: str,
) -> None:
    sovin_salary = 100000
    query = """
        SELECT salary
        FROM `table_effective_manager`
        WHERE name = ?
    """
    cursor.execute(query, (name,))
    res = cursor.fetchone()

    if res is None:
        print(f"No employee found with the name: {name}")
        return

    if res[0] > sovin_salary:
        delete_query = "DELETE FROM `table_effective_manager` WHERE name = ?"
        cursor.execute(delete_query, (name,))
        print(f"{name} has been fired!")
    else:
        new_salary = res[0] * 1.1
        upd_query = "UPDATE `table_effective_manager` SET salary = ? WHERE name = ? "
        cursor.execute(upd_query, (new_salary, name))
        print(f"{name}'s salary has been increased to {new_salary}")

    cursor.connection.commit()


if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, "Кузнецов П.Я.")