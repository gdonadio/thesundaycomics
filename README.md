<h1> thesundaycomics </h1>
<a href="https://thesundaycomics.onrender.com">thesundaycomics.onrender.com</a>

<h2>Synopsis</h2>
This project collects last Sunday's comic strips across the internet and places them on one webpage. The goal was to create an output that looks like the Sunday Comics page you'd find in a newspaper. I used Python to scrape to images from a list of webpages, place all the locations into .html code with a loop and then throw last Sunday's webpage online.

<h2>Files</h2>
<ul>
<li> <b>comiccode.py</b> - This code uses last Sunday's date and a list of comic webpages to find the image file for the last Sunday comic. A loop scrapes the webpages' source code, places the findings in a list, creates .html code with the list of images, and finally saves that code in an .html file. A Herokuapp timer runs this code daily at 4am. </li>

<li> <b>app_front.py</b> - This code runs whenever someone visits the website. The code opens the .html code and publishes that it for the world to enjoy.  </li>
</ul>

<h2>Author</h2>
Greg Donadio
<a href="https://github.com/gdonadio">github.com/gdonadio</a>


<h1> thesundaycomics </h1>
<a href="https://thesundaycomics.onrender.com">thesundaycomics.onrender.com</a>

<h2>Synopsis</h2>
This project collects last Sunday's comic strips from various syndicates and places them on a single webpage — just like the Sunday Comics section of a newspaper. It uses Python to scrape comic images from a list of websites, formats them into a clean HTML layout, and automatically publishes the result as a static webpage each week.

The site is now hosted as a free static site on Render, and the comic scraping + HTML generation is handled by GitHub Actions on a weekly schedule.

<h2>Files</h2>
<ul>
  <li><b>comiccode.py</b> – Scrapes image URLs from GoComics and ComicsKingdom for last Sunday’s comics, builds the HTML, and saves it as <code>output/index.html</code>.</li>

  <li><b>output/index.html</b> – The final rendered comic page, published at <a href="https://thesundaycomics.onrender.com">thesundaycomics.onrender.com</a>. Automatically updated by a GitHub Actions workflow.</li>

  <li><b>.github/workflows/update.yml</b> – GitHub Actions workflow that runs <code>comiccode.py</code> every Sunday morning and pushes the updated HTML to the repo for deployment.</li>
</ul>

<h2>Author</h2>
Greg Donadio  
<a href="https://github.com/gdonadio">github.com/gdonadio</a>
