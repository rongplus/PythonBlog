import mysql.connector


# Configure MySQL connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Good2017!",
    "database": "HackerBank",
}


# Initialize global cursor
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(buffered=True)


try:
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT * FROM notes")        
    data = cursor.fetchall()
    for record in data:
        print(len(record))
        print(record)
        print("-------------------")
        s = ''
        for st in record:
            a = st.find('a)')
            b = st.find('b)')
            c = st.find('c)')
            d = st.find('d)')
            if d!=-1:                
                 print("------find-----")
                 q = st[0:a]
                 aa = st[a:b]
                 ab = st[b:c]
                 ac = st[c:d]
                 ad = st[d:]
                 s = s + f"<br>"+q+ f"<br>"+aa+ f"<br>"+ab+ f"<br>"+ac+ f"<br>"+ad
            
            else:
                 s = s + str(st) + f"<br>"
        print (s)
        record = s
        #print(record)
        break
        #record[0] = record[0].replace('\n\r', '<br>')
        #record['answers'] = record['answers'].replace('\n', '').replace('\r', '')
        #record['rotation'] = record['rotation'].replace('\n', '').replace('\r', '')



    #data = [  record,record1]
    #print(data)
except Exception as e:
        print( f"Error fetching records: {str(e)}")