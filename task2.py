# TODO импортировать необходимые молули
 # TODO считать содержимое csv файла
 # TODO Сериализовать в файл с отступами равными 4


# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader) #преобразуем все строки в список словарей

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4) #записываем JSON с отступами 4


if __name__ == '__main__':  #для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


