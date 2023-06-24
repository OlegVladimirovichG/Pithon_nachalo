from fractions import Fraction

# Запрос двух дробей у пользователя
fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

# Разделение числителя и знаменателя для первой дроби
numerator1, denominator1 = map(int, fraction1.split('/'))

# Разделение числителя и знаменателя для второй дроби
numerator2, denominator2 = map(int, fraction2.split('/'))

# Создание объектов Fraction для обеих дробей
frac1 = Fraction(numerator1, denominator1)
frac2 = Fraction(numerator2, denominator2)

# Вычисление суммы и произведения дробей
sum_fraction = frac1 + frac2
product_fraction = frac1 * frac2

# Вывод результата
print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", product_fraction)

# Проверка результата с помощью модуля fractions
sum_check = Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2)
product_check = Fraction(numerator1, denominator1) * Fraction(numerator2, denominator2)

print("Проверка с использованием fractions (сумма):", sum_check)
print("Проверка с использованием fractions (произведение):", product_check)
