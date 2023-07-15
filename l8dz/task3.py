# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv
import json


def convert_to_csv():
    with (
        open('out/task_2.json', 'r', encoding='utf-8') as j,
        open('out/task_3.csv', 'w', newline='', encoding='utf-8') as c
    ):
        json_file = json.load(j)
        dict_list = []
        for k in json_file.keys():
            for i, n in json_file[k].items():
                dict_list.append({'access': k, 'id_': i, 'name': n})
        writer = csv.DictWriter(c, fieldnames=['access', 'id_', 'name'])
        writer.writeheader()
        writer.writerows(dict_list)


convert_to_csv()