#!/usr/bin/env python

import cgitb
cgitb.enable()
import cgi

from pyPdf import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
import StringIO

import sys

name = cgi.FieldStorage()['name'].value

basepdf = PdfFileReader(file("base.pdf", "rb"))

namelayerpacket = StringIO.StringIO()
namelayercanvas = canvas.Canvas(namelayerpacket)
namelayercanvas.setFontSize(25)
namelayercanvas.drawCentredString(396, 330, name)
namelayercanvas.save()
namelayerpacket.seek(0)
namelayerpdf = PdfFileReader(namelayerpacket) 
finalpdf = PdfFileWriter()
basepdf.getPage(0).mergePage(namelayerpdf.getPage(0)) 
finalpdf.addPage(basepdf.getPage(0))

outputpacket = StringIO.StringIO()
finalpdf.write(outputpacket)
outputpacket.seek(0)
print("Content-type: application/pdf")
print("Content-disposition: attachment; filename=certificate.pdf")
print("")
sys.stdout.write(outputpacket.getvalue())
