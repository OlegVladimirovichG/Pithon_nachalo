items = {
    "Спальный мешок": 1.2,
    "Тент": 1.8,
    "Палатка": 3.5,
    "Каремат": 0.7,
    "Котелок": 0.9,
    "Термос": 0.5
}

max_weight = 5.0  # Максимальная грузоподъемность рюкзака

backpack_items = []  # Список вещей, которые поместятся в рюкзак
total_weight = 0.0  # Общая масса вещей в рюкзаке

for item, weight in items.items():
    if total_weight + weight <= max_weight:
        backpack_items.append(item)
        total_weight += weight

# Вывод результатов
print("Вещи, которые поместятся в рюкзак:")
for item in backpack_items:
    print(item)
