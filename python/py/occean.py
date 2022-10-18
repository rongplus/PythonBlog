import xlsxwriter
import random
import pandas as pd
from collections import defaultdict
import csv
gDataPath = "c:/data/"
#gDataPath = "d:/download/"
gDataFile = 'baifeibi'
#gDataFile = 'bai'
#workbook = xlsxwriter.Workbook('d:\澳尾.xlsx')
#xls = pd.ExcelFile('c:/data/baifeibi.xlsx')
xls = pd.ExcelFile(gDataPath + gDataFile +'.xlsx')
df1 = pd.read_excel(xls , '尾数')
df2 = pd.read_excel(xls , '生肖')

print( df1.keys())
#Get size. = rows and cols
print (df1.shape)

dct1 = defaultdict(list)

dct2 = defaultdict(list)

for i in range(10):
    dct1[i] = 0.0

for i in df1.index:
    for j in range(1,df1.shape[1]+1):
        col = 'a' + str(j)
        #print( df1[col][i])
        row = df1[col][i]
        lt = row.split(',')
        total = 0.0
        for s in lt:
            nums = s.split('[')
            a1 = nums[0]
            a2 = nums[1].replace(']','')
            #print(a1,a2)
            total += int(a2)
        for s in lt:
            nums = s.split('[')
            a1 = float(nums[0])   
            a2 = float(nums[1].replace(']',''))
            b1 = (a2/total)
            dct1[int(nums[0])] = dct1[ int(nums[0])]+ b1

dct1 = dict(sorted(dct1.items(), key=lambda item: item[1]))

        #for a,b in dct.items():
            #print(a,b)

dct2 = defaultdict(list)
nms = ['猪','猴','羊','蛇','虎','狗','龙','牛','兔','鼠','马','鸡']
for i in range(12):
    dct2[nms[i]] = 0.0

for i in df1.index:
    for j in range(1,df2.shape[1]+1):
        col = 'a' + str(j)
        #print( df1[col][i])
        row = df2[col][i]
        lt = row.split(',')
        total = 0.0
        for s in lt:
            nums = s.split('[')
            a1 = nums[0]
            a2 = nums[1].replace(']','')
            #print(a1,a2)
            total += int(a2)
        for s in lt:
            nums = s.split('[')
            a1 = nums[0]
            #print(a1)
            a2 = float(nums[1].replace(']',''))
            b1 = (a2/total)
            dct2[a1] = dct2[a1]+ b1
dct2 = dict(sorted(dct2.items(), key=lambda item: item[1]))

#for a,b in dct1.items():
#    print(a,b)
#print("-----------------------")
#for a,b in dct2.items():
#    print(a,b)
    
# coding = utf-8
# - * - coding: UTF- 8 - * - 
with open(gDataPath + gDataFile +"a.csv", 'w', newline='') as csvfile:
        fieldnames = ['cata', 'value',]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for m,nums in dct1.items(): 
            print (m,nums)   
            writer.writerow({'cata':m,'value':nums})
with open(gDataPath + gDataFile +"b.csv", 'w', newline='',encoding='utf-8-sig') as csvfile:   
    fieldnames = ['cata', 'value',]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    for m,nums in dct2.items():
        print (m,nums)        
        stt2 =f'{nums:9.4f}'
        print(stt2)
        writer.writerow({'cata':m,'value':nums})
        