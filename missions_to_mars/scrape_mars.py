#!/usr/bin/env python
# coding: utf-8

# In[22]:


from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[23]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[24]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[25]:


titles = soup.find_all('div', class_="content_title")
paragraphs = soup.find_all('div', class_="rollover_description_inner")
#done with titles


# In[26]:


url = 'https://spaceimages-mars.com/'
browser.visit(url)
response = requests.get(url)
soup = bs(browser.html, 'html.parser')


# In[27]:


featured_image_url = soup.find('img', class_='headerimage fade-in')
featured_image_url = url + featured_image_url['src']
#done with pics


# In[28]:


url = "https://galaxyfacts-mars.com/"
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[49]:


table = pd.read_html(url)
table


# In[50]:


df = table[0]
df.columns = ['Stat', 'Mars', 'delete']
del df['delete']
df = df.drop(labels=0, axis=0)
df


# In[72]:


df2= table[1]
df2.columns=['Stat', 'Mars']
df2


# In[78]:


dfs = [df, df2]
dfs = pd.concat(dfs,ignore_index=True)
dfs


# In[81]:


facts=dfs.to_dict("records")
#donewithfacts


# In[88]:


url = 'https://marshemispheres.com'
browser.visit(url)
response = requests.get(url)
soup = bs(response.text, "html.parser")


# In[89]:


soup = soup.find_all('div', class_='item')


# In[92]:


hem_urls=[]

for x in soup:
    
    #using soup grab title 
    title= x.h3.text
    #find  page with image
    links= x.find("a", class_="itemLink product-item")['href']
    browser.visit(f"https://marshemispheres.com/{links}")
    #find the link
    img_url = browser.find_by_text('Sample')['href']
    #append to dict
    hem_urls.append({'title': title, 'img_url': img_url})

print (hem_urls)



# In[98]:


mars_data = {
        "titles": titles,
        "paragraphs": paragraphs,
        "featured_image_url": featured_image_url,
        "facts": facts,
        "hem_urls": hem_urls
        }


# In[99]:





# In[ ]:




