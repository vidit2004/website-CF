import requests
import json
import sqlite3
from flask import Flask, render_template


connect = sqlite3.connect('data.db')

response = requests.get("https://codeforces.com/api/user.ratedList")

res = json.loads(response.text)

connect.execute("DROP TABLE IF EXISTS CF")
connect.execute('''CREATE TABLE CF
           (USERNAME VARCHAR PRIMARY KEY NOT NULL,
          RATING INT NOT NULL,
         RANKING VARCHAR NOT NULL);''')

for data in res["result"]:
    u = data["handle"]
    rat = data["rating"]
    ran = data["rank"]
    connect.execute("INSERT INTO CF (USERNAME,RATING,RANKING) VALUES(?,?,?)",(u,rat,ran))
connect.execute('''SELECT * FROM CF ORDER BY RATING DESC''')

#all_data = connect.execute('''SELECT * FROM CF''')
cur=connect.cursor()
all_data = cur.execute('''SELECT * FROM CF''')
rows = cur.fetchall()
result_list = [list(row) for row in rows]

connect.close()