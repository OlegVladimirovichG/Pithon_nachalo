import json
from pprint import pprint


def convert_to_json(path, new_path):
    res = {}
    with (
        open(path, "r", encoding="utf-8") as f,
        open(new_path, 'w', encoding='utf-8') as j
    ):
        for line in f:
            name, data = line.split(' - ')
            res[name.upper()] = data[:-1]

        return json.dump(res, j)


convert_to_json('../Seminar 7/out/task_3.txt', 'out/task_1.json')