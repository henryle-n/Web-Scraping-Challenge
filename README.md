# Welcome to The Red Planet ...  *MARS !*
## 1. Background

For over 30 years since the first human kind's close-up of this planet in 1965, Mars Exploration has never stopped being a top-trending topic. The more we look, the more interesting facts we found about this 4<sup>th</sup> planet from the Sun, such as "polar ice caps and clouds in its atmosphere, seasonal weather patterns, volcanoes, canyons and other recognizable features" (*mars.nasa.gov*).

In this project, a web application is built to scrape multiple websites for data related to NASA Mars Exploration Program. All scraped data is stored in a MongoDB table, queried, and displayed on a comprehensive single HTML page.  

<a class = "btn" href="./static/images/web_look.jpg"><span style = "color:blue">**Click here**</span>
</a> to see the final page image.<br>

<p align="center">
<img src="./static/images/demo.gif" alt="Mars out of range ... Waiting for satellite signal ..." max-height="50%" max-width="50%"><p>
  
<hr>

## 2. Languages, Tools &  Techniques
* Languges:
  * Python 3 | HTML 5 | CSS 3 | Markdown
* Python Platform & Modules:
  * Flask | Anaconda3 (Python 3.8) | Spinter (Chromedriver) | Beautiful Soup | Pandas | PyMongo | Jinja
* HTML Libraries:
  * Bootstrap
* noSQL Database:
  * MongoDB (<a href="https://www.mongodb.com/try/download/community">Installation Link</a>)
* Software/ Applications:
  * Jupyter Notebook | Visual Studio Code | Google Chrome v. 84 | Windows Terminal | Git Bash
* Operating System:
  * Windows 10 Pro v1909

## 3. Table of Contents

All files are stored in the folder and sub-folder of "Missions_to_Mars"

 **FOLDER NAME** | **CONTENTS** |
:----------------|:-------------|
**Chromedriver-v84** | Chrome Driver for Google Chrome ver. 84
**Jupyter Notebook** | `Mission_to_Mars.ipynb`, utilized during developement of `scrape_mars.py`
 **static** | contains _style.css_, and pictures of HTML background, readme & final website screenshot|
  **templates** | contains _'index.html'_, main home page |
 **application.py** | Flask App to drive the website |
 **get_mars_data.py** | queries from MongoDB & shows data on main page  data |
 **load_mongo_db.py** | calls for new web-scraping and loading data into MongoDB |
 **scrape_mars.py** | scraps the data and export new data into new table |
 **requirements.txt** | all libraries/ modules were used in this project |

## 4. Process Overview
### 4.1. Process at a Glance
For simplifying codes and easier debugging, the whole process was broken up into smaller processes and thus written in multiple Python Files. The below schematic decribes how all files are working together.  

<div align="center">
    <img src="./static/images/workflow.JPG"/>
</div>

* Green arrows indicate process when **Fetch New Data** button is clicked. 
* Orange arrows indicate how the data is retrieved, processed and displayed on the front-end. 

### 4.1. Creating the App
#### Step 1 - Preparation & Develop Jupyter Notebook
* Create new environment:
  * `conda create -n <name-of-env> python=3.8`
  * `conda activate <name-of-env>`
  * `pip install -r requirements.txt`
* Download Chrome Driver:
  * In the address bar type: `chrome://version/`, look for **Google Chrome** header indicating current Chrome version. 
  * For example: `Google Chrome	84.0.4147.105 (Official Build) (64-bit) (cohort: Stable)`
* Download correct version of Chrome Driver, <a href="https://chromedriver.chromium.org/">link here.</a>
* Websites visited for scraping:

 **WEBSITE** | **WEB ADDRESS** |
 :---------- |:---------- | 
 **Mars Latest News** | https://mars.nasa.gov/news |
 **JPL Mars Featured Space Images**| https://www.jpl.nasa.gov/spaceimages |
 **Mars Weather** | https://twitter.com/marswxreport |
 **Mars Facts** | https://space-facts.com/mars | 
 **Mars Hemispheres** | https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars | 

* Capture all scraped data into a dictionary.
* Exported the Jupyter Notebook file to a Python file named *scrap_mars.py*.

#### Step 2 - Build MongoDB Application 
File name: **load_mongo_db.py**
* Download and install MongoDB.
* Utilize PyMongo to establish the connection to MongoDB.
  * If there is server connection error, perform these steps:
    * Start -> Administrative Tools -> Services -> MongoDB.
    * Make sure MongoDB Server (MongoDB) Status is *Running*.
    * <a href="./static/images/start_db.jpg">Click here</a> for an image demo.
* Write the dictionary of all data (scrapped from _Step 1_) into MongoDB.

#### Step 3 - Build Data Query Application from MongoDB 
File name: **get_mars_data.py**
* Utilize PyMongo to establish the connection to MongoDB.
* Query data in MongoDB.
* Prepare to send data back to Flask App.

#### Step 4 - Build Flask App & Home Page
File names: **application.py** & **index.HTML**
* Build HTML template as the main webpage, formatted by CSS & Jinja codes embedded.
* Build different RESTful APIs:
  * Render **index.html**.
  * Connect with previous Python apps for querying data and post on **HTML** template by **Jinja**.


#### Step 5 - Start-up Procedure
* For the first time use, launch **load_mongo_db.py** to get some data for MongoDB and webpage.
* Open and run **application.py**.

## 5. Summary
* All data was successfully loaded into MongoDB. No significant issue occurs while web-scrapping.
* Pending on internet connection, several websites took a very long time to load or not loading at all. This caused errors or missing data as the website has not yet done redering & loading. Delay time was added to multiple places in program to allow browser to catch up.   
* Many nested **"if-elif-else"** were used to patch up issues associated with slow or invalid website to ensure application processed without hiccup. A better way to do it is utilized **"try / error"** block to lean codes and improve working speed.
