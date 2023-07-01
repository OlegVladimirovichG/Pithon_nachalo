import random

def guess_number(lower_bound, upper_bound, num_attempts):
    secret_number = random.randint(lower_bound, upper_bound)

    for attempt in range(num_attempts):
        guess = int(input("Угадайте число: "))

        if guess == secret_number:
            print("Поздравляю! Вы угадали число!")
            return True
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    print("Количество попыток исчерпано. Загаданное число было:", secret_number)
    return False