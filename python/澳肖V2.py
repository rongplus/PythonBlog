import xlsxwriter
import random
import pandas as pd
#workbook = xlsxwriter.Workbook('d:\澳尾.xlsx')

gDataPath = "c:/data/"
gDataPath = "D:/analisis/"
gDataFile = "澳肖.xlsx"
gResultFile = "澳肖结果.xlsx"

xls = pd.ExcelFile(gDataPath+gDataFile)


g_logic = 12
g_column=4
g_max=[]
result_rows=[]
all = []


def append_result(colIndex,result,rd):
    print("append_result to =",colIndex,result)
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
    
def get_big2(rowText):
    lt = rowText.split(',')
    nums_all = []
    for s in lt:
        nums = s.split('[')
        val = nums[1].replace(']','')
        nums_all.append( int(val))
    
    #print("big2 ori", nums_all)
    #nums_all.sort(reverse=True)
    #print("big2 sort", nums_all)

    nums_all = list(set(nums_all))
    nums_all.sort(reverse=True)
    #print("big2 ret", nums_all,rowText)

    

    return [nums_all[0],nums_all[1]]


def find_result(colIndex,rowIndex,rd,dataFrame):
    #result_row = dataFrame[colIndex][rowIndex+g_logic]  
    #result_rows.append(result_row)
    #append_result(colIndex,result_row,rd)
    #return
    #print("--------------------find result--start--", "col=",colIndex,rowIndex)
    
    result_row = dataFrame[colIndex][rowIndex]  
    result_rows.append(result_row)
    append_result(colIndex-2,result_row,rd)
        #print("find in", colIndex,result_row)
    #print("-------------------------find result--end--col,row",colIndex,rowIndex)

#处理某期，某组结果 start_index= 期第一行，col= phase title
def deal_stage_phase2(start_index,row, col, zodiac,sheet_index,rd,dataFrame):
    max1 = 0;  
    #print("deal_stage_phase2-0",start_index,row, "col=", col, zodiac,sheet_index)

    #看看是不是最大。
    #本逻辑生肖
    new_zodiac = dataFrame['生肖'][start_index]
    row_text = dataFrame[col][start_index+row]
    #print("deal_stage_phase2-1",new_zodiac,row_text)
    lt = row_text.split(',')

    ret = get_big2(row_text)
    #print("big 2 = ",ret)
    for s in lt:
        nums = s.split('[')
        #print(nums)
        if nums[0] == new_zodiac:
            valueCur = nums[1].replace(']','')
            if int(valueCur) == ret[0] or int(valueCur) == ret[1]:
                #print(row)
                    #去下一个逻辑，下一列 相同位置
                print("第二步结果：",new_zodiac,row,row_text)
                find_result(col+1,start_index+g_logic+ row,rd,dataFrame)
                continue
            #found the zodiac, go next loop
            continue
                    
    return 0




#处理某期，某组结果 start_index= 期第一行，col= phase title
def deal_stage_phase(start_index, col, zodiac,sheet_index,rd,dataFrame):

    #print("deal_stage_phase",start_index, "col=", col, zodiac,sheet_index)
    max1 = 0;  
    #loop 1, get max value
    #进入逻辑, 得到所在column最大值
    for i in range(g_logic):
        #print(col, index)
        row = dataFrame[col][start_index+i]
        lt = row.split(',')
        ret = get_big2(row)
        for s in lt:
            nums = s.split('[')
            #print(nums)
            if nums[0] == zodiac:                
                valueCur = nums[1].replace(']','')
                v = int(valueCur)
                if v == ret[0] or v == ret[1]:
                    print("第一步结果：",zodiac, nums[0], v, ret,i+1,row)
                    #去下一个逻辑，下一列
                    deal_stage_phase2(start_index+ g_logic,i,col+1,zodiac,sheet_index, rd,dataFrame)
                    continue
                #found the zodiac, go next loop
                continue
    print("add blank",start_index,col,len(rd[col]) )
    while len(rd[col]) < start_index+ g_logic*3:
        rd[col].append("")                
    return 0

#读每一期， start_index是期第一行，每次共处理g_logic行
def deal_stage(start_index,sheet_index,rd,dataFrame):
    zodiac = dataFrame['生肖'][start_index]

    for i in range(g_column-2):
        deal_stage_phase(start_index, i+1,zodiac,sheet_index,rd,dataFrame)   

def dealSheet(name,indexOfSheet):
    print("Open sheet" , name)
    result_dict = {1:["","","","","","","","","","","","","","","","","","","","","","","",""],2:["","","","","","","","","","","","","","","","","","","","","","","",""],3:["","","","","","","","","","","","","","","","","","","","","","","",""],4:["","","","","","","","","","","","","","","","","","","","","","","",""]}
   
    result_rows = ["","","","","","","","","",""]
    df1 = pd.read_excel(xls , name)
    numOfRow = df1.shape[0]
    index = 0
    result_rows.clear()
    while index < numOfRow-g_logic*2:
        #print("read logic", index)
        deal_stage(index,indexOfSheet,result_dict,df1)
        
        index = index +g_logic
        #添加空行
        while len(result_rows) < index+ g_logic*2:
            result_rows.append("")
        append_blank_row(index,result_dict)
            
        print("----------------------------------------" ,index ,"------------------------")
        #break

    
    write_sheet(numOfRow,name,result_dict,df1)
    
    
   
def write_sheet(numOfRow,name,rd,dataFrame):
    

    while len(rd[1]) < numOfRow:
        rd[1].append("")
    while len(rd[2]) < numOfRow:
        rd[2].append("")
    while len(rd[3]) < numOfRow:
        rd[3].append("")
    while len(rd[4]) < numOfRow:
        rd[4].append("")

    print("wrtie file 1",len(rd[1]) , numOfRow)
    if len(rd[1]) == numOfRow:
        dataFrame['result1'] = rd[1]
    else:
        print("result 1", len(rd[1]))
        print( rd[1])
    if len(rd[2]) == numOfRow:
        dataFrame['result2'] = rd[2]
    else:
        print("result 2", len(rd[2]))
        print( rd[2])
    if len(rd[3]) == numOfRow:
        dataFrame['result3'] = rd[3]
    if len(rd[4]) == numOfRow:
        dataFrame['result4'] = rd[4]

    if len(result_rows) == numOfRow:
        dataFrame['result'] = result_rows
    else:
        print("result_rows ??", len(result_rows))
        #dataFrame.to_excel(writer, sheet_name=name)
    all.append(rd[1])
    all.append(rd[2])
    all.append(rd[3])
    dataFrame.to_excel(writer, sheet_name=name)
  
sh_index=0

writer = pd.ExcelWriter(gDataPath+gResultFile, engine='xlsxwriter')

#global worksheet
#worksheet = workbook.add_worksheet()
for sheet_name in xls.sheet_names:
   
    dealSheet(sheet_name, sh_index)
    sh_index = sh_index+1
    break

writer.close()
xls.close()