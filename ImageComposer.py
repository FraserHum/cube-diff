from PIL import Image
import math
import numpy
import requests


pageHeight = 3508
pageWidth = 2480

dpi = 300

cardHeight = int(round(3.5 * dpi))
cardWidth = int(round(2.5 * dpi))

outsideXBorder = 100
outsideYBorder = 700
xBorder = pageWidth - (2 * outsideXBorder) - (3 * cardWidth )
yBorder = pageHeight - (2 * outsideYBorder) - (3 * cardHeight)



def addImages(imgs):
    im = Image.new("RGB", (pageWidth, pageHeight))
    #for i in range(len(imgs)):
    for col in range(3):
        for row in range(3):
            print(imgs[row * 3 + col])
            response = requests.get(imgs[row * 3 + col], stream=True)
            image = Image.open(response.raw)
            image = image.resize((cardWidth, cardHeight))
            im.paste(image, cords(col, row))
    im.save("new-image.jpg", format="JPEG")


def cords(col, row):
 return ((outsideXBorder + (col * cardWidth) + (col * xBorder)),
 (outsideYBorder + (row * cardHeight) + (row * yBorder)))

