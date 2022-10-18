import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import re
import json
#workbook = xlsxwriter.Workbook('d:\澳尾.xlsx')

gDataPath = "c:/data/"
#gDataPath = "D:/Dowdload2022/"
gDataFile = "肖尾特点"
gResultFile = "结果"
surfix = ".xlsx"


xls = pd.ExcelFile(gDataPath+gDataFile+surfix)
result_shu_g = {'0': 0, '1': 0, '2': 0, '3': 0,
                '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
result_xiao_g = {'龙': 0, '狗': 0, '牛': 0, '猪': 0, '鸡': 0,
                 '兔': 0, '马': 0, '虎': 0, '蛇': 0, '鼠': 0, '猴': 0, '羊': 0}


def xiao_celldata(result_xiao, item_data):
    if ((item_data) == "nan"):
        return
    if (len(item_data) == 0):
        print("find --------")
        return
    xiao_lt = ['龙', '狗', '牛', '猪', '鸡', '兔', '马', '虎', '蛇', '鼠', '猴', '羊']
    # print(item_data)
    lt = item_data.split(',')
    nums_dict = {}
    for item in lt:
        item = item.replace(']', '')
        ss = item.split('[')
        #print(ss[0], ss[1])
        nums_dict[ss[0]] = int(ss[1])
    # print(nums_dict)
    nums_dict = dict(
        sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
    # print("------------")
    print("sorted cell = ", nums_dict)
    pre = -1
    index = 0
    exit_lt = []
    for item in nums_dict.items():
        # print(item[0],item[1],pre)

        if (item[1] != pre):
            #print("ad 1")
            pre = item[1]
            index += 1
        result_xiao[item[0]] += index
        exit_lt.append(item[0])
    index += 1
    print("result 1 = ", result_xiao)
    if (len(exit_lt) != 12):
        for xiao in xiao_lt:
            # print(num_i)
            if (xiao not in exit_lt):
                result_xiao[xiao] += index
    print("result 2 = ", result_xiao)


def readxiao(result_xiao, s):
    print("-----Read Xiao---")
    df = pd.read_excel(xls, s)
    # print(df.columns)
    # print(df.shape)
    cols = df.shape[1]

    for i in range(len(df)):
        # print(i)
        for col in range(cols):
            if (df.iloc[i, col] is None):
                print("find noooo")
            if (len(str(df.iloc[i, col])) == 0):
                print("find noooo")
            else:
                item_data = df.iloc[i, col]
                item_data = str(item_data).strip()
                # print(item_data)
                xiao_celldata(result_xiao, item_data)
            print("result cell = ", result_xiao)
            # break
        print("row ret = ", result_xiao)
    print("all ret = ", result_xiao)
    # break


def shu_celldata(result_shu, item_data):
    print("shu_celldata----")
    if ((item_data) == "nan"):
        print("null------")
        return
    if (len(item_data) == 0):
        print("find --------")
        return
    # print(item_data)
    lt = item_data.split(',')
    nums_dict = {}
    for item in lt:
        num = re.sub(r'\D', " ", item)
        ss = num.split(' ')
        #print (ss[0],ss[1])
        nums_dict[ss[0]] = int(ss[1])
    # print(nums_dict)
    nums_dict = dict(
        sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
    # print("------------")
    print("all num in a cell = ", nums_dict)
    pre = -1
    index = 0
    exit_lt = []
    for item in nums_dict.items():
        # print(item[0],item[1])
        if (item[1] != pre):
            pre = item[1]
            index += 1
        result_shu[item[0]] += index
        exit_lt.append(item[0])
    index += 1
    print("tmp ret =", result_shu)
    if (len(exit_lt) != 10):
        for num_i in range(10):
            # print(num_i)
            if (str(num_i) not in exit_lt):
                result_shu[str(num_i)] += index
    print("cell ret =", result_shu)


def readshu(result_shu, s):
    print("-----Read Shu---")
    df = pd.read_excel(xls, s)
    # print(df.columns)
    # print(df.shape)
    cols = df.shape[1]

    for i in range(len(df)):
        # print(i)
        for col in range(cols):
            if (df.iloc[i, col] is None):
                print("find noooo")
            if (len(str(df.iloc[i, col])) == 0):
                print("find noooo")
            else:
                item_data = df.iloc[i, col]
                item_data = str(item_data).strip()
                shu_celldata(result_shu, item_data)
            print("row ret =", result_shu)
        print("row ret =", result_shu)
        # break
    print("all ret =", result_shu)


result_shu_g = {'0': 0, '1': 0, '2': 0, '3': 0,
                '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
result_xiao_g = {'龙': 0, '狗': 0, '牛': 0, '猪': 0, '鸡': 0,
                 '兔': 0, '马': 0, '虎': 0, '蛇': 0, '鼠': 0, '猴': 0, '羊': 0}


def xiao(result_xiao_g, s):
    result_xiao_g = {'龙': 0, '狗': 0, '牛': 0, '猪': 0, '鸡': 0,
                     '兔': 0, '马': 0, '虎': 0, '蛇': 0, '鼠': 0, '猴': 0, '羊': 0}
    readxiao(result_xiao_g, s)
    result_xiao_g = dict(
        sorted(result_xiao_g.items(), key=lambda item: item[1], reverse=True))
    str1 = str(result_xiao_g)
    print(str1)
    with open('result.txt', 'a+', encoding="utf-8") as f:
        f.write(str1)
        f.write("\n")
        f.write("\n")


def shu(result_shu_g, s):
    result_shu_g = {'0': 0, '1': 0, '2': 0, '3': 0,
                    '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    readshu(result_shu_g, s)
    result_shu_g = dict(sorted(result_shu_g.items(),
                        key=lambda item: item[1], reverse=True))
    str1 = str(result_shu_g)
    print(str1)
    with open('result.txt', 'a+', encoding="utf-8") as f:
        # f.write(json.dumps(result_shu_g))
        f.write(str(result_shu_g))
        f.write("\n")
        f.write("\n")


# for i in range(8):
#    xiao(result_xiao_g,i)
# for i in range(8):
#    shu(result_shu_g,i+8)
xiao(result_xiao_g, 0)
shu(result_shu_g, 1)
