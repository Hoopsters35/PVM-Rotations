import requests, bs4, re

page = requests.get("http://runescape.wikia.com/wiki/Araxxor")

soup = bs4.BeautifulSoup(page.text, 'html5lib')

table = soup.select('td.status-active')[0].parent()

for index, elem in enumerate(table):
    print(f'Path {index + 1}: {elem.text}')

print(soup.find(text=re.compile(r'Days until next rotation: \d')))