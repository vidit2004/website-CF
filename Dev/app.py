from flask import Flask, render_template
from Database import result_list
import sqlite3

#connect = sqlite3.connect('data.db')


app = Flask(__name__)

@app.route("/")
def ratings():
    return render_template('home.html',List1=result_list)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)

#connect.close()