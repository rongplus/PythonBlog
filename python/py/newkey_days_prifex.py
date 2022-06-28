import sys
import argparse
from collections import defaultdict
import csv
import pandas as pd

from collections import defaultdict
import csv

dct = defaultdict(list)
dcardinality = defaultdict(list)
totalFile=15
def loadHistoryData(file_name,n):
    
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        header = next(spamreader)
        for row in spamreader:
            if len(row) > 2 or len(row)<1:
                continue
            #print(row[0], row[1])
            x = row[0].split(".")

            metric = ""
            if (len(x)>4):
                metric = x[0]+"."+x[1]+"."+x[2]+"."+x[3] #+"."+x[4]
            else:
                metric = row[0]


            if dct.get(metric) == None:
                #print ("None")
                for i in range(totalFile):
                    dct[metric].append(0) 
                

            dct[metric][n] += int(row[1])  
            

def writeAll(file_name, dict):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['metricName']
        for i in range(totalFile):
            fieldnames.append("day-" + str(i+1))
        for i in range(totalFile-1):
            fieldnames.append("delta-" + str(i+1))
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for m,nums in dict.items():
            if f'{m}' == 'metricName':
                continue
            row_dict =defaultdict(list)
            row_dict['metricName'] = m
            for i in range(len(nums)):
                row_dict['day-' + str(i+1)] = int(nums[i])
            for i in range(1, len(nums)):
                row_dict['delta-' + str(i)] = int(nums[i]) - int(nums[i-1])
                
           
           
            #writer.writerow({'metricName':f'{m}','value1':f'{nums[0]}','value2':f'{nums[1]}','value 2-1': num1})
            writer.writerow( row_dict)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process some integers.')

	print ('Number of arguments:', len(sys.argv), 'arguments.')
	print ('Argument List:', str(sys.argv))
	if len(sys.argv) < 4:
		print("Error, 4 patameters are required1")
		sys.exit(0)
	print("-------")
	totalFile = int(sys.argv[1])
	file_prefix = sys.argv[2]
	print( sys.argv[0]," total=",totalFile, " prefix=", file_prefix, " save to ", sys.argv[2])
	#sys.exit(0)

	for i in range(totalFile):
		loadHistoryData(file_prefix+str(i+1)+".csv",i)
	writeAll(sys.argv[3],dct)

