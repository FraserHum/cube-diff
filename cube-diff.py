#get current list
#get new list
#diff lists
#show new cards
#show replaced cards

import requests,sys,bs4


res = requests.get('https://magic.wizards.com/en/articles/archive/vintage-cube-cardlist')
type(res)

print(res.status_code == requests.codes.ok)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

cards = soup.select('table')

print(cards)

