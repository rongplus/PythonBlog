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
    print(int(len(df)/13))
    # return

    for i in range(int(len(df)/13)):
        print(i)
        result_xiao = {'龙': 0, '狗': 0, '牛': 0, '猪': 0, '鸡': 0,
                       '兔': 0, '马': 0, '虎': 0, '蛇': 0, '鼠': 0, '猴': 0, '羊': 0}
        for luoji in range(13):
            for col in range(2, cols):
                #print("------",i*13+luoji,col,df.iloc[i*13+luoji, col])
                if (df.iloc[i*13+luoji, col] is None):
                    print("find noooo")
                if (len(str(df.iloc[i*13+luoji, col])) == 0):
                    print("find noooo")
                else:
                    item_data = df.iloc[i*13+luoji, col]
                    item_data = str(item_data).strip()
                    # print(item_data)
                    xiao_celldata(result_xiao, item_data)
        # i+=12
        result_xiao = dict(
            sorted(result_xiao.items(), key=lambda item: item[1], reverse=True))
        str1 = str(result_xiao)
        print(str1)
        total = 0
        for item in result_xiao.items():
            total += item[1]
        print("total=", total)
        with open(gDataFile+'.txt', 'a+', encoding="utf-8") as f:
            f.write(str1)
            f.write("\n")
            f.write("\n")
            #print("result cell = ", result_xiao)
            # break
        #print("row ret = ", result_xiao)
    #print("all ret = ", result_xiao)
    # break


def readshu(result_shu, s):
    print("-----Read Shu---")
    df = pd.read_excel(xls, s)
    # print(df.columns)
    # print(df.shape)
    cols = df.shape[1]

    for i in range(int(len(df)/11)):
        print(i)
        result_shu = {'0': 0, '1': 0, '2': 0, '3': 0,
                      '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for luoji in range(11):
            for col in range(2, cols):
                if (df.iloc[i*11+luoji, col] is None):
                    print("find noooo")
                if (len(str(df.iloc[i*11+luoji, col])) == 0):
                    print("find noooo")
                else:
                    item_data = df.iloc[i*11+luoji, col]
                    item_data = str(item_data).strip()
                    shu_celldata(result_shu, item_data)
        # i+=10
        result_shu = dict(sorted(result_shu.items(),
                                 key=lambda item: item[1], reverse=True))
        str1 = str(result_shu)
        print(str1)
        with open(gDataFile + '.txt', 'a+', encoding="utf-8") as f:
            # f.write(json.dumps(result_shu_g))
            f.write(str(result_shu))
            f.write("\n")
            f.write("\n")

    print("all ret =", result_shu)


def xiao(result_xiao_g, s):
    result_xiao_g = {'龙': 0, '狗': 0, '牛': 0, '猪': 0, '鸡': 0,
                     '兔': 0, '马': 0, '虎': 0, '蛇': 0, '鼠': 0, '猴': 0, '羊': 0}
    readxiao(result_xiao_g, s)


def shu(result_shu_g, s):
    result_shu_g = {'0': 0, '1': 0, '2': 0, '3': 0,
                    '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    readshu(result_shu_g, s)
    result_shu_g = dict(sorted(result_shu_g.items(),
                        key=lambda item: item[1], reverse=True))
    str1 = str(result_shu_g)
    print(str1)
    with open(gDataFile + '.txt', 'a+', encoding="utf-8") as f:
        # f.write(json.dumps(result_shu_g))
        f.write(str(result_shu_g))
        f.write("\n")
        f.write("\n")


def xiao_celldata(result_xiao, item_data):
    if ((item_data) == "nan"):
        return
    if (len(item_data) == 0):
        print("find --------")
        return

    # print(item_data)
    lt = item_data.split(',')
    nums_dict = {}
    for item in lt:
        #print("cell data= " , item)
        item = item.replace(']', '')
        ss = item.split('[')
        #print(ss[0], ss[1])
        nums_dict[ss[0]] = int(ss[1])
    # print(nums_dict)
    nums_dict = dict(
        sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
    # print("------------")
    #print("sorted cell = ", nums_dict)
    (xiao, num), *rest = nums_dict.items()

    pre = num
    index = 0
    exit_lt = []
    for item in nums_dict.items():
        # print(item[0],item[1],pre)
        if (item[1] != pre):
            break
        result_xiao[item[0]] += 1


def shu_celldata(result_shu, item_data):
    # print("shu_celldata----")
    if ((item_data) == "nan"):
        # print("null------")
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
    #print("all num in a cell = ", nums_dict)
    (wei, num), *rest = nums_dict.items()
    pre = num
    index = 0

    for item in nums_dict.items():
        # print(item[0],item[1])
        if (item[1] != pre):
            break
        #print("item = ",item[0],item[1])
        result_shu[item[0]] += 1


gDataPath = "c:/data/"
#gDataPath = "D:/Dowdload2022/"
gDataFile = "澳肖尾统计"
gResultFile = "结果"
surfix = ".xlsx"


xls = pd.ExcelFile(gDataPath+gDataFile+surfix)
result_shu_g = {'0': 0, '1': 0, '2': 0, '3': 0,
                '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
result_xiao_g = {'龙': 0, '狗': 0, '牛': 0, '猪': 0, '鸡': 0,
                 '兔': 0, '马': 0, '虎': 0, '蛇': 0, '鼠': 0, '猴': 0, '羊': 0}


xiao(result_xiao_g, 0)
shu(result_shu_g, 1)
print("done")


# ------function test-----
# xiao_celldata(result_xiao_g,"牛[788],蛇[804],鼠[805],龙[826],狗[826],猴[836],马[867],兔[885],鸡[904],虎[910]")
#result_xiao_g = dict(  sorted(result_xiao_g.items(), key=lambda item: item[1], reverse=True))
#str1 = str(result_xiao_g)
# print(str1)
# xiao_celldata(result_xiao_g,"鸡[9797],马[9803],羊[9812],牛[9821],兔[9843],猪[9892],猴[9894],蛇[9921],龙[9973],狗[10039],虎[10090],鼠[10222]")
#result_xiao_g = dict(sorted(result_xiao_g.items(), key=lambda item: item[1], reverse=True))
#str1 = str(result_xiao_g)
# print(str1)

# shu_celldata(result_shu_g,"0[12278],8[12430],2[12490],6[12500],3[12624],5[12764],7[12769],4[12801],9[12821],1[12839]")

#str1 = str(result_shu_g)

#print("rest == ", str1)
# shu_celldata(result_shu_g,"4[1515],2[1532],7[1534],9[1539],1[1547],3[1563],5[1582],6[1585],0[1709],8[1744]")
#result_shu_g = dict( sorted(result_shu_g.items(), key=lambda item: item[1], reverse=True))
#str1 = str(result_shu_g)
# print(str1)


# ---------------------function test
#gDataPath = "D:/Dowdload2022/"
#xls = pd.ExcelFile(gDataPath+gDataFile+surfix)
#readxiao(result_xiao_g, s)
#readshu(result_shu_g, s)


# shu()
# xiao()
