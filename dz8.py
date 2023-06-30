import re
import requests
from collections import Counter

# Получение текста из ссылки
response = requests.get("https://ru.wikipedia.org/wiki/Python")
text = response.text

# Удаление тегов HTML и знаков препинания, приведение к нижнему регистру
clean_text = re.sub(r'<.*?>', '', text)
clean_text = re.sub(r'[^\w\s]', '', clean_text.lower())

# Разделение текста на слова
words = clean_text.split()

# Подсчет количества встречаемости каждого слова
word_counts = Counter(words)

# Получение 10 самых часто встречающихся слов
top_10_words = word_counts.most_common(10)

# Вывод результатов
for word, count in top_10_words:
    print(f"Слово: {word}, Количество: {count}")
