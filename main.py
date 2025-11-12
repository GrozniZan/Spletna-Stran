from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/homepage/<ime_podjetja>")
def hello_world(ime_podjetja):
    return render_template("main.html", ime_podjetja=ime_podjetja)

@app.route("/form/")
def test():
    return render_template("form_test.html")

@app.route("/form-submit/")
def handle_form():
    
    uporabniško_ime = request.args.get("username")
    geslo = request.args.get("password")
    print(uporabniško_ime, geslo)
    select_usr = 'select * from contacts where first_name ="'+uporabniško_ime+'" and last_name="'+geslo+'";'
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(select_usr)
    ls = cursor.fetchall()
    if len(ls) > 0:
        return "Prijava uspela"
    else:
        return"Napačno uporabniško ime ali geslo"
    

@app.route('/view_db/')
def view_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("select * from contacts;")
    return cursor.fetchall()

@app.route('/reg-test/')
def registracija():
    return render_template("registracija.html")

@app.route("/registracija-submit/")
def registracija_submit():
    uporabnisko_ime = request.args.get("username")
    geslo = request.args.get("password")
    print(uporabnisko_ime, geslo)

    insert_command = 'INSERT INTO contacts (first_name, last_name) VALUES("'+uporabnisko_ime+'", "'+geslo+'");'
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(insert_command)
    conn.commit()

    return "V izdelavi"


app.run(debug=True)
