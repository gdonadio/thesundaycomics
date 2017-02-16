<h1> thesundaycomics </h1>
<a href="http://thesundaycomics.herokuapp.com">thesundaycomics.herokuapp.com</a>

<h2>Synopsis</h2>
This project collects last Sunday's comic strips across the internet and places them on one webpage. The goal was to create an output that looks like the Sunday Comics page you'd find in a newspaper. I used Python to scrape to images from a list of webpages, place all the locations into .html code with a loop, upload that code into a Heroku PostgreSQL database, and then throw last Sunday's webpage online.

<h2>Files</h2>
<ul>
<li> <b>comiccode.py</b> - This code uses last Sunday's date and a list of comic webpages to find the image file for the last Sunday comic. A loop scrapes the webpages' source code, places the findings in a list, creates .html code with the list of images, and finally saves that code into a PostgreSQL database in a cell next to that Sunday's date. A Herokuapp timer runs this code daily at 4am. </li>

<li> <b>app_front.py</b> - This code runs whenever someone visits the website. The code opens the PostgreSQL database mentioned above, takes the .html code that's stored in the cell adjacent to last Sunday's date, and publishes that .html code for the world to enjoy.  </li>
</ul>

<h2>Author</h2>
Greg Donadio
<a href="https://github.com/gdonadio">github.com/gdonadio</a>
