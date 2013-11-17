from flask import *
from flask import Flask, render_template, request
import psycopg2  
import os
import urlparse
#import database

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/paint')
def paint():
    return render_template('paint.html')  

@app.route('/<filename>',methods=['POST'])
def save(filename=None):
    conn = psycopg2.connect(database='manimkv') 
    c=conn.cursor()
    c.execute("INSERT INTO savedimage (title,imagedata) VALUES (%s,%s)",[request.form['name'],request.form['data']])
    conn.commit()
    conn.close()
    c.close()
    return render_template('paint.html')

@app.route('/gallery')
def gallery():
    conn = psycopg2.connect(database='manimkv') 
    c=conn.cursor()
    c.execute("SELECT * FROM savedimage ORDER BY id desc")
    posts=[dict(id=i[0],title=i[1]) for i in c.fetchall()]

    print posts
    return render_template('gallery.html',posts=posts)

@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
    conn = psycopg2.connect(database='manimkv') 
    c=conn.cursor()	
    c.execute("SELECT * FROM savedimage WHERE title=%s",[filename])
    posts=[dict(id=i[0],title=i[1],imagedata=i[2]) for i in c.fetchall()]
    return render_template('imageload.html',posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
