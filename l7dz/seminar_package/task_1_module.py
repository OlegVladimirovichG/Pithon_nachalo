from random import randint, uniform


def fill_file(lines, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(lines):
            f.write(f"{randint(-1000, 1000)}|{uniform(-1000, 1000):.2f}\n")