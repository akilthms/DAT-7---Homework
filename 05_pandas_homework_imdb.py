# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:25:44 2015

@author: akilthomas
"""

import pandas as pd 
import matplotlib.pyplot as plt


movies = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT7/master/data/imdb_1000.csv')

#Number of rows
movies.shape[0]
#Number of columns
movies.shape[1]

#Use a for loop to print out type of each column
for col in movies.columns:
    print type(col)

#Output
#==============================================================================
# <type 'str'>
# <type 'str'>
# <type 'str'>
# <type 'str'>
# <type 'str'>
# <type 'str'>
#==============================================================================
#Actually after review there is a DataFrame method to do this
movies.dtypes
#Output
#==============================================================================
# star_rating       float64
# title              object
# content_rating     object
# genre              object
# duration            int64
# actors_list        object
# dtype: object
#==============================================================================

movies.duration.mean()
#120.97957099080695

movies.sort('duration')
#By default the sort method sorts ascending. We find that 'Freaks' is the shortest movie

movies.sort('duration', ascending = False)

#By setting ascending = False we can find the longest movie. Which is hamlet.

#A more concise command to get the answers we wanted would the following below. At this point not sure how to display only one record without using head
movies.sort('duration').head(1)
movies.sort('duration', ascending = False).head(1)

movies.duration.plot(kind = 'hist', bins = 20)

movies.duration.plot(kind = 'box')

movies.content_rating.value_counts()
#==============================================================================
# R            460
# PG-13        189
# PG           123
# NOT RATED     65
# APPROVED      47
# UNRATED       38
# G             32
# PASSED         7
# NC-17          7
# X              4
# GP             3
# TV-MA          1
#==============================================================================


movies.content_rating.value_counts().plot(kind ='bar')
plt.xlabel('Content Ratings')
plt.ylabel('Frequency')

movies.content_rating.map({'NOT RATED':'UNRATED', 'APPROVED':'UNRATED', 'PASSED':'UNRATED', 'GP':'UNRATED'})

movies.content_rating.replace('NOT RATED','UNRATED', inplace=True)
movies.content_rating.replace('APPROVED','UNRATED', inplace=True)
movies.content_rating.replace('PASSED','UNRATED', inplace=True)
movies.content_rating.replace('GP','UNRATED', inplace=True)


movies.content_rating.replace('X','NC-17', inplace=True)
movies.content_rating.replace('TV-MA','NC-17', inplace=True)

#Create a for loop interating through the columns and call .isnull.sum()

for col in movies.columns:
    print movies[col].isnull().sum()

# The content_ratings column has the only missing vaules with a number of 3
print movies.iloc[:,2].isnull().sum()

#First attempt at examining missing values, printing the row where missing then replacing all values with NA
#==============================================================================
# for col in movies.columns:
#     print movies[col].isnull().sum()
#     if movies[col].isnull().sum() > 0:
#         missing = movies[col].isnull()
#         #This loop "examines all missing values" 
#         for row in missing:
#             if row ==True:
#                 print movies[col]
#     #After we review them all we use the fillna method to replace them with NA
#     movies[col].fillna(value ='NA', inplace= True)
#==============================================================================
    
 #Replaces all missing values with NA
movies[col].fillna(value ='NA', inplace= True)

movies[movies.duration >= 120].star_rating.mean()
#Average star rating for movies over 2 hours is 7.95

movies[movies.duration < 120].star_rating.mean()
#Average star rating for movies over 2 hours is 7.84

#Use a scatter plot to find relationship between two numerical values
movies.plot(kind='scatter', x='duration', y='star_rating')
#It seems that two hours is the cut off point. Star raitings increase as duration increase
#but only upto two hours. Then the ratings begin to fall



movies.groupby('content_rating').duration.mean()
#==============================================================================
# content_rating
# G                 112.343750
# NA                132.000000
# NC-17             116.250000
# PG                115.300813
# PG-13             127.195767
# R                 122.163043
# UNRATED           116.475000
#==============================================================================

#Visualize relationship between duration and content rating
movies.boxplot(column='duration', by='content_rating')
movies.duration.hist(by=movies.content_rating, sharex=True)

movies.groupby('content_rating').star_rating.max()
#==============================================================================
# content_rating
# G                 8.6
# NA                8.2
# NC-17             8.4
# PG                8.8
# PG-13             9.0
# R                 9.3
# UNRATED           8.9
#==============================================================================

#Code can be much much simpler, but essentially what I did was:
#Make a for loop where we iterate through the top star ratings for each genre using an 
#index given by this line of code: len(movies.groupby('content_rating').star_rating.max())
#Give a print statement seperating each output.
#Now we filter our dataframe by genere, and then return a dataframe using loc where
#star_rating is comparable to the max star rating for that genre(given by the appropriate
#interation of the iloc method.
# then we use .title to return the title of the top rated movie. 

rating = ['G', 'NA', 'NC-17', 'PG', 'PG-13', 'R','UNRATED']
for i in range(0,len(movies.groupby('content_rating').star_rating.max())):
    print "This is the movie with top star rating for the " + rating[i]+ ' genre'
    print movies[movies.content_rating == rating[i]].loc[movies['star_rating'] == movies.groupby('content_rating').star_rating.max().iloc[i]].title
    print ""
    print ""

movies.sort('title').title.duplicated().sum()
# There are four duplicates 
#==============================================================================
# The Girl with the Dragon Tattoo
# True Grit
# Dracula
# Les Miserables
#==============================================================================
#[466, 662, 703, 924]
duplicates = movies.sort('title').title.duplicated()
duplicate_index = movies[movies.sort('title').title.duplicated() == True].index.tolist()

for index in duplicate_index: 
    print movies.iloc[index]
    print ""
    print ""
#There are not actual duplicates its the same movie name but with different actors
for index in duplicate_index:
    print movies[movies.title == movies.iloc[index].title]
    print ""
    print ""

#First make a filter list of genre with movies greater or equal to 10
# Extract out the genres that fullfill the condition into a list
#Use isin() to filter the original dataframe, group by the filtered genre and
#then calculate the mean of the star ratings 
more_than_ten=movies.groupby('genre').genre.count()>10

filtered_genres = [more_than_ten.index[i] for i in range(0,len(more_than_ten)) if more_than_ten[i] ==True]

movies[movies.genre.isin(filtered_genres)].groupby('genre').star_rating.mean()

        
