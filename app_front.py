# app_front.py 
# This Python code runs everytime someone visits the website. 
# comiccode.py runs the comic code that uploades the html code to Heroku's postgresql server. 
# comiccode.py is run 4AM every day and uploads the images from the last Sunday.

import re
import glob
import os
from flask import Flask 
app = Flask(__name__)


from datetime import date
today = date.today().toordinal()
prevsunday = today - (today % 7)
sundaydate = date.fromordinal(prevsunday)
kingdate = sundaydate.strftime("%Y-%m-%d")


TSC_DB = os.environ.get('TSC_DB')
TSC_USER = os.environ.get('TSC_USER')
TSC_SECRET = os.environ.get('TSC_SECRET')
TSC_HOST = os.environ.get('TSC_HOST')
TSC_PORT = os.environ.get('TSC_PORT')

import psycopg2	
cnxn = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (TSC_DB,TSC_USER,TSC_SECRET,TSC_HOST,TSC_PORT))
cursor = cnxn.cursor()
cursor.execute("SELECT DISTINCT n.CODE FROM comicDB AS n WHERE DATE = (%s)", (kingdate, ) )
dt = cursor.fetchall()
thisweekscode= dt[0][0]	


@app.route("/")
def showpage():
	return thisweekscode
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)