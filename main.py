from django.shortcuts import redirect
from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
@app.route('/')
def student():
    return  render_template('index_new.html')
@app.route('/result', methods=['GET', 'POST'])
def index():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="first"
    )
    cur = mydb.cursor()
    if request.method == 'POST':
         # Fetch form data
        userDetails=request.form
        name = userDetails['name']
        email = userDetails['email']
        password = userDetails['password']
        # cur = mydb.cursor()
        cur.execute("INSERT INTO first (name,email,password) VALUES ('"+name+"','"+email+"','"+password+"')")
        mydb.commit()
        cur.close()
        return "Thanks for registration. "
    return redirect('/')
app.run(debug=True)
