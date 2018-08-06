import requests, bs4, re

def days_until_switch_message(days):
    day = ''
    if days == 1:
        day = 'tonight'
    elif days == 2:
        day = 'tomorrow night'
    else:
        day = f'in {days} days'
    return f'Next rotation begins {day}'

page = requests.get("http://runescape.wikia.com/wiki/Araxxor")

soup = bs4.BeautifulSoup(page.text, 'html5lib')

table = soup.select('td.status-active')[0].parent()

for index, elem in enumerate(table):
    print(f'Path {index + 1}: {elem.text}')

days_until_switch = soup.find(text=re.compile(r'Days until next rotation: \d')).split()[-1]
print(days_until_switch_message(int(days_until_switch)))