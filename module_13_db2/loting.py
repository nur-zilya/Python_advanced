import sqlite3
import random

def generate_comands(c: sqlite3.Connection)->None:

    cursor = c.cursor()

    number_comands = random.randrange(4, 17, 4)
    comands = ["Манчестер Сити", "Бавария", "Реал Мадрид", "ПСЖ", "Ливерпуль", "Челси", "	Манчестер Юнайтед", "Интер Милан", "РБ Лейпциг", "Рома", "	Севилья", "Ювентус", "Боруссия Д", "Барселона", "Бенфика", "Атлетико Мадрид", "Вильярреал"]
    strength = random.choice["strong", "medium", "weak"]
    for cos in range(number_comands):
        cur