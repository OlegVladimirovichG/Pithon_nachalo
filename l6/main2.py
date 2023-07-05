from riddle_game import guess_riddle

riddle = "Какое слово начинается на 'э', заканчивается на 'а', а в середине имеет букву 'л'?"
options = ["электрокарта", "электростанция", "электролампа"]
num_attempts = 4

result = guess_riddle(riddle, options, num_attempts)

if result > 0:
    print(f"Загадка отгадана с попытки номер {result}.")
else:
    print("Загадку не удалось отгадать.")
