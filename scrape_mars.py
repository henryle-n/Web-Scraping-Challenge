#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# ### Import Dependencies
import pandas as pd
# import pymongo as pmo
from bs4 import BeautifulSoup as bsp
from splinter import Browser
import time



 # specify parser used
lib_used = 'html.parser'

# ### Set-up Web Browser Driver for Scraping
def init_browser():
       # specify the path of browser driver want to use
    executable_path = {'executable_path': 'chromedriver.exe'}

    # specify the name of browser want to use
    browser_name = 'chrome' 

    # start browser
    browser = Browser(browser_name, **executable_path, headless=False)
    return browser



def scrape():
    # fire up the browser
    browser = init_browser()

    # ### NASA Mars News Web Scraping
    # link to NASA Mars news
    article_url = 'https://mars.nasa.gov/news/'

    # access & get content 
    browser.visit(article_url)

    t_wait = 0
    del_t = 0.25

    # condition to make sure the webpage is loaded
    if browser.is_element_present_by_tag('/html') == False:
        time.sleep(t_wait)
        t_wait += del_t
    else:
        pass

    soup = bsp(browser.html, lib_used)
    time.sleep(5)
    # return results
    results = soup.find_all('div', class_='list_text')
    

    # pull the lastest news from the list with index = 0 :: indication of the top latest
    latest_news = results[0]

    # workflow: 
        # find all the div, then use the unique class of each div  
        # to access the content of a specific div
    for tag in latest_news.find_all('div'):
        if "content_title" in tag.attrs["class"]:
            las_news_title = tag.a.text
            las_news_link = f"https://mars.nasa.gov/{tag.a['href']}"
        elif "article_teaser_body" in tag.attrs["class"]:
            las_news_content = tag.text
        
            
    # print out what found in the loop
    # place holder for debug later if somethig is wrong
    # print(f'>> Lastest news of Mars from NASA:\n    {las_news_title}\n\n>> News Content:\n    {las_news_content}\n\n>> News Link:\n    {las_news_link}')


    # ### JPL Mars Space Images - Featured Image Web Scraping


    # link to Mars Image
    ft_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # access website
    browser.visit(ft_img_url)

    t_wait = 0
    del_t = 0.25

    # condition to make sure the webpage is loaded
    while False:
        if browser.is_element_present_by_tag('/html') == False and t_wait <=t_out:
            time.sleep(t_wait)
            t_wait += del_t
            print('waiting for the website')
        
        else:
            break
        print('website loaded')


    # click on couple of buttons to gain access to the full size image page
    # condition with if to make sure the subsequent codes will still run incase of issue
    if browser.links.find_by_partial_text('FULL IMAGE'):
        browser.links.find_by_partial_text('FULL IMAGE').click()
        
    else:
        print(f'No "FULL IMAGE" Button found')
    
        
    if browser.links.find_by_partial_text('more info'):
        browser.links.find_by_partial_text('more info').click()
        
        # delay time so browser can load before proceeding
        time.sleep(2)
        
    else:
        print(f'No "more info" Button found')
            
    # condition with if to make sure the subsequent codes will still run incase of issue
    if browser.links.find_by_partial_href('largesize'):
        browser.links.find_by_partial_href('largesize').click()
        
    else:
        print(f'No "Full size Image " Button found')
        
    feature_image_url = browser.url
    feature_image_url


    # ### Mars Weather Web Scraping
    # link to Mars weather
    weather_url = 'https://twitter.com/marswxreport?lang=en'

    # access & get content 
    browser.visit(weather_url)
    time.sleep(5)
    t_wait = 0
    del_t = 0.25

    # condition to make sure the webpage is loaded
    if browser.is_element_present_by_tag('body') == False:
        time.sleep(t_wait)
        t_wait += del_t
    else:
        pass

    # create soup object
    soup = bsp(browser.html, lib_used)
      

    # return results
    results = soup.find_all('span', class_='css-901oao')
    time.sleep(5)   

    # loop thru the list and find partial match for the weather content
    # as soon as the first string read, stop the loop
    mars_weather = ""
    for ea_tag in results:
        if "insight" and "sol" and "low" and " high" in ea_tag.text.lower():
            mars_weather = ea_tag.text
            print(ea_tag)
            break
        else:
            pass
    mars_weather


    # ### Mars Facts
    # link to Mars weather
    facts_url = 'https://space-facts.com/mars/'

    # access & get content 
    browser.visit(facts_url)
    time.sleep(3)   
    tables = pd.read_html(facts_url)
    tables[0]
    df = tables[0]
    df.columns = ["Description", "Value"]
    # df.set_index("Description", inplace=True)

    mars_info_table = df.to_html(classes="table table-striped", index = False)
    mars_info_table.replace("\n", "")

    df.to_html('mars_info_table.html')


    # ### Mars Hemispheres
    # create function to process webpage and retrieve hemisphere images of Mars

    def get_hemi_img(brwr, hemi_url, hemi_name):
        
        # since browser will take sometime to load,
        # create timer to delay the process and wait for chrome to load page
        # set wait time parameters
        t_wait = 0
        t_out = 3
        del_t = 1
        
        # access & get content by soup object
        browser.visit(hemi_url)
        soup = bsp(browser.html, lib_used)
        
        print(">> Progress = 10%")
        
        # condition to make sure the webpage is loaded
        if browser.is_element_present_by_tag('/html') == False:
            while t_wait <= (t_out-7):
                time.sleep(t_wait)
                t_wait += del_t
                continue
        else:
            pass

        print(">> Progress = 30%")
        
        # click on couple of buttons to gain access to the full size image page
        # condition with if to make sure the subsequent codes will still run incase of issue
        t_wait = 0

        if brwr.links.find_by_partial_text(hemi_name):
            brwr.links.find_by_partial_text(hemi_name).click()
            
            # condition to make sure the webpage is loaded
            print(">> Progress = 50%")
            if brwr.is_element_present_by_tag('/html') == False:
                if t_wait <= t_out:
                    time.sleep(t_wait)
                    t_wait += del_t
                
                else:
                    print("Page takes too long to load!")
                    
                
    
        else:
            t_wait = 0
            if t_wait <= t_out and not brwr.links.find_by_partial_text(hemi_name):
                    time.sleep(t_wait)
                    if brwr.links.find_by_partial_text(hemi_name):
                        brwr.links.find_by_partial_text(hemi_name).click()
                        
                    else:
                        t_wait += del_t
                        
            else:    
                print(f"Time out! Unable to find {hemi_name} Hemisphere Image")
                print("Page takes too long to load!")
                    
            
        
        print(">> Progress = 60%")
        # create soup object
        time.sleep(2)
        soup = bsp(browser.html, lib_used)
        time.sleep(2)
        
        # return results
        results = soup.find_all('ul', class_='')
        time.sleep(4)
        t_wait = 0
        
        if not results and t_wait <= t_out:
            time.sleep(t_wait)
            results = soup.find_all('ul', class_='')
            t_wait += del_t
        else:
            print("Time out!")
            
        
        print(">> Progress = 70%")
        
        # loop to find the tag a and href of the full size image
        try:
            for rsl in results[0].find_all('a'):
                if rsl.attrs["href"] and (rsl.text).lower() == "sample":
                    print('Getting Image Link')
                    img_link = rsl['href']
                    print('Getting Image Title')
                    img_title = hemi_name + ' Hemisphere'
        except Exception:
            print(f"Unable to process {hemi_name} Hemisphere Data")
            img_link = "Unable to get link"
            img_title = hemi_name + 'Hemisphere'
        print(">> Progress = 100%")
        return (img_title, img_link)

    # link to Mars hemisphere pics
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemi_name = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']

    # get the list of dictionary of all hemisphere image info
    hemisphere_image_urls = []

    for name in hemi_name:
        print(f'>> Processing data of {name} Hemisphere')
        print(f'>> Please wait ...')
        answer = get_hemi_img(browser, hemi_url, name)
        dict_each_hemi = {"title": answer[0] , "img_url": answer[1]}
        hemisphere_image_urls.append(dict_each_hemi)
        print(f'>> Finish with {name} Hemisphere\n{("-")*25}')
    
    # review data
    hemisphere_image_urls

   
    # ## Summary of all Scraped Data
    print(("=")*35, "START", ("=")*35)
    print(las_news_title, "\n", ("-")*50)
    print(las_news_content, "\n", ("-")*50)
    print(las_news_link, "\n", ("-")*50)
    print (feature_image_url, "\n", ("-")*50)
    print (mars_weather, "\n", ("-")*50)
    print(hemisphere_image_urls, "\n", ("-")*50)
    print(" >>> Closing Browser...", "\n", ("-")*50)
    try:
        browser.quit()
    except Exception:
        pass
    print(" >>> Browser Closed...", "\n", ("-")*50)
    print(("=")*35, "END", ("=")*35)

    mars_db = {
        "news_title" : las_news_title,
        "news_content" : las_news_content,
        "news_link" : las_news_link,
        "mars_facts" : mars_info_table,
        "feature_img_url" : feature_image_url,
        "mars_weather" : mars_weather,
        "hemisphere_img_url" : hemisphere_image_urls
        }

    return mars_db

# test and verify data is pulling in correctly
if __name__ == "__main__":
    print("\nVerifying Retrieved Data\n")
    print(scrape())
    print("\nProcess Complete!\n")
