# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, 
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_numeric_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)  
            if number.is_integer():
                return int(number)  
            else:
                return number  
        except ValueError:
            print("Ошибка: Введите целое или вещественное число.")
            

number = get_numeric_input("Введите целое или вещественное число: ")
print(f"Вы ввели число: {number}")
