# Welcome to The Red Planet ...  *MARS !*

## Background

For over 30 years since the first human kind's close-up of this planet in 1965, Mars Exploration has never stopped being a top-trending topic for not only scientists but also for general population all around the world. The more we look, the more interesting facts we found about this 4<sup>th</sup> planet from the Sun, such as "polar ice caps and clouds in its atmosphere, seasonal weather patterns, volcanoes, canyons and other recognizable features" (*mars.nasa.gov*).

In this project, a web application is built to scrape multiple websites for data related to NASA Mars Exploration Program. All scraped data is stored in a MongoDB table, queried, and displayed on a comprehensive single HTML page.  

**NOTE:** The main folder is ```Mission_to_Mars```

<a class = "btn" href="Missions_to_Mars/static/web_look.jpg"><span style = "color:blue">**Click here**</span>
</a> to see the final page image.<br>

<p align="center">
<img src="Missions_to_Mars/static/jumbotron_background.jpg" alt="Mars out of range ... Waiting for satellite signal ..." max-height="50%" max-width="50%"><p>
  
<hr>

## OS / Tools / Techniques / Modules
* Python | HTML5 / CSS3 | Markdown
* Flask | Bootstrap | Spinter | ChromeDriver | Beautiful Soup | Pandas
* PyMongo | MongoDB | Jupyter Notebook | Git
* Google Chrome, ver. 84 | GitBash Terminal
* Windows 10 Pro, ver. 1909 OS Build 18363.778

## Process Overview

### Step 1 - Build Jupyter Notebook  ( *mission_to_mars.ipynb* )
* Develop source codes for scraping data ultilizing various Python modules
* Websites visited for scraping:
| | | |
|-|-|-|
| **Mars Latest News** | https://mars.nasa.gov/news 
| **JPL Mars Featured Space Images**| https://www.jpl.nasa.gov/spaceimages 
| **Mars Weather** | https://twitter.com/marswxreport
| **Mars Facts** | https://space-facts.com/mars
| **Mars Hemispheres** | https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars  

    * **Mars Latest News** :: https://mars.nasa.gov/news
    * **JPL Mars Featured Space Images** :: https://www.jpl.nasa.gov/spaceimages/
    * **Mars Weather** :: https://twitter.com/marswxreport
    * **Mars Facts** :: https://space-facts.com/mars/
    * **Mars Hemispheres** :: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

* Capture all scraped data into a dictionary
* Exported the Jupyter Notebook file to a Python file named *scrap_mars.py*

### Step 2 - Build MongoDB Application ( *load_mongo_db.py* )
* Utilize PyMongo to establish the connection to MongoDB
* Write the dictionary of all data (in _Step 1_) into MongoDB

### Step 3 - Build Get Data Application ( *get_mars_data.py* )
* Utilize PyMongo to establish the connection to MongoDB
* Query current data in MongoDB store in memory
* Prepare to send to main python app and HTML

### Step 4 - Build Flask / HTML Application( *application.py* / *index.HTML* )
* Build HTML template contains content layout / format
* Build different ***@route*** to connect with previous python app for querying on the existing data or scraping for new data, then render all data into an HTML template


### Step 5 - Start-up Procedure
* For first time use, launch **load_mongo_db.py** to load the first time dataset
* Open and run **application.py** to pull data from MongoDB, render data with HTML as a template


## Table of Content
All files are stored in the folder and sub-folder of "Missions_to_Mars"

* **static** :: folder contains _style.css_ which is a CSS format file, and other pictures of HTML background, etc.
*  **templates** :: contains _'index.html'_ which is the template for displaying data on the web
* **_Mission_t0_Mars.ipynb_** :: original jupyter notebook for developing program
* **application.py**application.py :: exported / converted from the jupyter notebook
* **get_mars_data.py** :: query & show on HTML file any existing MongoDB data
* **load_mongo_db.py** :: file to call for new web scaping and loading data into MongoDB
* **scrape_mars.py** :: scraping codes to scrap the data and export new data into new table

## Summary
* All data was successfully load / query into MongoDB, no significant event occurs
* Three python files were built to split the codes into easier to read, troubleshoot, test, etc. when problems occur 
* The challenging part is writing CSS file to work with Flask & HTML
* Pending on internet connection, several websites took a very long time to load or not loading at all. This causes errors or missing data as the website has not yet done redering  HTML / CSS files   
* Many nested **"if-elif-else"** were used to path up issues associated with slow or invalid website to ensure application processed without hiccup. A better way to do it is utilized **"try / error"** block to lean codes and improve working speed 

