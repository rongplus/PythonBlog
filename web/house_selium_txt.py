import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import win32con
import time
from win32clipboard import GetClipboardData, OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData

# 读取剪贴板的数据


def get_clipboard():
    OpenClipboard()
    d = GetClipboardData(win32con.CF_TEXT)
    CloseClipboard()
    # print(d.decode("GBK"))
    return d.decode('GBK')

# 写入剪贴板数据


def set_clipboard(astr):
    OpenClipboard()
    EmptyClipboard()
    # 可以sleep一下，防止操作过快报错
    # time.sleep(1)
    SetClipboardData(win32con.CF_UNICODETEXT, astr)
    CloseClipboard()


def openWeb(url, fName):
    driver = webdriver.Chrome()
    driver.get(url)
    # get total
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    lt = soup.find_all(
        'div', attrs={'class': 'link-item status-sld hasheader'})
    print("----link-item status-sld hasheader =", len(lt))

    total = len(lt)
    for i in range(total):
        driver.execute_script(f"window.scrollTo(0, {i*1200});")
        time.sleep(3)
        # driver.execute_script(script)

    a = ActionChains(driver)
    a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
    a.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
    # save web
    txt = get_clipboard()
    with open(fName, 'w', encoding='utf-8') as of:
        of.write(txt)

    work_txt(fName)


def writeToExel(row, data_list):
    for col_num, data in enumerate(data_list):
        worksheet.write(row, col_num, data)


def addAddress(lt, txt):
    #Inof("address", txt)
    print("address", txt)
    lt.append(txt)


def addPrice(lt, txt):
    Inof("Price", txt)
    # Sold:$750,000List:$779,900Burlington Mountainside Halton
    txt = txt.replace(",", "")
    Inof("Price again ", txt)
    num = re.findall(r'\d+', txt)
    lt.append(num[0])
    lt.append(num[1])
    #ss = txt.split("$")


def addListDate(lt, txt):
    Inof("ListDate", txt)
    # Contract Date:8/22/2022
    ss = txt.split(":")
    lt.append(ss[1])


def addSoldDate(lt, txt):
    Inof("SoldDate", txt)
    # Sold Date:10/18/2022
    ss = txt.split(":")
    lt.append(ss[1])


def addDOM(lt, txt):
    Inof("DOM", txt)
    ss = txt.split(":")
    lt.append(ss[1])


def addLot(lt, txt):
    Inof("LOT", txt)
    lt.append(txt)


def addBedRoom(lt, txt):
    Inof("BedRoom", txt)
    ss = txt.split(":")
    lt.append(ss[1])


def addWashRoom(lt, txt):
    Inof("WashRoom", txt)
    ss = txt.split(":")
    lt.append(ss[1])


def addMLS(lt, txt):
    Inof("MLS", txt)
    ss = txt.split(":")
    lt.append(ss[1])


def addBasement(lt, txt):
    Inof("BaseMent", txt)
    ss = txt.split(":")
    lt.append(ss[1])


def addAge(lt, txt):
    Inof("age", txt)
    ss = txt.split(":")
    lt.append(ss[1])


def addSquare(lt, txt):
    print("square", txt)
    ss = txt.split(":")
    lt.append(ss[1])


def Inof(ll, txt):
    # print(ll,txt)
    i = 0


def dump(lt):
    ii = 0
    #print("---------One data-------")
    for line in lt:
        # print(ii,line)
        ii += 1
    writeToExel(total, lt)


total = 0


def work_txt(fname):
    global index
    global total
    with open(fname, 'r', encoding='utf-8') as of:
        index = -1
        data = []
        hd = ["地址", "叫价", "售价", "上市", "成交", "在市时长",
              "占地", "卧室", "洗手间", "ID", "地下室", "房龄"]
        dump(hd)
        st = False
        while True:
            line = of.readline()
            if not line:
                break
            txt = line.strip()
            # if (txt=='Links:Virtual TourActions:Print'):
            if (txt.startswith("image1 of")):
                # print(total,"-----",line.strip())
                index = -1
                total += 1
                data = []

                st = True
                line = of.readline()
                txt = line.strip()
                if (len(txt) == 0):
                    line = of.readline()
                    txt = line.strip()
                addAddress(data, txt)

            elif (txt == '1660 North Service Rd E #103, Oakville, ON L6H7G3905-281-2888'):
                # print(index,"-----",line.strip())
                index = 0
                # write to execl
                dump(data)
                # writeToExel(index,data)
                st = False
                # return
            elif (st):
                # add to list;
                index += 1

                # if (index == 0):
                # print("Address:",txt)
                #    addAddress(data, txt)
                if (txt.startswith("Sold:")):
                    addPrice(data, txt)
                elif (txt.startswith("Contract Date:")):
                    addListDate(data, txt)
                elif (txt.startswith("Sold Date:")):
                    addSoldDate(data, txt)
                elif (txt.startswith("DOM:")):
                    addDOM(data, txt)
                elif (txt.startswith("Acreage:")):
                    line = of.readline()
                    addLot(data, line)
                elif (txt.startswith("Bedrooms:")):
                    addBedRoom(data, txt)
                elif (txt.startswith("Washrooms:")):
                    addWashRoom(data, txt)
                elif (txt.startswith("MLS#")):
                    addMLS(data, txt)
                elif (txt.startswith("Basement:")):
                    addBasement(data, txt)
                elif (txt.startswith("Apx Age:")):
                    addAge(data, txt)

                # data.append(txt)


gDataPath = "D:/Dowdload2022/"
month = "11"
workbook = xlsxwriter.Workbook(gDataPath+'month' + month + '.xlsx')
worksheet = workbook.add_worksheet()
index = 0
total = 0
url = "http://v3.torontomls.net/Live/Pages/Public/Link.aspx?Key=c107db39240c488e8190108f61362417&App=TREB"
ff = gDataPath+'month' + month + '.txt'
openWeb(url, ff)

workbook.close()
