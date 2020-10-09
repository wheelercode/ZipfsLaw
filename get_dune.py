import re
from bs4 import BeautifulSoup
import requests

url = 'https://novels80.com/241224-dune.html#list-chapter'
text = requests.get(url).text
soup = BeautifulSoup(text, 'html.parser')
P = re.compile(r'^(\/dune\/.*)')
link = 'https://novels80.com/'
links = []
for a in soup.find_all('a'):
    href = a['href']
    if href:
        m = P.match(href)
        if m:
            links.append('{}{}'.format(link, href))

dune = ''
for link in links:
    soup = BeautifulSoup(requests.get(link).text, 'html.parser')
    div = soup.find('div', {'class': 'chapter-content'})
    if div:
        dune += div.text
    else:
        print(link)
with open('dune.txt', 'a+') as outfile:
    outfile.write(dune)