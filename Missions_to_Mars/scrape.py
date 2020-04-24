#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# ### Import Dependencies

# In[24]:


import pandas as pd
# import pymongo as pmo
from bs4 import BeautifulSoup as bsp
from splinter import Browser
import time
import os
import os.path
from os import path


# ### Set-up Web Browser Driver for Scraping

# In[2]:
def scrape():

    # specify the path of browser driver want to use
    executable_path = {'executable_path': 'chromedriver.exe'}

    # specify the name of browser want to use
    browser_name = 'chrome'

    # specify parser used
    lib_used = 'html.parser'

    # start browser
    browser = Browser(browser_name, **executable_path, headless=False)


    # ### NASA Mars News Web Scraping

    # In[3]:


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

    # return results
    results = soup.find_all('div', class_='list_text')
    results


    # In[4]:


    # pull the lastest news from the list with index = 0 :: indication of the top latest
    latest_news = results[0]
    latest_news


    # In[5]:


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
    print(f'>> Lastest news of Mars from NASA:\n    {las_news_title}\n\n>> News Content:\n    {las_news_content}\n\n>> News Link:\n    {las_news_link}')


    # ### JPL Mars Space Images - Featured Image Web Scraping

    # In[6]:


    # link to Mars Image
    ft_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # access website
    browser.visit(ft_img_url)

    t_wait = 0
    del_t = 0.25

    # condition to make sure the webpage is loaded
    if browser.is_element_present_by_tag('/html') == False:
        time.sleep(t_wait)
        t_wait += del_t
    else:
        pass


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

    # In[7]:


    # link to Mars weather
    weather_url = 'https://twitter.com/marswxreport?lang=en'

    # access & get content 
    browser.visit(weather_url)

    t_wait = 0
    del_t = 0.25

    # condition to make sure the webpage is loaded
    if browser.is_element_present_by_tag('/html') == False:
        time.sleep(t_wait)
        t_wait += del_t
    else:
        pass

    # create soup object
    soup = bsp(browser.html, lib_used)
    print(soup)

    # return results
    results = soup.find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    results


    # In[8]:


    # loop thru the list and find partial match for the weather content
    # as soon as the first string read, stop the loop
    for ea_tag in results:
        if ea_tag.text[0:7] == "InSight":
            mars_weather = ea_tag.text
            break
    mars_weather


    # ### Mars Facts

    # In[9]:


    # link to Mars weather
    facts_url = 'https://space-facts.com/mars/'

    # access & get content 
    browser.visit(facts_url)
    time.sleep(3)   
    # soup = bsp(browser.html, lib_used)



    # return results
    # results = soup.find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    # results


    # In[10]:


    tables = pd.read_html(facts_url)
    tables[0]
    df = tables[0]
    df.columns = ["Description", "Value"]
    df


    # In[11]:


    mars_info_table = df.to_html(index=False)
    mars_info_table.replace("\n", "")


    # In[12]:


    df.to_html('mars_info_table.html')


    # ### Mars Hemispheres

    # In[13]:


    # create function to process webpage and retrieve hemisphere images of Mars

    def get_hemi_img(brwr, hemi_url, hemi_name):
        
        # since browser will take sometime to load,
        # create timer to delay the process and wait for chrome to load page
        # set wait time parameters
        t_wait = 0
        t_out = 10
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
        time.sleep(3)
        soup = bsp(browser.html, lib_used)
        time.sleep(4)
        
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


    # In[14]:


    # link to Mars hemisphere pics
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemi_name = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']


    # In[15]:


    # get the list of dictionary of all hemisphere image info
    hemisphere_image_urls = []

    for name in hemi_name:
        print(f'>> Processing data of {name} Hemisphere')
        print(f'>> Please wait ...')
        answer = get_hemi_img(browser, hemi_url, name)
        dict_each_hemi = {"title": answer[0] , "img_url": answer[1]}
        hemisphere_image_urls.append(dict_each_hemi)
        print(f'>> Finish with {name} Hemisphere\n{("-")*25}')


    # In[16]:
    hemisphere_image_urls

    # pd.DataFrame(hemisphere_image_urls)


    # ## Summary of all Scraped Data

    # In[17]:


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
        "feature_img_url" : feature_image_url,
        "mars_weather" : mars_weather,
        "hemisphere_img_url" : hemisphere_image_urls
        }

    return mars_db
