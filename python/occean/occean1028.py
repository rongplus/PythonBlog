import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import re
import json

gDataPath = "c:/data/"
#gDataPath = "D:/Dowdload2022/"
gDataFile = "3组数据匹配20221028"
gResultFile = "结果"
surfix = ".xlsx"
xls = pd.ExcelFile(gDataPath+gDataFile+surfix)

df = pd.read_excel(xls, 0)

print(df.columns)
print(df.shape)
total_row = df.shape[0]
total_col = df.shape[1]

item_data = df.iloc[49, 0]
print(item_data)
value1 = int(item_data)
item_data = df.iloc[99, 0]
print(item_data)
value2 = int(item_data)


data = []
data1 = []
for x in range(int(total_col/3)):
    data.append([])
for x in range(50):
    data1.append([])


def read(row, col):
    print("read")


def readA():
    # print("---A----")
    for col in range(0, int(total_col/3)):
        for i in range(49):  # row
            # print("------",i,col*3)
            item_data = df.iloc[i, col*3]
            if (compData(item_data, value1)):
                readB(i+50, col*3+1)
            else:
                data1[i].append("")


def readB(row, col):
    # print("---b----",row,col)
    item_data = df.iloc[row, col]
    if (compData(item_data, value2)):
        readC(row+50, col+1)
    else:
        data1[row-50].append("")


def readC(row, col):
    print("find ", row-100, col-2, row-50, col-1, row, col)
    item_data1 = df.iloc[row-100, col-2]
    item_data2 = df.iloc[row-50, col-1]
    item_data = df.iloc[row, col]
    print(item_data1)
    print("-----------------------------")
    print(item_data2)
    print("-----------------------------")
    print(item_data)
    print("=============================")
    data1[row-100].append(item_data)


def compData(item_data, value):
    if (item_data is None):
        return False
    if (len(str(item_data)) == 0):
        return False
    # print(item_data)
    lt = item_data.split(',')
    res = lt[::-1]
    pre = -1
    index = 0
    for item in res:
        if (index == 12):
            break
        #print("cell data= " , item)
        item = item.replace(']', '')
        ss = item.split('[')

        if (pre != int(ss[1])):
            pre = int(ss[1])
            index += 1
        if (int(ss[0]) == value):
            return True
    return False


readA()


print(len(data1))
print(len(data1[0]))

writer = pd.ExcelWriter(gDataPath+gResultFile+surfix, engine='xlsxwriter')
header = []
for x in range(20):
    header.append("col" + str(x))

df123 = pd.DataFrame(data1)

df123.to_excel(writer, sheet_name="result")
writer.close()
xls.close()
