# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Верните дату в текущем году, соответствующую этому тексту. Логируйте ошибки, если текст не соответсвует формату.
# Логгируйте объект именованного кортежа с атрибутами, соответствующими дате, если дата существует
import logging
from datetime import datetime
from collections import namedtuple

logging.basicConfig(filename='task_3.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} {levelname} - {msg}',
                    style='{')
logger = logging.getLogger()

DAYS = {
    'пон': 0,
    'вто': 1,
    'сре': 2,
    'чет': 3,
    'пят': 4,
    'суб': 5,
    'вос': 6,
}
MONTHS = {
    'янв': 1,
    'фев': 2,
    'мар': 3,
    'апр': 4,
    'май': 5,
    'мая': 5,
    'июн': 6,
    'июл': 7,
    'авг': 8,
    'сен': 9,
    'окт': 10,
    'ноя': 11,
    'дек': 12,
}
Dates = namedtuple('Dates', ['Year', 'Month', 'Day', 'user_text'])


def text_to_date(text):
    try:
        dn, d, m = text.split()
    except ValueError as e:
        logger.exception(e)
    else:
        week_day = DAYS[d[:3]]
        month = MONTHS[m[:3]]
        year = datetime.now().year
        dn = int(dn[:-2])
        counter = 1

        for day in range(1, 32):
            date = datetime(year=year, month=month, day=day)
            if date.weekday() == week_day:
                if counter == dn:
                    date_log = Dates(date.year, date.month, date.day, text)
                    logger.info(f'{date_log = }')
                    return date
                counter += 1


print(text_to_date('5-я суббота июля'))