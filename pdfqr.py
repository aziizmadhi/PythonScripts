import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
#from reportlab.pdfgen import canvas ----=====------======----==---==-----=-
import qrcode

from fpdf import FPDF

from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab_qrcode import QRCodeImage


merger = PdfFileMerger()

inputfile = 'testIN.pdf'

QRcode = 'QRcode.pdf'

outputfile = 'output.pdf'   #<< where the output will be saved 

docFile = 'SBP.docx'

pprT = 'identicon.png'

"""Gives me the number of pages"""

with open(inputfile, "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    size = pdf_reader.numPages
    print(size)

"""PaperTowns pdf conversion"""

pdf = FPDF()
# imagelist is the list with all image filenames
pdf.add_page()
pdf.image(pprT,0,0,1,1)
pdf.output("identicon.pdf", "F")
pprtown = "identicon.pdf"

"""Create QRcode and place it (x , y)"""

doc = Canvas('QRcode.pdf')
qr = QRCodeImage('https://www.acs.com.sa/' ,
    size=30 * mm,
    fill_color='black',
    back_color= None,
    border=4,
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)
qr.drawOn(doc, 20, 40) # x (left,right) y (up,down)

# qr.drawOn(doc, 20, 735) << Top Left

# qr.drawOn(doc, 500, 735)<< Top Right

# qr.drawOn(doc, 500, 40) << Bottom right 

# qr.drawOn(doc, 20, 40) << Bottom left 


doc.showPage()
doc.save()

"""Merges QR.pdf with input PDF"""

with open(inputfile, 'rb') as k:
    pdf = PyPDF2.PdfFileReader(k)

    with open(pprtown, 'rb') as pprtownS:
        pprtownS = PyPDF2.PdfFileReader(pprtown)

        with open(QRcode, 'rb') as QRcodefile:
            QRcodePdf = PyPDF2.PdfFileReader(QRcodefile)

            p = pdf.getPage(0)

            w = QRcodePdf.getPage(0)

            t = pprtownS.getPage(0)

            p.mergePage(w)
            p.mergePage(t)

            pdfwriter = PyPDF2.PdfFileWriter()

            pdfwriter.addPage(p)
    #        for page in range(1, size):
    #            p = pdf.getPage(page)
    #            pdfwriter.addPage(p)
    #        output = PdfFileWriter()

            with open(outputfile, 'wb') as outputfileF:
                pdfwriter.write(outputfileF)