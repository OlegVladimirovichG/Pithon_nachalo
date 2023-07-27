from time import time


class MyString(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()

        return instance


a = MyString('Строка', 'Автор')
# print(f'Строка: {a}, Автор: {a.author}, Время: {a.time}')
print(a)