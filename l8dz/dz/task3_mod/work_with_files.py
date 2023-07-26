import csv
import json
import os
import pickle
from pathlib import Path


def calculate_dir(dirname, filenames):
    dir_size = 0
    dir_dict, dir_list = [], []
    for file in filenames:
        file = Path(file)
        size = os.path.getsize(dirname / file)
        dir_dict.append({
            'name': file.name,
            'parent': dirname.name,
            'size': size,
            'type': 'file',
        })
        dir_list.append([file.name, dirname.name, size, 'file'])
        dir_size += size
    dir_dict = {dirname.name: {
        'name': dirname.name,
        'parent': dirname.parent.name,
        'size': dir_size,
        'type': 'directory',
        'files': dir_dict}}
    dir_list += [[dirname.name, dirname.parent.name, dir_size, 'directory']]
    return dir_dict, dir_list, dir_size


def recalculate_size(walks, dir_dict, dir_list):
    for dirname, subdirs, filenames in walks[::-1]:
        dirname = Path(dirname)
        if subdirs:
            for dir_ in subdirs:
                dir_dict[dirname.name]['size'] += dir_dict[dir_]['size']
                for line in dir_list:
                    if dirname.name == line[0]:
                        line[2] += dir_dict[dir_]['size']


def create_files(result_directory, dct, lst):
    directory = Path(result_directory)
    if not directory.exists():
        Path.mkdir(directory)
    with (
        open(directory / 'result.json', "w", encoding="utf-8") as j,
        open(directory / 'result.csv', "w", newline='', encoding="utf-8") as c,
        open(directory / 'result.pickle', "wb") as p
    ):
        json.dump(dct, j, ensure_ascii=False)
        pickle.dump(dct, p)
        csv_writer = csv.writer(c)
        csv_writer.writerow(['name', 'parent', 'size', 'type'])
        csv_writer.writerows(lst)


def generate_dict(check_directory, result_directory):
    walks = [d for d in os.walk(check_directory)]
    dir_dict, dir_list = {}, []
    for dirname, subdirs, filenames in walks:
        dirname = Path(dirname)
        ddict, dlist, dsize = calculate_dir(dirname, filenames)
        dir_list += dlist
        dir_dict.update(ddict)
    recalculate_size(walks, dir_dict, dir_list)
    create_files(result_directory, dir_dict, dir_list)