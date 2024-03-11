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

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        question = request.form.get("question")
        answers = request.form.get("answers")
        rotation = request.form.get("rotation")
        if question:
            save_note_to_db(question,answers,rotation)
            return redirect(url_for("add"))

    return render_template("index.html")

def save_note_to_db(question, answers, rotation):
    try:
        insert_query = "INSERT INTO notes (question, answers, rotation,correct) VALUES (%s, %s, %s,1)"
        cursor.execute(insert_query, (question, answers, rotation))
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

if __name__ == "__main__":
    app.run(debug=True)
