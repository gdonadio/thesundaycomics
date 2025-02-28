# app_front.py 
# The get_latest_comic() function code runs everytime someone visits the website. 
# comiccode.py runs the comic code that creates the html code. 
# comiccode.py is run 4AM every day and uploads the images from the last Sunday.

import os
import urllib.parse as up
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_latest_comic():
    """Fetch the latest HTML from the database on each request."""
    up.uses_netloc.append("postgres")
    url = up.urlparse(os.environ["DATABASE_URL"])
    
    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
    cursor = conn.cursor()
    
    # Get the latest Sunday's comic
    cursor.execute("SELECT code FROM comicDB ORDER BY date DESC LIMIT 1")
    htmlcode = cursor.fetchone()

    cursor.close()
    conn.close()

    return htmlcode[0] if htmlcode else "<h1>No comic found for this week.</h1>"

@app.route("/")
def showpage():
    return get_latest_comic()  # Always fetch fresh data on each request

if __name__ == "__main__":
    app.run()
