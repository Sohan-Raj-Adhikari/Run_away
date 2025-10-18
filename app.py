from flask import Flask, render_template, g, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import helpers

app = Flask(__name__)
app.debug = True
app.secret_key = 'Haaland'

@app.route("/")
def index():
    if not session.get('user_id'):
        return redirect("/login")
    return render_template('index.html')

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        pswrd = request.form.get('password')
        confirmar = request.form.get('confirmation')
        db = helpers.getdb()
        if pswrd == confirmar:
            cur = db.execute("SELECT * FROM users WHERE user_name = ?", (name,))
            if cur.fetchone():
                return render_template('error.html', message='Unique username needed.')
            cursor = db.execute("INSERT INTO users(user_name, hash) VALUES(?,?)", (name, generate_password_hash(confirmar)))
            db.commit()
            return redirect("/login")
        else:
            return render_template('error.html', message="Passwords need to be same")
    return render_template('register.html')

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
    return render_template('login.html')

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
