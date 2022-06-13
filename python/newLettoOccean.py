import xlsxwriter
import random
import pandas as pd
#workbook = xlsxwriter.Workbook('d:\澳尾.xlsx')

gDataPath = "d:/analisis/"
gDataFile = "data.xlsx"
gResultFile = "result.xlsx"

xls = pd.ExcelFile(gDataPath+gDataFile)
df1 = pd.read_excel(xls)
numOfRow = df1.shape[0]
print(numOfRow)
value = df1[1][49]
print(value)
writer = pd.ExcelWriter(gDataPath+gResultFile, engine='xlsxwriter')

result_dict = {}
print("value=",value)
for j in range(1,12):
    row=[]
    for i in range(49):
    
        v = df1[j][i]
        lt = v.split(',')
        print("lt length=", len(lt))
        
        #print (lt)
        bF=False
        for ind in range(len(lt)-12,len(lt)):
            nums = lt[ind].split('[')
            #print (nums[0])
            if int( nums[0])==value:               
                bF=True 
                #print ("find=", ind)
        if bF:
            r_row = df1[j][i+50]
            row.append(r_row)
            #print(row)
        else:
            row.append("")
        #print(row)
        #print(i,"-------------")
    print("col=", j, len(row))
    result_dict[j]=row        
        #for s in lt:
        #    nums = s.split('[')
        #    print(nums[0])

df2 = pd.DataFrame(result_dict) 
#print( df1.shape, df2.shape)
df1 = df1.append(df2, ignore_index = True)
#print( df1.shape)

df1.to_excel(writer)
writer.close()