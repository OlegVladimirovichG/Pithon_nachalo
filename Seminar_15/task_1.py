# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
import logging

logging.basicConfig(filename='task_1.log',
                    encoding='utf-8',
                    level=logging.ERROR)
logger = logging.getLogger()


def dev_by_zero(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error('Деление на ноль!')
        return float('inf') if a > 0 else float('-inf')


print(dev_by_zero(-2, 0))