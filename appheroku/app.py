from flask import Flask
from datetime import datetime
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psycopg2.extras

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='HOSTNAME',
        database='DATABASE URI',
        user='USERNAME',
        password='PASSWORD')
    return conn

@app.route("/classement/attaque/")
@app.route("/classement/")
def classement_atk():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        select_stats = 'SELECT username,attaque,pv,ChapterNm,ChapterHm FROM Stats ORDER BY attaque DESC;'
        cur.execute(select_stats)
        displayDB = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('displaydb.html', data=displayDB)

@app.route("/classement/pv/")
def classement_pv():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        select_stats = 'SELECT username,attaque,pv,ChapterNm,ChapterHm FROM Stats ORDER BY pv DESC;'
        cur.execute(select_stats)
        displayDB = cur.fetchall()
        cur.close()
        conn.close()
        compteur = len(displayDB)
        return render_template('displaydb.html', data=displayDB, heading=heading, compteur=compteur)

@app.route("/")
def home(name = None):
    return render_template(
        "home.html",
        name=name,
        date=datetime.now()
    )

@app.route("/tuto-classement/")
def aboutme(name=None):
    return render_template(
        "tuto-classement.html",
        name=name,
        date=datetime.now()
    )


if __name__ == '__main__':
    app.run(threaded=True)
