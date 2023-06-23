# Запрос целого числа у пользователя
number = int(input("Введите целое число: "))

# Преобразование в шестнадцатеричное представление
hex_representation = hex(number)[2:].upper()

# Вывод результата
print("Шестнадцатеричное представление:", hex_representation)

# Проверка результата с помощью функции hex
hex_check = hex(number)[2:].upper()
print("Проверка с использованием hex:", hex_check)