# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:05:16 2015

@author: akilthomas
"""
#Import relevant modules 

import pandas as pd 
from bs4 import BeautifulSoup 
import requests 
rookies = pd.read_csv('Rookies_CFB_Stats.csv')

rookies.rename(columns = {'Unnamed: 0': 'Name'}, inplace = True)
#Other features, college years played, NFL team previous years record record, rushing stats, 
def gather_prev_season():
    
def W_L_Record():


def team_ABRV()
    d = {}
    url = 'http://www.footballgeography.com/sample-page-2/pro-football-abbreviations/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text)
    rows = bs.find(name = 'tbody').find_all(name = 'tr')
    print len(rows) 
    
    
    