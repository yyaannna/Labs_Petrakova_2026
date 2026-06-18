import re
import requests
from collections import Counter

# ---------------- ВВЕДЕННЯ ДАТИ ----------------

date = input("Введіть дату (dd.mm.yyyy): ")

# Формування URL
dd, mm, yyyy = date.split('.')

url = f"http://www.pravda.com.ua/news/date_{dd}{mm}{yyyy}/"

print(f"\nЗавантаження: {url}")

# ---------------- ЗАВАНТАЖЕННЯ HTML ----------------

response = requests.get(url)

if response.status_code != 200:
    print("Помилка завантаження сторінки")
    exit()

html = response.text

# ---------------- ПОШУК ЗАГОЛОВКІВ ----------------

pattern_headers = r'<div class="article_header".*?<a.*?>(.*?)</a>'

headers = re.findall(
    pattern_headers,
    html,
    re.DOTALL
)

print(f"\nЗнайдено заголовків: {len(headers)}")

# ---------------- ПОШУК СЛІВ З ВЕЛИКОЇ ЛІТЕРИ ----------------

words = []

for header in headers:

    # Видалення HTML-тегів
    clean_text = re.sub(r'<.*?>', '', header)

    # Пошук слів з великої літери
    found = re.findall(
        r'\b[А-ЯІЇЄA-Z][а-яіїєА-ЯІЇЄa-zA-Z\-]+\b',
        clean_text
    )

    words.extend(found)

# ---------------- ПІДРАХУНОК ----------------

counter = Counter(words)

print("\nНайчастіші теми / особистості:\n")

for word, count in counter.most_common(20):
    print(f"{word:20} {count}")