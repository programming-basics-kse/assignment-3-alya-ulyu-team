import argparse
import os
from idlelib.iomenu import encoding


def perevirka(file_path, country, year, output=None)
    if not os.path.exists(file_path):
        print(f"Well fella, файл {file_path} відсутній!")
        return

    with open(file_path, 'r', encoding='utf-8') as data_mandata
        columns = data_mandata.readline().strip().split('\t')

        if "Name" not in columns or "Sport" not in columns or "Medal" not in columns or "Team" not in columns or "Year" not in columns:
            print("Well fella, у файлі відсутні потрібні колонки!")
            return

parser = argparse.ArgumentParser(description="Обробка даних за 120 років Олімпійських ігор")
parser.add_argument("file", help="Шлях до файлу")
parser.add_argument("-medals", required=True, help="Назва країни? Або її код")
parser.add_argument("year", help="Рік у якому були Олімпійські ігри")
parser.add_argument("-output", help="опціональна функція до 1 завдання")

args = parser.parse_args()