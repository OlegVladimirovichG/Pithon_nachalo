# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, start, stop=None, step=None):
        self.stop = stop if stop else start
        self.start = start if stop else stop
        self.step = step or 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop + 1:
            factorial = self._factorial(self.start)
            self.start += self.step
            return factorial
        raise StopIteration

    def _factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self._factorial(n - 1)


f = Factorial(2, 5, 2)
for _ in range(5):
    print(next(f))