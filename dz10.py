def process_variables():
    # Создаем несколько переменных
    variable1s = [3, 'f', 'ee', 3.14159265]
    variable2s = 'Banana'
    variable3 = 'Seven'
    variable4 = 'Геодезия - это наука о методах определения фигуры и размеров Земли, изображения земной поверхности на планах и картах, и точных измерений на местности, связанных с решением различных научных и практических задач.'
    variable5s = 23123132
    variable6s = 3.14159265

    # Получаем список всех переменных в текущей области видимости
    variables = list(locals().items())

    # Создаем новый словарь для сохранения обновленных переменных
    updated_variables = {}

    # Обходим все переменные и заменяем содержимое оканчивающихся на 's' переменных на None
    for name, value in variables:
        if name != 's' and name.endswith('s'):
            updated_variables[name] = None
        else:
            updated_variables[name.rstrip('s')] = value

    # Возвращаем обновленные переменные
    return updated_variables


# Тестируем функцию
result = process_variables()

# Выводим значения переменных
print("Переменная variable1:", result.get('variable1'))
print("Переменная variable2:", result.get('variable2'))
print("Переменная variable3:", result.get('variable3'))
print("Переменная variable4:", result.get('variable4'))
print("Переменная variable5:", result.get('variable5'))
print("Переменная variable6:", result.get('variable6'))
