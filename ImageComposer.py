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

# def ComposeImage():
#     createCanvas()
#     drawLines()
#     drawCards()



def createCanvas():
    im = Image.new("RGB", (pageWidth, pageHeight), color=(255,255,255))
    drawHorizontalLines(im)
    drawVerticleLines(im)
    return im

def addImages(imgs):
    im = createCanvas()
    j = 0
    for i in range(len(imgs)):
        

        if (needNewImage(i)):
            j = j + 1
            im.save("cardSheet-" + str(j)  + ".jpg", format="JPEG")
            im = createCanvas()
        response = requests.get(imgs[i], stream=True)
        col = getCol(i)
        row = getRow(i)
        image = Image.open(response.raw)
        image = image.resize((cardWidth, cardHeight))
        im.paste(image, cords(col,row))

        
    im.save("cardSheet-" + str(j + 1) + ".jpg", format="JPEG")


def cords(col, row):
 return ((outsideXBorder + (col * cardWidth) + (col * xBorder)),
 (outsideYBorder + (row * cardHeight) + (row * yBorder) ))

def drawSquare(im, col, row):
     draw = ImageDraw.Draw(im)
     start = cords(col, row)
     end = (start[0] + cardWidth, start[1] + cardHeight)
     draw.rectangle((start, end), fill=(0,0,0))


def drawLine():
    return

def drawVerticleLines(im):
    for col in range(3):
        x = cords(col, 0)[0] - 3
        draw = ImageDraw.Draw(im)
        draw.line((x, 0, x , pageHeight), width=6, fill=(0,0,0))
        x = x + cardWidth + 5
        draw = ImageDraw.Draw(im)
        draw.line((x, 0, x, pageHeight), width=6, fill=(0,0,0))

def drawHorizontalLines(im):
    for row in range(2):
        y = cords(0, row)[1] - 3
        draw = ImageDraw.Draw(im)
        draw.line((0, y, pageWidth, y), width=6, fill=(0,0,0))
        y = y + cardHeight + 5
        draw = ImageDraw.Draw(im)
        draw.line((0, y, pageWidth, y), width=6, fill=(0,0,0))


# def drawVerticleLeftLine(im, col):
#     x = cords(col, 0)[0] - 3
#     draw = ImageDraw.Draw(im)
#     draw.line((x, 0, x , pageHeight), width=6, fill=(0,0,0))

# def drawVerticleRightLine(im, col):
#     x = cords(col, 0)[0] + cardWidth + 2
#     draw = ImageDraw.Draw(im)
#     draw.line((x, 0, x, pageHeight), width=6, fill=(0,0,0))

# def drawHorizontalTopLine(im, row):
#     y = cords(0, row)[1] - 3
#     draw = ImageDraw.Draw(im)
#     draw.line((0, y, pageWidth, y), width=6, fill=(0,0,0))

# def drawHorizontalBottomLine(im, row):
#     y = cords(0, row)[1] + cardHeight + 2
#     draw = ImageDraw.Draw(im)
#     draw.line((0, y, pageWidth, y), width=6, fill=(0,0,0))

def getCol(i):
    return i % 3

def getRow(i):
   return 1 if ((i % 6) > 2) else 0

def needNewImage(i):
    return ((i > 0) and (i % 6 == 0))