import requests
import bs4
import time
import json
import ImageComposer
import makepdf


def parseCardName(card):
  parsed = card.rstrip("/n").replace(' ', '+')
  return parsed


cards = []
with open('addedCards', 'r') as newCards:
  for card in newCards:
    cardName = parseCardName(card)
    req = requests.get(
        'https://api.scryfall.com/cards/named?exact=' + cardName)
    cardJson = req.json()


    if ['highres_image']:
      if 'card_faces' not in cardJson:
        cards.append(cardJson['image_uris']['large'])
      else:
        for face in cardJson['card_faces']:
          cards.append(face['image_uris']['large'])
    else:
      if 'card_faces' not in cardJson:
         cards.append(cardJson['image_uris']['normal'])
      else:
        for face in cardJson['card_faces']:
          cards.append(face['image_uris']['normal'])
    
  makepdf.makePdf("new cards", ImageComposer.addImages(cards))
 # res = requests.get()


 
