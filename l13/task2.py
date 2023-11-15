# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get_from_dict(dictionary, key, default_value=None):
    try:
        return dictionary[key]
    except KeyError:
        return default_value


my_dict = {"name": "John", 
           "age": 30, 
           "city": "New York"}

name = get_from_dict(my_dict, "name", "Unknown")
print(f"Name: {name}")

occupation = get_from_dict(my_dict, "occupation", "Unemployed")
print(f"Occupation: {occupation}")