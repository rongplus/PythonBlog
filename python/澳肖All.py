import xlsxwriter
import random
import pandas as pd

all =[]
gDataPath = "d:/analisis/"
gDataPath = "c:/data/"
gResultFile = "澳肖结果.xlsx"
gAllResultFile = "澳肖结果All.xlsx"

def doJob():

    xls_total = pd.ExcelFile(gDataPath+gResultFile)
    sh_index = 0
    for sheet_name in xls_total.sheet_names:
        df1 = pd.read_excel(xls_total , sheet_name)
        
        print(sheet_name)
        #if sh_index==0:
        print(df1.columns.tolist())
        
        
        all.append(df1['result1'])
        all.append(df1['result2'])
        all.append(df1['result3'])
        all.append(df1['result4'])
        sh_index+=1
    data = {}
    print(len(all))
    for i in range(sh_index):
        data[str(i)+"-1"] = all[i*4]
    for i in range(sh_index):
        data[str(i)+"-2"] = all[i*4+1]  
    for i in range(sh_index):
        data[str(i)+"-3"] = all[i*4+2]
    for i in range(sh_index):
        data[str(i)+"-4"] = all[i*4+3]

    df = pd.DataFrame(data=data)
    print(df.columns.tolist())
    writer = pd.ExcelWriter(gDataPath+gAllResultFile, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="AllResult")
    writer.close()
        
    xls_total.close()


doJob()
gResultFile = "澳尾结果.xlsx"
gAllResultFile = "澳尾结果All.xlsx"

#doJob()