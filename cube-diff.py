# get current list
# get new list
# diff lists
# show new cards
# show replaced cards

import requests
import sys
import bs4


res = requests.get(
    'https://magic.wizards.com/en/articles/archive/vintage-cube-cardlist')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

newCards = soup.select('table')[1].select('a')

newCardsList = []
for card in newCards:
    newCardsList.append(card.string.rstrip('\n'))

addedCards = []
removedCards = []


with open('cubeList', 'r') as oldCards:
    oldCardsList = []
    for line in oldCards:
        oldCardsList.append(line.rstrip('\n'))

    for newCard in newCardsList:
        if newCard.rstrip('\n') not in oldCardsList:
            addedCards.append(newCard.rstrip('\n'))

    for oldCard in oldCardsList:
        if oldCard.rstrip('\n') not in newCardsList:
            removedCards.append(oldCard.rstrip('\n'))

with open('addedCards', 'w') as f:
    for card in addedCards:
        f.write(card + '\n')

with open('removedCards', 'w') as f:
    for card in removedCards:
        f.write(card + '\n')

print("added cards: ")
print("\n".join(addedCards))
print("removed Cards: ")
print("\n".join(removedCards))
print("added: " + str(len(addedCards)) + " removed:" + str(len(removedCards)))
#f.write(card.string+ '\n')

proceed = input("do you want to update your cube file? y/n: ")

print(newCards[1])
if proceed == 'n':
    exit()
else:
    with open('cubeList', 'w') as cubeList:
        for card in newCards:
            cubeList.write(card.string + '\n')
