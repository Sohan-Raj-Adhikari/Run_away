from flask import Flask, render_template, g, request, redirect, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import helpers
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.secret_key = 'Haaland'

@app.route("/", methods=["GET","POST"])
def index():
    curr_theme = session.get('theme', 'light')
    if not session.get('user_id'):
        return render_template("intro.html", theme=curr_theme)
    return render_template("index.html", theme=curr_theme)

@app.route("/theme")
def theme():
    session['theme'] = 'dark' if session.get('theme') == 'light' else 'dark'
    return redirect('/')

@app.route("/retrieve")
def retrieve():
    if not session.get('user_id'):
        error = {"error":"not logged in"}
        return jsonify(error)
    db = helpers.getdb()
    cursor = db.execute("SELECT distance, duration, date, note FROM runs WHERE user_id = ?", (session.get('user_id'), ))
    rows = cursor.fetchall()
    if not rows:
        return jsonify({"error" : "database failure"})
    column_names = [column[0] for column in cursor.description]
    newrows = [dict(zip(column_names, row)) for row in rows]
    return jsonify(newrows)

@app.route("/record", methods=["GET","POST"])
def record():
    if not session.get('user_id'):
        return redirect("/login")
    if request.method == "POST":
        distance = request.form.get('distance', type=float)
        minutes = request.form.get('minutes', type=int)
        hours = request.form.get('hours', type = int)
        seconds = request.form.get('seconds', type= int)
        notes = request.form.get('notes')
        date = request.form.get('date')
        db = helpers.getdb()
        if not distance and minutes and hours and seconds:
            return render_template("error.html", message="invalid paramenters")
        elif hours == 0 and minutes == 0:
            return render_template("error.html", message="Time cannot be less than 1 minute.")
        elif date > str(datetime.now().date):
            return render_template("error.html", message="Date can't be in the future.")
        else:
            if hours == 0:
                duration = minutes * 60 + seconds
            elif minutes == 0 and hours!=0:
                duration = hours * 60 * 60 + seconds
            else:
                duration = hours * 60 * 60 + minutes * 60 + seconds
            cursor = db.execute("INSERT INTO runs(user_id, distance, duration, date, note) VALUES (?,?,?,?,?)", (session["user_id"], distance, duration, date, notes))
            db.commit()
            return redirect("/")
    else:
        return render_template("error.html", message="Some unforceen error occured.")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        pswrd = request.form.get('password')
        confirmar = request.form.get('confirmation')
        db = helpers.getdb()
        if pswrd == confirmar and name != " ":
            cur = db.execute("SELECT * FROM users WHERE user_name = ?", (name,))
            if cur.fetchone():
                return render_template('error.html', message='Unique username needed.')
            cursor = db.execute("INSERT INTO users(user_name, hash) VALUES(?,?)", (name, generate_password_hash(confirmar)))
            db.commit()
            return redirect("/login")
        else:
            return render_template('error.html', message="Passwords need to be same")
    return render_template('register.html', theme=session.get('theme', 'light'))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        pswrd = request.form.get('password')
        db = helpers.getdb()
        rows = db.execute("SELECT * FROM users WHERE user_name = ?", (name, )).fetchone()
        if not rows:
            return render_template('error.html', message='invalid username')
        if check_password_hash(rows['hash'], pswrd):
            session['user_id'] = rows['id']
            return redirect("/")   
        else:
            return render_template('error.html', message="Password and username don't match.")
    return render_template('login.html', theme=session.get('theme', 'light'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.teardown_appcontext
def closedb(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
