''' Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.'''
import csv
import json


def back_to_json(origin_file, new_file):
    with (
        open(origin_file, 'r', encoding='utf-8') as c,
        open(new_file, 'w', encoding='utf-8') as j
    ):
        csv_file = csv.reader(c)
        res = []
        headers = []
        for i, [access, id_, name] in enumerate(csv_file):
            if i:
                if len(id_) < 10:
                    id_ = f'{int(id_):010}'
                name = name.title()
                name_hash = str(hash(name + id_))
                res.append(dict(zip(headers, [access, id_, name, name_hash])))
            else:
                headers = [access, id_, name] + ['name_hash']
        json.dump(res, j)

back_to_json('out/task_3.csv', 'out/task_4.json')