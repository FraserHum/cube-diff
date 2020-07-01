from PIL import Image, ImageDraw
import math
import numpy
import requests
import random


pageHeight = 2480
pageWidth = 3508

dpi = 300

cardHeight = int(round(3.5 * dpi))
cardWidth = int(round(2.5 * dpi))

outsideXBorder = 250
outsideYBorder = 150
xBorder = int((pageWidth - (2 * outsideXBorder) - (3 * cardWidth )) / 2)
yBorder = int((pageHeight - (2 * outsideYBorder) - (2 * cardHeight)) / 1)
print(xBorder)
print(yBorder)



def addImages(imgs):
    im = Image.new("RGB", (pageWidth, pageHeight), color=(255,255,255))
    
    
    #for i in range(len(imgs)):
    for col in range(3):
        drawVerticleLeftLine(im, col)
        drawVerticleRightLine(im, col)
        for row in range(2):
            drawHorizontalTopLine(im, row)
            drawHorizontalBottomLine(im, row)
            
            print(imgs[row * 3 + col])
            response = requests.get(imgs[row * 3 + col], stream=True)
            image = Image.open(response.raw)
            image = image.resize((cardWidth, cardHeight))
            im.paste(image, cords(col, row))
    im.save("new-image.jpg", format="JPEG")


def cords(col, row):
 return ((outsideXBorder + (col * cardWidth) + (col * xBorder)),
 (outsideYBorder + (row * cardHeight) + (row * yBorder) ))

def drawSquare(im, col, row):
     draw = ImageDraw.Draw(im)
     start = cords(col, row)
     end = (start[0] + cardWidth, start[1] + cardHeight)
     draw.rectangle((start, end), fill=(0,0,0))




def drawVerticleLeftLine(im, col):
    x = cords(col, 0)[0] - 3
    draw = ImageDraw.Draw(im)
    draw.line((x, 0, x , pageHeight), width=6, fill=(0,0,0))

def drawVerticleRightLine(im, col):
    x = cords(col, 0)[0] + cardWidth + 2
    draw = ImageDraw.Draw(im)
    draw.line((x, 0, x, pageHeight), width=6, fill=(0,0,0))

def drawHorizontalTopLine(im, row):
    y = cords(0, row)[1] - 3
    draw = ImageDraw.Draw(im)
    draw.line((0, y, pageWidth, y), width=6, fill=(0,0,0))

def drawHorizontalBottomLine(im, row):
    y = cords(0, row)[1] + cardHeight + 2
    draw = ImageDraw.Draw(im)
    draw.line((0, y, pageWidth, y), width=6, fill=(0,0,0))