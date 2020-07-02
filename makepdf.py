from fpdf import FPDF
from PIL import Image

def makePdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(listPages[0])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])
    print(listPages)

    for page in listPages:
        pdf.add_page()
        pdf.image(page, 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")


