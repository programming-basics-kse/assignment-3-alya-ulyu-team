import argparse
import os

parser = argparse.ArgumentParser(description="Обробка даних за 120 років Олімпійських ігор")
parser.add_argument("file", help="Шлях до файлу")
parser.add_argument("-medals", required=True, help="Назва країни? Або її код")
parser.add_argument("year", help="Рік у якому були Олімпійські ігри")
parser.add_argument("-output", help="опціональна функція до 1 завдання")

args = parser.parse_args()