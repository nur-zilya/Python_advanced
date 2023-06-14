import sqlite3

sql_inq = """ SELECT COUNT(id) FROM salaries
WHERE salary < 5000;
"""
avg = """SELECT AVG(salary) FROM salaries;"""

median = """SELECT AVG(med) FROM 
(SELECT salary AS med,
ROW_NUMBER() OVER (ORDER BY salary) AS row_num,
COUNT(*) OVER() AS total_rows
FROM salaries) sub
WHERE
row_num IN (FLOOR ((total_rows + 1) / 2), CEIL((total_rows + 1) / 2));
"""

med = """SELECT salary FROM salaries ORDER BY salary LIMIT 1 OFFSET (SELECT COUNT(*) FROM salaries) / 2"""

if __name__ == "__main__":
    with sqlite3.connect('hw_4_database.db') as conn:
        cur = conn.cursor()
        cur.execute(median)
        res = cur.fetchall()
        print(res)
