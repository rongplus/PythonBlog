import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import re
import json
#workbook = xlsxwriter.Workbook('d:\澳尾.xlsx')


def readxiao(result_xiao, s):
    print("-----Read Xiao---")
    df = pd.read_excel(xls, s)
    # print(df.columns)
    # print(df.shape)
    cols = df.shape[1]

    target = df.iloc[0, 1]
    print("xiao    =", target)

    for i in range(12):
        print(i)

        for col in range(3, cols):
            #print("------",i*13+luoji,col,df.iloc[i*13+luoji, col])
            if (df.iloc[i, col] is None):
                print("find noooo")
            if (len(str(df.iloc[i, col])) == 0):
                print("find noooo")
            else:
                item_data = df.iloc[i, col]
                item_data = str(item_data).strip()
                # print(item_data)
                xiao_celldata(target, item_data, col, i)

    print(xiao_ret)

    ret_df = []
    empty_row = []
    for x in range(cols):
        empty_row.append(' ')
    for i in range(12):
        if (i not in xiao_ret):
            ret_df.append(empty_row)
        else:
            tmp = []
            ret_cols = xiao_ret[i]
            for col in range(cols):
                if (col not in ret_cols):
                    tmp.append(' ')
                else:
                    tmp.append(df.iloc[i+12, col])
            ret_df.append(tmp)

    # print(ret_df)
    writer = pd.ExcelWriter(gDataPath+gResultFile +
                            "-1"+surfix, engine='xlsxwriter')
    header = []
    for x in range(cols):
        header.append("col" + str(x))

    df = pd.DataFrame(ret_df, columns=header)

    df.to_excel(writer, sheet_name="xiao")
    writer.close()


def readshu(result_shu, s):
    print("-----Read Shu---")
    df = pd.read_excel(xls, s)
    # print(df.columns)
    # print(df.shape)
    cols = df.shape[1]

    item_data = df.iloc[0, 1]
    print("num    =", item_data)
    target = int(item_data) % 10
    print("target    =", target)

    for i in range(10):
        print(i)
        for col in range(3, cols):
            if (df.iloc[i, col] is None):
                print("find noooo")
            if (len(str(df.iloc[i, col])) == 0):
                print("find noooo")
            else:
                item_data = df.iloc[i, col]
                item_data = str(item_data).strip()
                shu_celldata(target, item_data, i, col)

    print(wei_ret)

    ret_df = []
    empty_row = []
    for x in range(cols):
        empty_row.append(' ')
    for i in range(10):
        if (i not in wei_ret):
            ret_df.append(empty_row)
        else:
            tmp = []
            ret_cols = wei_ret[i]
            for col in range(cols):
                if (col not in ret_cols):
                    tmp.append(' ')
                else:
                    tmp.append(df.iloc[i+10, col])
            ret_df.append(tmp)

    # print(ret_df)
    writer = pd.ExcelWriter(gDataPath+gResultFile+surfix, engine='xlsxwriter')
    header = []
    for x in range(cols):
        header.append("col" + str(x))

    df = pd.DataFrame(ret_df, columns=header)

    df.to_excel(writer, sheet_name="wei")
    writer.close()
    # for ret in wei_ret.items():
    #    #print(ret)
    #    col = ret[0]
    #    rows = ret[1]


def xiao(result_xiao_g, s):
    readxiao(0, s)


def shu(result_shu_g, s):
    readshu(result_shu_g, s)


def xiao_celldata(result_xiao, item_data, col, row):
    if ((item_data) == "nan"):
        return
    if (len(item_data) == 0):
        print("find --------")
        return

    # print(item_data)
    lt = item_data.split(',')[6:]
    #print( "how == ",len(lt))
    ret = 0
    for item in lt:
        #print("cell data= " , item)
        item = item.replace(']', '')
        ss = item.split('[')

        if (ss[0] == result_xiao):
            # xiao_ret.append([col,row])
            if (row not in xiao_ret):
                xiao_ret[row] = []
            xiao_ret[row].append(col)
            break
            # print(row,col)


def shu_celldata(result_shu, item_data, row, col):
    # print("shu_celldata----")
    if ((item_data) == "nan"):
        # print("null------")
        return
    if (len(item_data) == 0):
        print("find --------")
        return
    # print(item_data)
    lt = item_data.split(',')[5:]
    ret = 0
    for item in lt:
        #print("cell data= " , item)
        item = item.replace(']', '')
        ss = item.split('[')
        #print(ss[0], ss[1])

        if (int(ss[1]) % 10 == result_shu):
            if (row not in wei_ret):
                wei_ret[row] = []
            wei_ret[row].append(col)
            break
            # print(row,col)


gDataPath = "c:/data/"
gDataPath = "D:/Dowdload2022/"
gDataFile = "澳肖尾上下对照"
gResultFile = "结果"
surfix = ".xlsx"

xiao_ret = {}
wei_ret = {}


xls = pd.ExcelFile(gDataPath+gDataFile+surfix)


xiao(0, 1)
shu(0, 0)
print("done")
