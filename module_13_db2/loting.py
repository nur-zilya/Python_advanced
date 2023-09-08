import sqlite3
import random

def create_table(c: sqlite3.Connection):
    cursor = c.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `table_comands` (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comand_name TEXT,
        country TEXT,
        strength TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `table_groups` (
        command_id INTEGER PRIMARY KEY AUTOINCREMENT,
        command_name VARCHAR,
        group_name INTEGER,
        FOREIGN KEY (command_id) REFERENCES uefa_commands (id)
        )
    """)

    c.commit()

def generate_comands(c: sqlite3.Connection) -> None:
    cursor = c.cursor()
    comands = [
        "Манчестер Сити", "Бавария", "Реал Мадрид", "ПСЖ", "Ливерпуль", "Челси", "Манчестер Юнайтед", "Интер Милан",
        "РБ Лейпциг", "Рома", "Севилья", "Ювентус", "Боруссия Д", "Барселона", "Бенфика", "Атлетико Мадрид"]

    countries = ["Германия", "Испания", "Англия", "Италия", "Франция", "Португалия", "Нидерланды", "Бельгия", "Швейцария", "Хорватия",
                 "Турция", "Швеция", "Польша", "Дания", "Украина", "Австрия"]

    for command_id, command in enumerate(comands, start=1):
        country = random.choice(countries)
        strength = random.choice(["strong", "medium", "weak"])
        cursor.execute("INSERT INTO `table_comands` (comand_name, country, strength) VALUES (?, ?, ?)", (command, country, strength))


    c.commit()

def generate_groups(c: sqlite3.Connection):
    cursor = c.cursor()

    cursor.execute("SELECT * FROM `table_comands`")
    commands = cursor.fetchall()

    strong_teams = [command for command in commands if command[3] == "strong"]
    medium_teams = [command for command in commands if command[3] == "medium"]
    weak_teams = [command for command in commands if command[3] == "weak"]

    group_count = random.randrange(4,17,4)
    groups = []

    for group in range(group_count):
        new_group = {
            "group_name": group + 1,
            "teams": [
                strong_teams.pop(),
                medium_teams.pop(),
                medium_teams.pop(),
                weak_teams.pop()
            ]
        }
        groups.append(new_group)

    for group in groups:
        group_name = group["group_name"]
        for team in group["teams"]:
            team_id = team[0]
            team_name = team[1]
            cursor.execute("INSERT INTO `table_groups` (group_name, command_name) VALUES (?, ?)", (group_name, team_name))

    c.commit()


if __name__ == '__main__':
    with sqlite3.connect("uefa.db") as conn:
        create_table(conn)
        generate_comands(conn)
        generate_groups(conn)
        c = conn.cursor()
        c.execute("SELECT * FROM `table_groups`")
        res = c.fetchall()
        for row in res:
            print(row)
