from flask import Flask, render_template, redirect, url_for
import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS  usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_usu TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
""")
conexion.commit()
conexion.close


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/endesarrollo")
def endesarrollo():
    return render_template("endesarrollo.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)