from bs4 import BeautifulSoup
import requests
import re

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_="main-article")

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

def sanitize_filename(title):
    return re.sub(r'[^\w\s-]', '', title)

for link in links:
    result = requests.get(f'{root}{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_="main-article")
    title = box.find('h1').get_text()
    transcript = box.find('div', class_="full-script").get_text(strip=True, separator=' ')

    sanitize_title = sanitize_filename(title)

    with open(f'{sanitize_title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)
    