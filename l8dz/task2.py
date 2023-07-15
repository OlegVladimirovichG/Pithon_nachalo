import json
from pathlib import Path


def add_to_json():
    if Path('out/task_2.json').exists():
        with open('out/task_2.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
    else:
        file = {str(k): {} for k in range(1, 8)}
    while True:
        inp = input("Введите  через пробел: Имя Идентификатор Уровень_доступа: ")
        if not inp:
            break
        name, id_, access = inp.split()
        file[access].update({id_: name})
        # file.setdefault(access, {}).update({id_: name})
    with open('out/task_2.json', 'w', encoding='utf-8') as f:
        json.dump(file, f)


add_to_json()