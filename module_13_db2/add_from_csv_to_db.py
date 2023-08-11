import sqlite3

def add_from_csv_to_db(cur, filename):
    records = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            isbn, book_name, author, publish_year = line.split(',')
            records.append(tuple([book_name, author, int(publish_year), isbn]))

        for record in records:
            cur.execute("""INSERT INTO `table_books` (book_name, author, publish_year, isbn) VALUES (?,?,?,?)""", record)


if __name__ == "__main__":
    with sqlite3.connect('practise.db') as conn:
        cur = conn.cursor()
        cur.executescript(create_table)
        add_from_csv_to_db(cur, 'book_list.csv')
        cur.connection.commit()
