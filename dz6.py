from collections import Counter

friends_items = {
    "Вова": ("Рюкзак", "Палатка", "Спальный мешок"),
    "Олег": ("Рюкзак", "Котелок", "Термос"),
    "Стас": ("Рюкзак", "Карта", "Фонарик", "Удочка", "Спальный мешок"),
    "Денис": ("Лодка", "Мотор", "Спальный мешок", "Каша")
}

# Вопрос 1: Какие вещи взяли все три друга
common_items = set.intersection(*[set(items) for items in friends_items.values()])

print("Вещи, взятые всеми тремя друзьями:")
for item in common_items:
    print(item)

# Вопрос 2: Какие вещи уникальны, есть только у одного друга и имя этого друга
all_items = [item for items in friends_items.values() for item in items]
item_counts = Counter(all_items)
unique_items = {item for item, count in item_counts.items() if count == 1}
unique_friend = {item: [] for item in unique_items}

for friend, items in friends_items.items():
    for item in items:
        if item in unique_items:
            unique_friend[item].append(friend)

print("\nУникальные вещи и имена друзей:")
for item, friends in unique_friend.items():
    print(f"Вещь: {item}, Имена друзей: {', '.join(friends)}")

# Вопрос 3: Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
missing_friend = {}

for item in common_items:
    friends_without_item = [friend for friend, items in friends_items.items() if item not in items]
    if len(friends_without_item) == len(friends_items) - 1:
        missing_friend[item] = friends_without_item[0]

print("\nВещи, присутствующие у всех друзей кроме одного:")
for item, friend in missing_friend.items():
    print(f"Вещь: {item}, Имя друга: {friend}")
