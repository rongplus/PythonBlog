import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import re
import json

gDataPath = ""
#gDataPath = "D:/Dowdload2022/"
gDataFile = "20230103更新"
gResultFile = "结果"
surfix = ".xlsx"
xls = pd.ExcelFile(gDataPath+gDataFile+surfix)


data1 = []
for x in range(12):
    data1.append([])

df1 = pd.read_excel(xls, 1)

data2 = []

for x in range(10):
    data2.append([])

df2 = pd.read_excel(xls, 0)

print(df1.columns)
print(df1.shape)
total_row = df1.shape[0]
total_col = df1.shape[1]

item_data = df1.iloc[12, 0]
print(item_data)
value1 = item_data


def compDataXiao(item_data, value):
    if (item_data is None):
        return False
    if (len(str(item_data)) == 0):
        return False
    # print(item_data)
    lt = item_data.split(',')
    #res = lt[-6:]
    res = lt[::-1]
    pre = -1
    index = 0

    for item in res:
        if (index == 6):
            break
        #print("cell data= " , item)
        item = item.replace(']', '')
        ss = item.split('[')
        if (pre != int(ss[1])):
            pre = int(ss[1])
            index += 1

        if (ss[0] == value):
            return True
    return False


def readXiao():
    # print("---A----")
    for col in range(0, total_col):
        for i in range(12):  # row
            # print("------",i,col*3)
            item_data = df1.iloc[i, col]
            if (compDataXiao(item_data, value1)):
                #readB(i+13, col)
                row = i+13
                print("---b----", row, col)
                item_data = df1.iloc[row, col]
                data1[row-13].append(item_data)


print(df2.columns)
print(df2.shape)
total_row = df2.shape[0]
total_col = df2.shape[1]

item_data = df2.iloc[10, 0]
print(item_data)
value2 = int(item_data)


def compDataShu(item_data, value):
    if (item_data is None):
        return False
    if (len(str(item_data)) == 0):
        return False
    # print(item_data)
    lt = item_data.split(',')
    #res = lt[-5:]
    res = lt[::-1]
    pre = -1
    index = 0

    for item in res:
        if (index == 5):
            break
        item = item.replace(']', '')
        ss = item.split('[')
        if (int(ss[0]) == value):
            return True
    return False


def readShu():
    # print("---A----")
    for col in range(0, total_col):
        for i in range(10):  # row
            # print("------",i,col*3)
            item_data = df2.iloc[i, col]
            if (compDataShu(item_data, value2)):
                #readB(i+13, col)
                row = i+11
                print("shu ---b----", row, col)
                item_data = df2.iloc[row, col]
                data2[row-11].append(item_data)


readXiao()

readShu()

print(len(data1), len(data2))
print(len(data1[0]), len(data2[0]))

writer = pd.ExcelWriter(gDataPath+gDataFile +
                        gResultFile+surfix, engine='xlsxwriter')


df123 = pd.DataFrame(data1)
df223 = pd.DataFrame(data2)


df223.to_excel(writer, sheet_name="result1")
df123.to_excel(writer, sheet_name="result2")
writer.close()
xls.close()
