def fibonacci_generator():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()

for i in range(int(input('Введите число: '))):
    print(next(fib_gen))
