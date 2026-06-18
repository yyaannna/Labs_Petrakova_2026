import re
import requests
from collections import Counter
from html.parser import HTMLParser



class PravdaParser(HTMLParser):

    def __init__(self):
        super().__init__()

        self.in_article = False
        self.in_link = False

        self.headers = []

    def handle_starttag(self, tag, attrs):

        attrs = dict(attrs)

        if tag == "div" and attrs.get("class") == "article_header":
            self.in_article = True

        elif self.in_article and tag == "a":
            self.in_link = True

    def handle_data(self, data):

        if self.in_article and self.in_link:
            text = data.strip()

            if text:
                self.headers.append(text)

    def handle_endtag(self, tag):

        if tag == "a":
            self.in_link = False

        elif tag == "div":
            self.in_article = False



date = input("Введіть дату (dd.mm.yyyy): ")

dd, mm, yyyy = date.split('.')

url = f"http://www.pravda.com.ua/news/date_{dd}{mm}{yyyy}/"

print(f"\nЗавантаження: {url}")


response = requests.get(url)

if response.status_code != 200:
    print("Помилка завантаження сторінки")
    exit()

html = response.text


parser = PravdaParser()

parser.feed(html)

headers = parser.headers

print(f"\nЗнайдено заголовків: {len(headers)}")


words = []

for header in headers:

    found = re.findall(
        r'\b[А-ЯІЇЄA-Z][а-яіїєА-ЯІЇЄa-zA-Z\-]+\b',
        header
    )

    words.extend(found)


counter = Counter(words)

print("\nНайчастіші теми / особистості:\n")

for word, count in counter.most_common(20):
    print(f"{word:20} {count}")