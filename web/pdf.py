
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
# import libraries
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import json
import sys
import datetime
# python 3
from urllib.request import Request, urlopen
# python 2
import urllib
import xlsxwriter
#import urllib2


def pdf_to_text(input_file, output):
    i_f = open(input_file, 'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
    interpreter = PDFPageInterpreter(resMgr, TxtConverter)
    for page in PDFPage.get_pages(i_f):
        interpreter.process_page(page)

    txt = retData.getvalue()
    print(txt)
    with open(output, 'w', encoding='utf-8') as of:
        of.write(txt)


input_pdf = 'D:\\Dowdload2022\\h1.pdf'
output_txt = 'D:\\Dowdload2022\\h1.txt'
pdf_to_text(input_pdf, output_txt)
