import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import re
import json

gDataPath = ""
gDataPath = "D:/Dowdload2022/"
gDataFile = "demo1"
gResultFile = "结果"
surfix = ".xlsx"
xls = pd.ExcelFile(gDataPath+gDataFile+surfix)

data1 = []
df1 = pd.read_excel(xls, 0)
df1 = df1.replace('nan', '')
df1 = df1.fillna('')
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
    print(item_data)
    lt = item_data.split(',')
    res = lt[-5:]

    for item in res:
        #print("cell data= " , item)
        item = item.replace(']', '')
        ss = item.split('[')
        if (ss[0] == value):
            return True
    return False


def readXiao():
    # print("---A----")
    for col in range(0, total_col):
        for i in range(12):  # row
            print("readxiao------", i, col)
            item_data = df1.iloc[i, col]
            if (compDataXiao(item_data, value1)):
                #readB(i+13, col)
                row = i+13
                print("---b----", row, col)
                item_data = df1.iloc[row, col]
                data1.append(item_data)


readXiao()


data2 = []

df2 = df1  # pd.read_excel(xls, 1)
df2 = df2.replace('nan', '')
df2 = df2.fillna('')
print(df2.columns)
print(df2.shape)
total_row = df2.shape[0]
total_col = df2.shape[1]

item_data = df2.iloc[10, 0]
print(item_data)
#value2 = int(item_data)


def compDataShu(item_data, value):
    if (item_data is None):
        return False
    if (len(str(item_data)) == 0):
        return False
    # print(item_data)
    lt = item_data.split(',')
    res = lt[-4:]

    for item in res:
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
                print("---b----", row, col)
                item_data = df2.iloc[row, col]
                data2.append(item_data)


# readShu()


print(len(data1), len(data2))

frame1 = []
for d in range(int(len(data1)/30)+1):
    print("d=", d)
    frame1.append([])
    for i in range(30):
        if (i+d*30) < len(data1):
            frame1[d].append(data1[i+d*30])
        # print(i+d*30)


frame2 = []
for d in range(int(len(data2)/30)+1):
    frame2.append([])
    for i in range(30):
        if (i+d*30) < len(data2):
            frame2[d].append(data2[i+d*30])


print(len(frame1), len(frame2))
print(len(frame1[0]), len(frame2[0]))

writer = pd.ExcelWriter(gDataPath+gDataFile +
                        gResultFile+surfix, engine='xlsxwriter')


df123 = pd.DataFrame(frame1)
df223 = pd.DataFrame(frame2)

df123.to_excel(writer, sheet_name="result1")
df223.to_excel(writer, sheet_name="result2")
writer.close()
xls.close()
