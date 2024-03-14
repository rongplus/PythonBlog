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

@app.route("/query", methods=["GET", "POST"])
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(buffered=True)

    if request.method == "POST":
        next_button = request.form.get("next_button")
        if next_button:
            record = cursor.fetchone()
            if record:
                return render_template("index.html", note=record[1])
            else:
                return "No more records."

    cursor.execute("SELECT * FROM notes")
    record = cursor.fetchone()
    conn.close()

    return render_template("question.html", note=record[1])

if __name__ == "__main__":
    app.run(debug=True)
