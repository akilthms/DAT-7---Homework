# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:37:57 2015

@author: akilthomas
"""
import requests 
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd 
#Created a dictionary using default dict so we can add the info to the dict. 
def movie_info(ID):
   dct = defaultdict(str)
   #Construct the URL with the variable id
   url = 'http://www.imdb.com/title/'+ID+'/'
   #Get the html from the url 
   html = requests.get(url)
   info = html.text
   b = BeautifulSoup(info)
   
   #use the beatiful soup library to get the information we need from the corresponding webpage
   title = b.find(name = "h1").find(name = 'span', attrs = {'itemprop': 'name', 'class': 'itemprop'}).text
   star_rating = b.find(name = 'div', attrs={'class': 'titlePageSprite star-box-giga-star'}).text
   description = b.find(name = 'td', attrs = {'id':'overview-top'}).find('p', attrs={'itemprop':'description'}).text
   content_rating = b.find(name = 'div', attrs={'class':'infobar'}).find(name = 'meta', attrs = {"itemprop":"contentRating"})['content']
   duration = int(b.find(name = 'time', attrs = {'itemprop':'duration'})['datetime'][2:-1])
   
   key = ['title', 'star_rating','description', 'content_rating', 'duration']
   value = [title,star_rating,description,content_rating, duration]
   #Construct our dictionary and then return it
   for i in range(0, len(key)):
       dct[key[i]] = value[i]
   return dct

#open our text file which holds the ids to be used in our function.
with open('/Users/akilthomas/Desktop/DAT7/data/imdb_ids.txt','rU') as f:
    movie_titles = f.read()
    #Use the .split method to create an array of ids
    movie_titles = movie_titles.split()
#Use a list comprehension and our function to create a list of dictionaries with the corresponding information
data = [movie_info(title) for title in movie_titles]
      

#place our list of dictionaries in a dataframe
df = pd.DataFrame(data)  
    
