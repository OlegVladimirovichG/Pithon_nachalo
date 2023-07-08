import os
from pathlib import Path
from random import randint, choice, randbytes

VOWELS = 'aeiouy'
ALL = 'abcdefghijklmnopqrstuvwxyz'
GROUPS = {
    Path('binary'): ['bin', 'dll'],
    Path('image'): ['jpg', 'png', 'jpeg'],
    Path('text'): ['pdf', 'doc', 'txt'],
}


def create_file(path, ext, name):
    save_path = path
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    with open(f"{save_path}/{name}.{ext}", "wb") as f:
        f.write(randbytes(255))


def generate_name(min_=6, max_=30):
    while True:
        name_length = randint(min_, max_)
        res = ''
        for _ in range(name_length):
            res = res + choice(ALL)
        if any(c in res for c in VOWELS):
            return res.capitalize()


def create(path, min_name=6, max_name=30, **kwargs):
    if not os.path.exists(path):
        os.makedirs(path)
    for k, v in kwargs.items():
        for _ in range(v):
            create_file(path, k, generate_name(min_name, max_name))

def group_files(path):
    p = Path(path)
    for f in p.iterdir():
        for k, v in GROUPS.items():
            if f.suffix[1:] in v:
                save_path = Path(p / k)
                break
        else:
            save_path = Path(p / "misc")
        if not Path.exists(save_path):
            Path.mkdir(save_path)
        f.replace(save_path / f.name)