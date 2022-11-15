import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import re
import json
import numpy

gDataPath = "c:/data/"
#gDataPath = "D:/Dowdload2022/"
gDataFile = "澳肖20221112"
gResultFile = "结果2"
surfix = ".xlsx"
xls = pd.ExcelFile(gDataPath+gDataFile+surfix)

df = pd.read_excel(xls, 1)
df = df.replace(numpy.nan, '', regex=True)
numOfRow = 12
totalRow = numOfRow+1
print(df.columns)
print(df.shape)
total_row = df.shape[0]
total_col = df.shape[1]

item_data = df.iloc[numOfRow, 0]

value1 = item_data
item_data = df.iloc[numOfRow*2+1, 0]

value2 = item_data
value3 = df.iloc[numOfRow*3+2, 0]


data = []
data1 = []


for x in range(total_col):
    data.append([])
for x in range(numOfRow):
    data1.append([])
print(value1, value2, value3, "")
print("done")

values = [value1, value2, value3, "", ""]
data = []
data1 = []
for x in range(total_col):
    data.append([])
for x in range(numOfRow):
    data1.append([])


def readNum1():
    # print("---A----")
    for col in range(0, total_col):
        for i in range(numOfRow):  # row
            # print("------",i,col*3)
            item_data = df.iloc[i, col]
            if (compData(item_data, value1)):
                readNum2(i, col)
            else:
                data1[i].append("")
                #print("1 append",i,len(data1[i]))


def readNum2(row, col):
    # print("---b----",row,col)
    item_data = df.iloc[row+totalRow, col]
    if (compData(item_data, value2)):
        readNum3_1(row, col)
    else:
        data1[row].append("")
        #print("2 append",row,len(data1[row]))


def readNum3_1(row, col):
    item_data = df.iloc[row+totalRow*2, col]
    if (compData(item_data, value3)):
        readNum4_1(row, col)
    else:
        data1[row].append("")
        #print("3 append",row,len(data1[row]))


def readNum3_2(row, col):
    item_data = df.iloc[row+totalRow*2, col]
    if (compData(item_data, value3)):
        readNum4_2(row, col)
    else:
        data1[row].append("")
        #print("3 append",row,len(data1[row]))


def readNum4_1(row, col):
    print("find ----", row, col)

    item_data = df.iloc[row+totalRow*3, col]
    for i in range(4):
        data = df.iloc[row+totalRow*i, col]

        print(data, "-----", values[i])
    print("-----------------------------")

    data1[row].append(item_data)
    #print("5 append",row,len(data1[row]))


def readNum4_2(row, col):
    item_data = df.iloc[row+totalRow*3, col]
    if (compData(item_data, value4)):
        readNum5(row, col)
    else:
        data1[row].append("")
        #print("4 append",row,len(data1[row]))


def readNum5(row, col):
    print("find ----", row, col)

    item_data = df.iloc[row+totalRow*4, col]
    for i in range(5):
        data = df.iloc[row+totalRow*i, col]

        print(data, "-----", values[i])
    print("-----------------------------")

    data1[row].append(item_data)
    #print("5 append",row,len(data1[row]))


def readNum3(row, col):
    print("find ----", row, col)
    item_data = df.iloc[row, col]
    item_data1 = df.iloc[row+totalRow, col]
    item_data2 = df.iloc[row+totalRow*2, col]
    print(item_data)
    print("-----------------------------")
    print(item_data1)
    print("-----------------------------")
    print(item_data2)

    print("=============================")
    data1[row].append(item_data)


def compData(item_data, value):
    if (item_data is None):
        return False
    if (len(str(item_data)) == 0):
        return False
    # print(item_data)
    lt = item_data.split(',')
    res = lt[6:]

    for item in res:
        #print("cell data= " , item)
        item = item.replace(']', '')
        ss = item.split('[')
        if (ss[0] == value):
            return True
    return False


readNum1()

print(len(data1))
print(len(data1[0]))


writer = pd.ExcelWriter(gDataPath+gResultFile+surfix, engine='xlsxwriter')
header = []
for x in range(len(data1[0])):
    header.append("col" + str(x))

df123 = pd.DataFrame(data1)

df123.to_excel(writer, sheet_name="result")
writer.close()
xls.close()
