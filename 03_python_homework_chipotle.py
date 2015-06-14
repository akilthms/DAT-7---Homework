# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 08:30:51 2015

@author: akilthomas
"""
#Part 1
import csv

with open('chipotle.tsv', 'rU') as file: 
    data = [row for row in csv.reader(file, delimiter = '\t')]
#Part 2
header = data[0] #Stores the header of the data

body = data[1:] #Stores only the data to be analyzed

#Part 3
#To find the average number price of an order we will have to sum all the price
#and divide it by the total amount of unique orders.

#To accomplish this we must clean our price data
#To properly sum the prices we most remove the dollar sign

prices = [float(price[4][1:-1]) for price in body] 
    
average = sum(prices)/int(body[-1][0])

print average 
    
#The average price of a meal is $18.81 
#Part 4
# Create a list comprehension that creates a list of all sodas in the data set
sodas = [row[3] for row in body if row[2] == 'Canned Soda' or row[2] == 'Canned Soft Drink'] # row[2] - Is Canned Soda or Canned Soft drink if either one we add the name of the drink row[3]

unique_sodas = set(sodas)

cleaned_sodas = [soda[1:-1] for soda in unique_sodas] #clean the data a bit

#Part 5 
# fInd total amount of toppings by summing a list of integers of toppings per each burrito
toppings_count = [len(row[3].replace('[',"").replace(']',"").split(',')) for row in body if 'Burrito' in row[2]]
burrito_count = 0 
for row in body:
    if 'Burrito' in row[2]:
        burrito_count+=1
#There are 1172 burritos in total
average_toppings = float(sum(toppings_count)) / burrito_count
# The averagae number of toppings per burrito 5.4 or 5 approxiamtely

#Part 6 
# First we need a list of each unique chip order(set).
# Then we iterate through the data and add the orders(quantity column)

chip_orders = set([row[2] for row in body if 'Chips' in row[2]])

chips = [chip for chip in chip_orders]

# set the keys(chip order) of our dictionary to a value of zero
my_dict = {}

for chip in chips: 
    my_dict[chip] = 0

for row in body:
    if 'Chips' in row[2]:
        my_dict[row[2]] += int(row[1])
#Output
#==============================================================================
# {'Chips': 230,
#  'Chips and Fresh Tomato Salsa': 130,
#  'Chips and Guacamole': 506,
#  'Chips and Mild Fresh Tomato Salsa': 1,
#  'Chips and Roasted Chili Corn Salsa': 23,
#  'Chips and Roasted Chili-Corn Salsa': 18,
#  'Chips and Tomatillo Green Chili Salsa': 45,
#  'Chips and Tomatillo Red Chili Salsa': 50,
#  'Chips and Tomatillo-Green Chili Salsa': 33,
#  'Chips and Tomatillo-Red Chili Salsa': 25,
#  'Side of Chips': 110}
#==============================================================================

# What makes more money for Chipotle? Chips or drinks? 

#Build a unique order of drinks. Which is Canned Soda, Canned Soft Drink, Izze,
# Nantucket Nectar, Bottled Water and then sum their prices do the same thing for
#the chip orders

Drinks = set([row[2] for row in body if row[2] == 'Canned Soda' or row[2] == 'Canned Soft Drink' or row[2]=='Izze'or row[2]=='Bottled Water' or row[2]== 'Nantucket Nectar']) 
Drinks = [drink for drink in Drinks]

Sum_Drinks = sum([float(row[4][1:-1]) for row in body if row[2] in Drinks])
Sum_Chips = sum([float(row[4][1:-1]) for row in body if row[2] in chips])
#In this sample set Chips made more money ($3775.38) then drinks (1044.760)
