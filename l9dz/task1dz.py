import csv
import json
import math
import random

def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            data = {
                'parameters': {
                    'args': args,
                    'kwargs': kwargs
                },
                'result': result
            }

            with open(filename, 'w') as file:
                json.dump(data, file)

            return result

        return wrapper

    return decorator

@save_to_json('function_result.json')
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Number 1', 'Number 2', 'Number 3'])

        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

# Пример использования
filename = 'random_numbers.csv'
num_rows = random.randint(100, 1000)

generate_csv(filename, num_rows)
print(f"CSV файл '{filename}' сгенерирован с {num_rows} строками.\n")

@save_to_json('equation_results.json')
def process_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        results = []
        for row in reader:
            a, b, c = map(int, row)
            result = solve_quadratic_equation(a, b, c)
            results.append({'a': a, 'b': b, 'c': c, 'roots': result})

        return results

equation_results = process_csv(filename)
print(f"Результаты уравнений сохранены в JSON файле 'equation_results.json'.")
