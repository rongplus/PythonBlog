import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import re
import json

gDataPath = ""
#gDataPath = "D:/Dowdload2022/"
gDataFile = "20221201统计"
gResultFile = "结果"
surfix = ".xlsx"
xls = pd.ExcelFile(gDataPath+gDataFile+surfix)

df = pd.read_excel(xls, 0)
df = df.replace('nan', '')
df = df.fillna('')
print(df.columns)
print(df.shape)
total_row = df.shape[0]
total_col = df.shape[1]

item_data = df.iloc[49, 0]
print(item_data)
value1 = int(item_data)


data = []
data1 = []
data2 = []
for x in range(int(total_col/2)):
    data.append([])
for x in range(50):
    data1.append([])
    data2.append([])


def compData(item_data, value):
    if (item_data is None):
        return False
    if (len(str(item_data).strip()) == 0):
        return False
    print(item_data)
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


def readA():
    # print("---A----")
    for col in range(0, int(total_col/2)):
        rCol = col*2
        for i in range(49):  # row
            # print("------",i,col*3)
            item_data = df.iloc[i, col*2]
            if (compData(item_data, value1)):
                readB(i+50, rCol)
            else:
                data1[i].append("")

    for col in range(0, int(total_col/2)):
        for i in range(49):  # row
            rCol = col*2+1
            # print("------",i,col*3)
            item_data = df.iloc[i, rCol]
            if (compData(item_data, value1)):
                readB2(i+50, rCol)
            else:
                data2[i].append("")


def readB(row, col):
    # print("---b----",row,col)
    print("find  A ", row-50, "--", col-1, "  ",  row, "--", col)
    item_data2 = df.iloc[row-50, col-1]
    item_data = df.iloc[row, col]
    # print(item_data2)
    # print("-----------------------------")
    # print(item_data)
    # print("=============================")
    data1[row-50].append(item_data)


def readB2(row, col):
    # print("---b----",row,col)
    print("find B  ", row-50, "--", col-1, "  ",  row, "--", col)
    item_data2 = df.iloc[row-50, col-1]
    item_data = df.iloc[row, col]
    # print(item_data2)
    # print("-----------------------------")
    # print(item_data)
    # print("=============================")
    data2[row-50].append(item_data)


print("find  数据（行--列）   结果（行--列）", )
data = []
data1 = []
for x in range(int(total_col/2)):
    data.append([])
for x in range(50):
    data1.append([])
readA()


print(len(data1))
print(len(data1[0]))

writer = pd.ExcelWriter(gDataPath+gResultFile+"A"+surfix, engine='xlsxwriter')
header = []
for x in range(20):
    header.append("col" + str(x))

df123 = pd.DataFrame(data1)

df123.to_excel(writer, sheet_name="result")
writer.close()


writer2 = pd.ExcelWriter(gDataPath+gResultFile+"B"+surfix, engine='xlsxwriter')
header = []
for x in range(20):
    header.append("col" + str(x))

df124 = pd.DataFrame(data2)

df124.to_excel(writer2, sheet_name="result")
writer2.close()


xls.close()
