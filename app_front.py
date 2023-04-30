# app_front.py 
# This Python code runs everytime someone visits the website. 
# comiccode.py runs the comic code that creates the html code. 
# comiccode.py is run 4AM every day and uploads the images from the last Sunday.

import re
from flask import Flask 
app = Flask(__name__)

with open('index.html') as f:
    thisweekscode = f.read()

@app.route("/")
def showpage():
	return thisweekscode
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)