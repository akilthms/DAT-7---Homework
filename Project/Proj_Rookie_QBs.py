# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:03:34 2015

@author: akilthomas
"""

#Our hypothesis is that we can compile a list of rookie QB's buy using Beautiful soup and requests. By manipulating the url and scaping the NFL.com database
#We will only scrape the Rookie QBs that have over 50 attempts. This will ensure with a high rate that they played the majority of the season
from bs4 import BeautifulSoup
import requests 
from time import sleep 
Seasons = range(2014, 1979, -1)


def getMyRookies(_Seasons):
    rookie_QBs = [] 
    for season in _Seasons: 
        url = 'http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticCategory=PASSING&season=' + str(season) + '&seasonType=REG&experience=0&tabSeq=0&qualified=false&Submit=Go'
        r = requests.get(url)
        print r
        b = BeautifulSoup(r.text)
        rows = b.find_all(name = 'tr') 
        for row in rows[1:]:
            cols = row.find_all(name = 'td')
            position = cols[3].text
            attempts = int(cols[5].text)
            if position =='QB' and attempts > 100: 
                rookie_QBs.append(cols[1].find(name = 'a').text)
        sleep(2)
    return rookie_QBs

#print getMyRookies([2014,2013,2012])
#Rookie_List = getMyRookies(Seasons)

#for year in [2014,2013,2012]: 
#    print getMyRookies([year])

Rookie_List = [u'Derek Carr',u'Teddy Bridgewater',u'Blake Bortles',u'Zach Mettenberger',u'Geno Smith',u'Mike Glennon',u'EJ Manuel',u'Matt McGloin',u'Andrew Luck',u'Brandon Weeden',u'Ryan Tannehill',u'Robert Griffin III',u'Russell Wilson',u'Nick Foles',u'Ryan Lindley',u'Cam Newton',u'Andy Dalton',u'Blaine Gabbert',u'Christian Ponder',u'T.J. Yates',u'Sam Bradford',u'Colt McCoy',u'Jimmy Clausen',u'John Skelton',u'Mark Sanchez',u'Matthew Stafford',u'Josh Freeman',u'Keith Null',u'Matt Ryan',u'Joe Flacco',u'Trent Edwards',u'Matt Moore',u'John Beck',u'Matt Leinart',u'Vince Young',u'Bruce Gradkowski',u'Jay Cutler',u'Kyle Orton',u'Charlie Frye',u'Alex Smith',u'Ryan Fitzpatrick',u'Ben Roethlisberger',u'Eli Manning',u'Craig Krenzel',u'Byron Leftwich',u'Kyle Boller',u'David Carr',u'Joey Harrington',u'Chad Hutchinson',u'Patrick Ramsey',u'Chris Weinke',u'Quincy Carter',u'Michael Vick',u'Mike McMahon',u'Tim Couch',u'Cade McNown',u'Donovan McNabb',u'Shaun King',u'Akili Smith',u'Peyton Manning',u'Charlie Batch',u'Ryan Leaf',u'Jake Plummer',u'Tony Banks',u'Kerry Collins',u'Eric Zeier',u'Heath Shuler',u'Rick Mirer',u'Drew Bledsoe',u'Tommy Maddox']

def getCollegeStats(Rookie): 
    #manipulate url
    Rookie = Rookie.lower().replace(" ", "-")
    url = 'http://www.sports-reference.com/cfb/players/'+Rookie+'-1.html' 
    r = requests.get(url)
    #create beautifulSoup object
    b = BeautifulSoup(r.text)
    #find our row with the career stats of the NFL Rookie QB in college 
    row = b.find(name = 'tfoot').find(name = 'tr')
    #cols will hold all of our stats we then use indexing/slicing to access each specific stat
    cols = row.find_all(name = 'td')
    pass_completions = cols[6].text
    attempts = cols[7].text
    pass_completion_precentage  = cols[8].text
    passing_yards = cols[9].text
    passing_yards_per_attempt = cols[10].text
    adjusted_passing_yards_per_attempt = cols[11].text
    pass_TDs = cols[12].text
    pass_interceptions = cols[13].text
    passing_effeciency_rating = cols[14].text
    
    stats_row = [pass_completions, attempts, pass_completion_precentage,passing_yards, passing_yards_per_attempt,adjusted_passing_yards_per_attempt,pass_TDs, pass_interceptions, passing_effeciency_rating]
    stats_row = [float(stat) for stat in stats_row]
    return stats_row

#print getCollegeStats(Rookie_List[0])

#defining a function to get all of our stats for our rookies.
def rookieStatsRoundUp(Rookie_List):
    Player_and_Stats = {}
    for rookie in Rookie_List:
        Player_and_Stats[rookie] = getCollegeStats(rookie)
        sleep(2)
    return Player_and_Stats

print rookieStatsRoundUp(Rookie_List)

db_subset_1 = rookieStatsRoundUp(Rookie_List[0:10])
db_subset_2 = rookieStatsRoundUp(Rookie_List[10:20])
db_subset_3 = rookieStatsRoundUp(Rookie_List[20:30])
db_subset_4 = rookieStatsRoundUp(Rookie_List[30:40])
db_subset_5 = rookieStatsRoundUp(Rookie_List[50:60])
db_subset_6 = rookieStatsRoundUp(Rookie_List[60:70])

#Joe flacco only has stats for one year at Pittsburgh 
missing_sats = ['Joe Flacco', 'Keith Null', 'John Skelton','Ryan Fitzpatrick' ]
Rookie_List_Edited = [u'Derek Carr',u'Teddy Bridgewater',u'Blake Bortles',u'Zach Mettenberger',u'Geno Smith',u'Mike Glennon',u'EJ Manuel',u'Matt McGloin',u'Andrew Luck',u'Brandon Weeden',u'Ryan Tannehill',u'Robert Griffin III',u'Russell Wilson',u'Nick Foles',u'Ryan Lindley',u'Cam Newton',u'Andy Dalton',u'Blaine Gabbert',u'Christian Ponder',u'T.J. Yates',u'Sam Bradford',u'Colt McCoy',u'Jimmy Clausen',u'Mark Sanchez',u'Matthew Stafford',u'Josh Freeman',u'Matt Ryan',u'Trent Edwards',u'Matt Moore',u'John Beck',u'Matt Leinart',u'Vince Young',u'Bruce Gradkowski',u'Jay Cutler',u'Kyle Orton',u'Charlie Frye',u'Alex Smith',u'Ryan Fitzpatrick',u'Ben Roethlisberger',u'Eli Manning',u'Craig Krenzel',u'Byron Leftwich',u'Kyle Boller',u'David Carr',u'Joey Harrington',u'Chad Hutchinson',u'Patrick Ramsey',u'Chris Weinke',u'Quincy Carter',u'Michael Vick',u'Mike McMahon',u'Tim Couch',u'Cade McNown',u'Donovan McNabb',u'Shaun King',u'Akili Smith',u'Peyton Manning',u'Charlie Batch',u'Ryan Leaf',u'Jake Plummer',u'Tony Banks',u'Kerry Collins',u'Eric Zeier',u'Heath Shuler',u'Rick Mirer',u'Drew Bledsoe',u'Tommy Maddox']
db_subset_3_1 = rookieStatsRoundUp(Rookie_List_Edited[20:30])

#My Tests
mylist = [getCollegeStats(rook) for rook in Rookie_List_Edited[20:30]]
print getCollegeStats(Rookie_List_Edited[20:30][7])
#End Tests 
def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
Database = merge_dicts(db_subset_1, db_subset_2, db_subset_3_1,db_subset_4, db_subset_5, db_subset_6)
Database = rookieStatsRoundUp(Rookie_List_Edited)
import pandas as pd
Database_pd = pd.DataFrame(Database)
new_db = pd.DataFrame(columns = ['names','pass_completions', 'attempts', 'pass_completion_precentage','passing_yards', 'passing_yards_per_attempt', 'adjusted_passing_yards_per_attempt','pass_TDs', 'pass_interceptions', 'passing_effeciency_rating'])
new_db.names = Rookie_List_Edited
Database_pd = Database_pd.transpose()
Database_pd.columns = ['CMP', 'Attps', 'PCT','Yds', 'Y/A', 'AY/A','TDs', 'Int', 'Rate']
pd.set_option('display.width', 170)
compare_List = list(Database_pd.index)

for player in Rookie_List_Edited:
    if player not in compare_List: 
        print player

players_missing = [player for player in Rookie_List_Edited if player not in compare_List]


addition_data = rookieStatsRoundUp(players_missing)
more_data = pd.DataFrame(addition_data)
more_data = more_data.transpose()
more_data.columns = ['CMP', 'Attps', 'PCT','Yds', 'Y/A', 'AY/A','TDs', 'Int', 'Rate']
Database_pd_result = pd.concat([Database_pd,more_data], axis = 0)

#Update Alex Smith in the data. This is not the Alex Smith that started for the 49ERS 
alex_smith = [389,	587,66.3,5203,8.9,	9.9,47,8,164.4]

Database_pd_result.loc['Alex Smith'] = alex_smith

Database_pd_result.to_csv('Rookies.csv')


