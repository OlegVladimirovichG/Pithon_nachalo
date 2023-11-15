# На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.
import logging
from functools import wraps

logging.basicConfig(filename='task_2.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} {levelname} - {msg}',
                    style='{')
logger = logging.getLogger()


def save_params(func):
    @wraps(func)
    def wrapper(a, b, c):
        func_res = func(a, b, c)
        logger.info(f'{func.__name__}. args: {a = }, {b = }, {c = }. result: {func_res}',)
        return func_res

    return wrapper


@save_params
def square_root_finder(a, b, c):
    """Нахождение корней квадратного уравнения"""
    d = b ** 2 - 4 * a * c
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    return x1, x2

square_root_finder(12, 23, 34)