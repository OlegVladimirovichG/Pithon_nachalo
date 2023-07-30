# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)


import time

class MyString(str):
    def __new__(cls, value, author):
        instance = super(MyString, cls).__new__(cls, value)
        instance.author = author
        instance.created_at = time.time()
        return instance

# Example usage
author_name = "John"
text = "Hello, I'm a custom string."

my_string = MyString(text, author_name)
print(my_string)  # Output: Hello, I'm a custom string.
print(my_string.upper())  # Output: HELLO, I'M A CUSTOM STRING.
print(my_string.author)  # Output: John
print(my_string.created_at)  # Output: <current timestamp>
