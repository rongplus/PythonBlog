from urllib.request import Request, urlopen
import re
import argparse
import sys
import json
import os
# -*- coding: UTF-8 -*-

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Target Url",type=str)
parser.add_argument('type', help="Target Type(DOC|PPT|TXT|PDF)",type=str)
args = parser.parse_args()

url = args.url
type = args.type

y = 0
def DOC(url):
    doc_id = re.findall('view/(.*).html', url)[0]
    html = requests.get(url).text
    lists=re.findall('(https.*?0.json.*?)\\\\x22}',html)
    lenth = (len(lists)//2)
    NewLists = lists[:lenth]
    for i in range(len(NewLists)) :
        NewLists[i] = NewLists[i].replace('\\','')
        txts=requests.get(NewLists[i]).text
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),',txts)
        for i in range(0,len(txtlists)):
            global y
            print(txtlists[i][0].encode('utf-8').decode('unicode_escape','ignore'))
            if y != txtlists[i][1]:
                y = txtlists[i][1]
                n = '\n'
            else:
                n = ''
            filename = doc_id + '.txt'
            with open(filename,'a',encoding='utf-8') as f:
                f.write(n+txtlists[i][0].encode('utf-8').decode('unicode_escape','ignore').replace('\\',''))
        print("save"+filename)




def PPT(url):
    doc_id = re.findall('view/(.*).html',url)[0]
    url = "https://wenku.baidu.com/browse/getbcsurl?doc_id="+doc_id+"&pn=1&rn=99999&type=ppt"
    html = requests.get(url).text
    lists=re.findall('{"zoom":"(.*?)","page"',html)
    for i in range(0,len(lists)):
        lists[i] = lists[i].replace("\\",'')
    try:
        os.mkdir(doc_id)
    except:
        pass
    for i in range(0,len(lists)):
        img=requests.get(lists[i]).content
        with open(doc_id+'\img'+str(i)+'.jpg','wb') as m:
            m.write(img)
    print("PPT" + doc_id +" ")

def TXT(url):
    doc_id = re.findall('view/(.*).html', url)[0]
    url = "https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id="+doc_id
    html = requests.get(url).text
    md5 = re.findall('"md5sum":"(.*?)"',html)[0]
    pn = re.findall('"totalPageNum":"(.*?)"',html)[0]
    rsign = re.findall('"rsign":"(.*?)"',html)[0]
    NewUrl = 'https://wkretype.bdimg.com/retype/text/'+doc_id+'?rn='+pn+'&type=txt'+md5+'&rsign='+rsign
    txt = requests.get(NewUrl).text
    jsons = json.loads(txt)
    texts=re.findall("'c': '(.*?)',",str(jsons))
    print(texts)
    filename=doc_id+'.txt'
    with open(filename,'a',encoding='utf-8') as f:
        for i in range(0,len(texts)):
            texts[i] = texts[i].replace('\\r','\r')
            texts[i] = texts[i].replace('\\n','\n')

            f.write(texts[i])
    print("save" + filename)

def PDF(url):
    doc_id = re.findall('view/(.*).html',url)[0]
    url = "https://wenku.baidu.com/browse/getbcsurl?doc_id="+doc_id+"&pn=1&rn=99999&type=ppt"
    html = requests.get(url).text
    lists=re.findall('{"zoom":"(.*?)","page"',html)
    for i in range(0,len(lists)):
        lists[i] = lists[i].replace("\\",'')
    try:
        os.mkdir(doc_id)
    except:
        pass
    for i in range(0,len(lists)):
        img=requests.get(lists[i]).content
        with open(doc_id+'\img'+str(i)+'.jpg','wb') as m:
            m.write(img)
    print("FPD " + doc_id + " ")


if __name__ == "__main__":
    try:
        print("""
###Athor:Lz1y
###Blog:www.Lz1y.cn
###TIPS:PDF|PPT 
        """)
        eval(type.upper())(url)
    except:
        print(" erroe")