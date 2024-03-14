from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

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

@app.route("/")
def home():
    all_routes = get_all_routes()
    print("List of all routes:")
    result=f"<br>"
    for route in all_routes:
        print(f"/{route}")
        result+= f"<a href=" + f"/{route}" + f">" + f"{route}" + f"</a><br>"
    return render_template("home.html", routes=all_routes)
    return "Welcome to the home page!" + result

@app.route("/about")
def about():
    return render_template("about.html")

def get_all_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            routes.append(rule.endpoint)
    return routes

@app.route("/addright", methods=["GET", "POST"])
def addright():
    if request.method == "POST":        
           return "addright"
    elif request.method =="GET":
        return "ABC"

    return render_template("addright.html")

@app.route("/addwrong", methods=["GET", "POST"])
def addwrong():
    if request.method == "POST":
        question = request.form.get("question")
        answers = request.form.get("answers")
        rotation = request.form.get("rotation")
        if question:
            save_note_to_db1(question,answers,rotation)
            return redirect(url_for("addwrong"))

    return render_template("addwrong.html")

def save_note_to_db(question, answers, rotation):
    try:
        sql = (
        "INSERT IGNORE INTO notes (question, answers, rotation,correct) "
        "VALUES (%s, %s, %s, 1)"
        )
        val = (question, answers, rotation)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")

def save_note_to_db1(question, answers, rotation):
    try:
        sql = (
        "INSERT IGNORE INTO notes (question, answers, rotation,correct) "
        "VALUES (%s, %s, %s, 0)"
        )
        val = (question, question, answers, rotation)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")


@app.route("/query", methods=["GET", "POST"])
def query():
    global cursor  # Use the global cursor

    if request.method == "POST":
        next_button = request.form.get("next_button")
        if next_button:
            record = cursor.fetchone()
            if record:
                return render_template("question.html", question=record[0],answers=record[1],rotation=record[2])
            else:
                return "No more records."
        return redirect(url_for("add"))

    cursor.execute("SELECT * FROM notes")
    record = cursor.fetchone()
   
    return render_template("question.html", question=record[0],answers=record[1],rotation=record[2])

def saveQuestions(question,answerA ,answerB ,answerC ,
        answerD ,answer ,rotation,correct ,module):
    try:
        sql = (
        "INSERT IGNORE INTO insurance (question,answerA ,answerB ,answerC ,"
        " answerD ,answer ,rotation ,correct ,module) "
        " VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s) "
        )
        val = (question,answerA ,answerB ,answerC , answerD ,answer ,rotation,correct ,module)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")


@app.route("/add", methods=["GET", "POST"])
def add():
     if request.method == "POST":
         con= request.form.get("question")
         
         if con:
            pos1 = con.find('a)')
            question = con[:pos1]
            pos2 = con.find('b)')
            ans_a = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('c)')
            ans_b = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('d)')
            ans_c = con[pos1:pos2]
            pos1 = pos2
            pos2 =  con.find('YOUR ANSWER')
            ans_d = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('Rationale:')
            answer = con[pos1+10:pos2]
            rotation = con[pos2+10:]
            
            saveQuestions(question,ans_a,ans_b,ans_c,ans_d,answer,rotation,1,1)
            return render_template("index.html", questions=[question,ans_a,ans_b,ans_c,ans_d,answer,rotation])
          

     return render_template("index.html")


@app.route('/questions')
def questions():
    #global cursor  # Use the global cursor

    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT * FROM notes")        
        data = cursor.fetchall()
    
        return render_template('questions.html', records=data)
    except Exception as e:
        return f"Error fetching records: {str(e)}"
    
if __name__ == "__main__":
    
    app.run(debug=True)
