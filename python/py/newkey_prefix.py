from collections import defaultdict
import csv
dct = defaultdict(list)
dcardinality = defaultdict(list)
def loadHistoryData(file_name,n):
    
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        
        for row in spamreader:
            if len(row) > 2 or len(row)<1:
                continue
            #print(row[0], row[1])
            x = row[0].split(".")
            #print(x)
            metric = ""
            if (len(x)>4):
                metric = x[0]+"."+x[1]+"."+x[2]+"."+x[3] #+"."+x[4]
            else:
                metric = row[0]

            if metric == 'metricName':
                continue


            if dct.get(metric) == None:
                #print ("None")
                dct[metric].append(0)                
                dct[metric].append(0)
                

            dct[metric][n] += int(row[1])     

    


loadHistoryData("/Users/ronghuang/Pinterest/newkey/onday0517.csv",0)
loadHistoryData("/Users/ronghuang/Pinterest/newkey/twoday0717.csv",1)


def writeAll(file_name, dict):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['metricName', 'value1','value2','value 2-1']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for m,nums in dict.items():
            if f'{m}' == 'metricName':
                continue
            stt1 = f'{nums[0]}'
            stt2 = f'{nums[1]}'
            #print (stt1,stt2)
            num1 = int(stt2) - int(stt1)
           
            writer.writerow({'metricName':f'{m}','value1':f'{nums[0]}','value2':f'{nums[1]}','value 2-1': num1})
           

writeAll("newkey2day3.csv",dct)

