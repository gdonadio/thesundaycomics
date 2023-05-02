# app_front.py 
# This Python code runs everytime someone visits the website. 
# comiccode.py runs the comic code that creates the html code. 
# comiccode.py is run 4AM every day and uploads the images from the last Sunday.

import os
import urllib.parse as up
import psycopg2

import re
from flask import Flask 
app = Flask(__name__)

from datetime import date
today = date.today().toordinal()
prevsunday = today - (today % 7)
sundaydate = date.fromordinal(prevsunday)
kingdate = sundaydate.strftime("%Y-%m-%d")

up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
                    user=url.username,
                    password=url.password,
                    host=url.hostname,
                    port=url.port
                    )
cursor = conn.cursor()
cursor.execute("select distinct a.code from comicDB a where a.date = '{}'".format(kingdate) )
htmlcode = cursor.fetchall()

@app.route("/")
def showpage():
    return htmlcode[0][0]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
