
import xlsxwriter
import random
import pandas as pd
#workbook = xlsxwriter.Workbook('d:\澳尾.xlsx')

gDataPath = "d:/analisis/"
gDataFile = "澳尾4.xlsx"
gResultFile = "澳尾结果.xlsx"


xls = pd.ExcelFile(gDataPath + gDataFile)

g_logic = 10
g_column=4
g_max=[]
result_rows=[]

def append_result(colIndex,result,rd):
    print("add to =",colIndex,result)
    rd[colIndex].append(result)
    
    
def append_blank_row(stageIndex,rd):
     
    while len(rd[1]) < stageIndex+ g_logic:
        rd[1].append("")
    while len(rd[2]) < stageIndex+ g_logic:
        rd[2].append("")
    while len(rd[3]) < stageIndex+ g_logic:
        rd[3].append("")
    while len(rd[4]) < stageIndex+ g_logic:
        rd[4].append("")
    

def find_result(colIndex,rowIndex,rd,dataFrame):
    #print("--------------------find result--start--",colIndex,rowIndex)
    if colIndex !=1:
        #print("find result--same column--",colIndex)
        result_row = dataFrame[colIndex][rowIndex+g_logic]  
        result_rows.append(result_row)
        append_result(colIndex-1,result_row,rd)
        #print(result_row)
       
    if colIndex !=4:    
        result_row = dataFrame[colIndex+1][rowIndex+g_logic]  
        result_rows.append(result_row)
        append_result(colIndex,result_row,rd)
        #print("find in", colIndex,result_row)
    #print("-------------------------find result--end--col,row",colIndex,rowIndex)
        
#处理某期，某组结果 start_index= 期第一行，col= phase title
def deal_stage_phase(start_index, col, zodiac,sheet_index,rd,dataFrame):
    max1 = 0;  
    #loop 1, get max value
    #进入逻辑, 得到所在column最大值
    for i in range(g_logic):
        #print(col, index)
        row = dataFrame[col][start_index+i]
        lt = row.split(',')
        for s in lt:
            nums = s.split('[')
            #print(nums)
            if int(nums[0]) == zodiac:
                #biggest
                if s==lt[len(lt)-1]: 
                    #print(row)
                    find_result(col,start_index+ i,rd,dataFrame)                   
                    continue
                
                valueLast= lt[len(lt)-1].split('[')[1].replace(']','')
                valueCur = nums[1].replace(']','')
                if int(valueCur) == int(valueLast):
                    #print(row)
                    find_result(col,start_index+ i,rd,dataFrame)
                    continue
                #found the zodiac, go next loop
                continue
                    
    return 0

#读每一期， start_index是期第一行，每次共处理g_logic行
def deal_stage(start_index,sheet_index,rd,dataFrame):
    zodiac = int(dataFrame['号码'][start_index]) %10

    for i in range(g_column):
        deal_stage_phase(start_index, i+1,zodiac,sheet_index,rd,dataFrame)   
        #print("----------------------------------------" ,i ,"------------------------")

def dealSheet(name,indexOfSheet):
    print("Open sheet" , name)
    result_dict = {1:["","","","","","","","","",""],2:["","","","","","","","","",""],3:["","","","","","","","","",""],4:["","","","","","","","","",""]}
   
    result_rows = ["","","","","","","","","",""]
    df1 = pd.read_excel(xls , name)
    numOfRow = df1.shape[0]
    index = 0
    result_rows.clear()
    while index < numOfRow-g_logic:
        #print("read logic", index)
        deal_stage(index,indexOfSheet,result_dict,df1)
        print("----------------------------------------" ,index ,"------------------------")
        index = index +g_logic
        #添加空行
        while len(result_rows) < index+ g_logic:
            result_rows.append("")
        append_blank_row(index,result_dict)
            
        print("----------------------------------------" ,index ,"------------------------")
        #break

    
    write_sheet(numOfRow,name,result_dict,df1)
    
    
   
def write_sheet(numOfRow,name,rd,dataFrame):
    print("wrtie file")
    if len(rd[1]) == numOfRow:
        dataFrame['result1'] = rd[1]
    else:
        print("result 1", len(rd[1]))
    if len(rd[2]) == numOfRow:
        dataFrame['result2'] = rd[2]
    else:
        print("result 2", len(rd[2]))
    if len(rd[3]) == numOfRow:
        dataFrame['result3'] = rd[3]
    if len(rd[4]) == numOfRow:
        dataFrame['result4'] = rd[4]
 
    dataFrame.to_excel(writer, sheet_name=name)
  

sh_index=0

writer = pd.ExcelWriter(gDataPath+gResultFile, engine='xlsxwriter')

#global worksheet
#worksheet = workbook.add_worksheet()
for sheet_name in xls.sheet_names:
   
    dealSheet(sheet_name, sh_index)
    sh_index = sh_index+1
    #break

writer.close()