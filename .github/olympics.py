import argparse
import os
from idlelib.iomenu import encoding


def perevirka(file_path, country, year, output=None):
    if not os.path.exists(file_path):
        print(f"Well fella, файл {file_path} відсутній!")
        return

    with (open(file_path, 'r', encoding='utf-8')) as data_mandata:
        columns = data_mandata.readline().strip().split('\t')

        if "Name" not in columns or "Sport" not in columns or "Medal" not in columns or "Team" not in columns or "Year" not in columns:
            print("Well fella, у файлі відсутні потрібні колонки!")
            return

        name_id = columns.index("Name")
        sport_id = columns.index("Sport")
        medal_id = columns.index("Medal")
        team_id = columns.index("Team")
        year_id = columns.index("Year")

        medalisty = []
        medals_quantity = {"Gold": 0, "Silver": 0, "Bronze": 0}

        next_line = data_mandata.readline()
        while next_line:
            rows = next_line.strip().split('\t')
            if len(rows) <= max(name_id, sport_id, medal_id, team_id, year_id):
                next_line = data_mandata.readline()
                continue

            if rows[team_id] == country and rows[year_id] == year and rows[medal_id] != "NA":
                medalisty.append((rows[name_id], rows[sport_id], rows[medal_id]))
                if rows[medal_id] in medals_quantity:
                    medals_quantity[rows[medal_id]] += 1

                next_line = data_mandata.readline()

        if not medalisty:
            print(f"Well fella, медалісти з країни {country} у {year} році відсутні!")
            return

        topovi_medalisty = medalisty[:10]

        result = "Перші 10 медалістів:\n"
        for name, sport, medal in topovi_medalisty:
            result += f"{name} - {sport} - {medal}\n"
        result += f"\nСума медалей:\nЗолото: {medals_quantity["Gold"]}, Срібло: {medals_quantity["Silver"]} Бронза: {medals_quantity["Bronze"]}"





def main():

    parser = argparse.ArgumentParser(description="Обробка даних за 120 років Олімпійських ігор")
    parser.add_argument("file", help="Шлях до файлу")
    parser.add_argument("-medals", required=True, help="Назва країни? Або її код")
    parser.add_argument("year", help="Рік у якому були Олімпійські ігри")
    parser.add_argument("-output", help="опціональна функція до 1 завдання")

    args = parser.parse_args()

    perevirka(args.file, args.medals, args.year)

if __name__ == "__main__":
    main()