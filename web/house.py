# import libraries
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from bs4 import SoupStrainer as strainer
import json
import sys
import datetime
# python 3
from urllib.request import Request, urlopen
# python 2
import urllib
import xlsxwriter
#import urllib2
from lxml import etree


def findInTabular1(tabular):
    global index
    lt = tabular.find_all('span', attrs="formitem formfield")
    print("----in tabular =", len(lt))
    data_list = []
    for span in lt:
        # print(span.text,"---")
        data_list.append(span.text)
    # writeToExel(index,data_list)
    index += 1


def findInPart(part):
    lt = part.find_all('div', attrs={'class': 'formitem formgroup tabular'})
    if (len(lt) == 0):
        print("find Error--------------", index)
        return

    print("----formitem formgroup tabular =", len(lt))
    findInTabular1(lt[0])


def work():

    url = 'C:\\Users\\huang\\Downloads\\a.htm'
    data = open(url,).read()
    print("file length= ", len(data))

    dom = etree.HTML(data)

    print("dom=", len(dom[0]))
    for d in dom[0]:
        print(d.tag)
    print("dom=", len(dom[1]))
    for d in dom[1]:
        print(d.tag)
    #divs = etree.SubElement(dom[1], "div")
    # print(dom[1].get("div"))
    #print("divs=", len(divs))
    #build_text_list = dom[1].XPath("//div")
    #print("divs=", len(build_text_list))
    total = 0
    for element in dom[1].iter("div"):
        # print(element.text)
        total += 1
    print("total= ", total)

    return
    print(etree.tostring(dom[0]))
    print(dom[0].tag)
    lt = dom.xpath("//div")
    print(len(lt))

    lt = dom.xpath("//body")
    lt = dom.xpath("//div[@class='link-item status-sld hasheader']")

    index = 0
    only_item_cells = strainer(
        "div", attrs={"class": "formitem formgroup tabular"})
    print(len(lt))
    for ii in lt:
        print("----index----", index)
        with open('readme' + str(index)+'.txt', 'w', encoding="utf-8") as f:
            aa = str(etree.tostring(ii))
            f.write(aa)

        #soup = BeautifulSoup(etree.tostring(ii), 'html.parser',parse_only=only_item_cells)

        # print(soup)
        # findInPart(soup)

        print("end ----index----", index)
        index += 1


work()
