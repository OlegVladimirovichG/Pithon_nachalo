# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.
from Classes import module_2

c = module_2.Archive(42, "Data")
# print(c)
print(f'{c.num = }, {c.value = }, {c.archive = }')
d = module_2.Archive(55, "Data2")
print(f'{c.num = }, {c.value = }, {c.archive = }')
print(f'{d.num = }, {d.value = }, {d.archive = }')
# help(c)
e = module_2.Archive(22, "Data3")
print(f'{e.num = }, {e.value = }, {e.archive = }')

print(f"{e = }")