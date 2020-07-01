import requests
import bs4
import time
import json


def parseCardName(card):
  parsed = card.rstrip("/n").replace(' ', '+')
  return parsed


cards = []
with open('addedCards', 'r') as newCards:
  for card in newCards:
    cardName = parseCardName(card)
    req = requests.get(
        'https://api.scryfall.com/cards/named?exact=' + cardName)
    js = req.json()

    if ['highres_image']:
      if 'card_faces' not in js:
        cards.append(js['image_uris']['large'])
      else:
        for face in js['card_faces']:
          cards.append(face['image_uris']['large'])
    else:
      if 'card_faces' not in js:
         cards.append(js['image_uris']['normal'])
      else:
        for face in js['card_faces']:
          cards.append(face['image_uris']['normal'])
    time.sleep(0.1)
    
  print(cards)
 # res = requests.get()


 
