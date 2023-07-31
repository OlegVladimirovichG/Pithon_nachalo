# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        if value <= 0:
            raise ValueError("ОШИБКА!")


class Rectangle:
    a = Range()
    b = Range()

    def __init__(self, a, b=None):
        self.a = a
        self.b = b
        self._shape = 'rectangle'
        if not b:
            self._b = a
            self._shape = 'square'

    @property
    def shape(self):
        return self._shape

    def per(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

r = Rectangle(1, 10)
print(r.per())