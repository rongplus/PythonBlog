import xlsxwriter
import random
import pandas as pd
#workbook = xlsxwriter.Workbook('d:\澳尾.xlsx')

#gDataPath = "D:/Download/"
gDataPath = "c:/data/"
gDataFile = "澳尾9"
gResultFile = "结果"
surfix = ".xlsx"


xls = pd.ExcelFile(gDataPath+gDataFile+surfix)


g_logic = 12
g_column=4
g_max=[]
result_rows=[]
all = []

sh_index =0
new_df = []

def findTarget(target,numners):
    #print("findTarget",numners,len(numners))
    for colInx in range(5,10):
        #print(colInx)
        s = numners[colInx]
        #print(s)
        nums = s.split('[')
            #print(nums)
        if int(nums[0]) == target:
            return True
    return False

def getData(df,origCol,origRow, colOffset,rowOffset):
    #print("get")
    c_name = df.columns[origCol+colOffset]
    item_data = df[c_name][origRow+rowOffset]
    #print(item_data)
    lt = item_data.split(',')
    lt = lt[5:]
    r = ','.join(lt)
   
    new_df[origCol-3].append(r)
   
  

def createNewDataFrame(row,col):
    print("new data")
    for r in range(col):
        colData = ['' for x in range(11)]
        print(len(colData))
        new_df.append(colData)

def writeResult(df):
    print("done")
    index = 1
    for lt in new_df:
        print("Result-"+str(index),len(lt))
        df["Result-"+str(index)] = lt;
        index +=1
    writer = pd.ExcelWriter(gDataPath+gDataFile+gResultFile+surfix, engine='xlsxwriter')
    
    df.to_excel(writer,index = False, sheet_name="name")
    writer.close()
        
    
def dealSheet(name,indexOfSheet):
    print(name)
    frame_width =10
    frame_height = 11#10+1 blank row
    
    df1 = pd.read_excel(xls , name)
    print(df1.columns)
    print(df1.shape)
    #prepare new dataframe
    
    
    total_row = df1.shape[0]
    total_col = df1.shape[1]
    createNewDataFrame(frame_height,total_col-frame_width-3)
    target_num = 0
    for row in range(0,total_row-frame_height):
        c_name = df1.columns[1]
       
       
        #print(row)
        if (row%11==0):
            target_num = df1[c_name][row]%10
        #print("target=" ,target_num )
        for col in range(3,total_col-frame_width):
            c_name = df1.columns[col] 
            item_data = df1[c_name][row]
            if (pd.isna(item_data)):
                new_df[col-3].append('')
                continue
            #print(df1[c_name][row])
            lt = item_data.split(',')
            #print("data = ------",lt)
            if (findTarget(target_num,lt)):
                #print("find one",row,col-2)
                getData(df1,col,row,frame_width,frame_height)
            else:
                 new_df[col-3].append('')
                
            #break
    writeResult(df1)
    
for sheet_name in xls.sheet_names:
    #print(sheet_name)
    dealSheet(sheet_name, sh_index)
    sh_index +=1
    #print(new_df)
    print(len(new_df[0]))
 

