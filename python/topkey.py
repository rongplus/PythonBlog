import matplotlib.pyplot as plt
import numpy as np
import csv
import collections
from collections import defaultdict
d_detail = {}
d_total = defaultdict(lambda:float)
dates= []
def getDates(file_name):
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for row in spamreader:
            if len(row) > 3 or len(row)<1:
                continue           
            if row[0] not in dates:
                dates.append(row[0])

    dates.sort()
    dates.insert(0,"metric")

     
def loadHistoryData(file_name,n):
    
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for row in spamreader:
            if len(row) > 3 or len(row)<1:
                continue
            #print(row[0], row[1])
            x = row[1].split(".")
            #print(x)
            metric = ""
            if (len(x)>4):
                metric = x[0]+"."+x[1]+"."+x[2]+"."+x[3] #+"."+x[4]
            else:
                metric = row[1]

            if metric == 'metricName':
                continue


            if d_detail.get(metric) == None:
                #print ("None")
                default_value=0
                
                d_detail[metric] =dict.fromkeys(dates,0)# defaultdict(lambda:float) #dict.fromkeys([x for x in range(30)])
                d_detail[metric]["metric"] = metric
            #print(d_detail)
           
         
            #print(d_detail[metric][row[0]] )
            d_detail[metric][row[0]] = int(row[2]) 
            if metric in d_total.keys():
                d_total[metric] =float(d_total[metric])+ float(row[2])    
            else:
                d_total[metric] = float(row[2])
            if row[0] not in dates:
                dates.append(row[0])



def test():
    for it in d_total.items():
            print(it[0],it[1])

    for item in d_detail.items():
        print(item[0])
        values=[]
        
        for d in dates:
            if d not in item[1].keys():
                item[1][d] = 0
        dict(sorted(item[1].items(), key=lambda item: item[0]))
        print(item[1].keys())
        for sub in item[1].items():
            print(sub[0],sub[1])
            
        break

def writeAll(file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dates)

        writer.writeheader()
        for item in d_detail.items():
            writer.writerow( item[1])
getDates('/Users/ronghuang/Downloads/30days_topkey_-1.csv')
loadHistoryData('/Users/ronghuang/Downloads/30days_topkey_-1.csv',0)  
writeAll('/Users/ronghuang/Pinterest/topkey/r.csv')