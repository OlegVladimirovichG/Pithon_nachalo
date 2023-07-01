def guess_riddle(riddle, options, num_attempts):
    for attempt in range(1, num_attempts + 1):
        guess = input(f"Попытка #{attempt}: Введите ваш ответ: ")

        if guess in options:
            print("Поздравляю! Вы отгадали загадку.")
            return attempt

        print("Неправильный ответ.")

    print("Количество попыток исчерпано.")
    return 0
