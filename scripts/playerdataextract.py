from cmath import nan
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import numpy as np
import pandas as pd
import time
from datetime import timedelta
from datetime import datetime
from os.path import exists
from csv import writer

'''
extratournament = pd.DataFrame(np.array([['test-open']]), columns = ['tournamentname'])
print(extratournament)
extratournament.to_csv('/Users/jonsa/OneDrive/Documents/code/tournamentsread.csv')
'''

#create a function that creates/updates the player files
def playerupdate(tournamentname, course):
    
    #check this tournament hasn't been done before:
    readtourneys = pd.read_csv('tournamentsread.csv')
    print(readtourneys['tournamentname'])
    if course in readtourneys['tournamentname'].to_list():
        print('ALREADY UPDATED!')
    else:
  
    
    #1 read in the data and get it in a nice format
  
        tourneyscores = pd.read_csv('/Users/jonsa/OneDrive/Documents/code/tournaments/' + tournamentname + '.csv')
        #print(tourneyscores.columns)
        newcols = ['index','name']
        holes = range(1,73,1)
        newcols += holes
        #print(newcols)
        tourneyscores.columns = newcols
        tourneyscores['name'] = tourneyscores['name'].str.lower()

        tourneyscores.set_index('name', inplace=True)
        tourneyscores.drop('index', axis=1, inplace=True)
        print(tourneyscores.head())
        
        #2 for each player name, check if the csv exists and create it if it doesn't
        playercols = ['hole','score','round', 'par', 'yards', 'average_score','location', 'date', 'temp', 'wind', 'rain']
        for player in tourneyscores.index:
            if os.path.exists('/Users/jonsa/OneDrive/Documents/code/players/' + str(player) + '.csv'):
                print(str(player) + ' player file already exists')
                print(type(player))
            else:
                print('creating file for ' + str(player))
                df = pd.DataFrame(columns= playercols)
                print(player)
                df.to_csv('/Users/jonsa/OneDrive/Documents/code/players/' + str(player) + '.csv')
        
        #3 for each player name create a list of lists comprised of hole number and score and round, making sure hole number is still correct after nans are removed
            print('kjfljgdkflgj')
            print(tourneyscores.index)
            print(tourneyscores.index[2])
            print(player)
            print(tourneyscores.index[2] == player)
            print('dfdfdgfhgfggnb')
            #newrows = tourneyscores.loc[player].values.tolist()
            test = tourneyscores.loc[str(player)]
            
            newrows = [[test.index[x]%18 , test[test.index[x]], (((test.index[x] - 1)//18) + 1)] for x in range(0, len(test))]
            for x in newrows:
                if x[0] == 0:
                    x[0] += 18
            newrows = [x for x in newrows if str(x[1]) != "nan"]
            #newrows = [[y, x] for x in newrows if str(x) != "nan"]   [test.index[x], test[x]]
            #print(newrows)
        #create a dataframe with hole score and round
            holesandscores = pd.DataFrame(np.array(newrows), columns=['hole', 'score','round'])
        
        #this looks to be working up to here
    
        #3.1 import the course data and add par yards and average score to the player holes data
            courseinfo = pd.read_csv('/Users/jonsa/OneDrive/Documents/code/tournaments/' + course + 'course21.csv')
            courseinfo.index.name = 'ind2'
            #print(tourneyscores)
            playerdatawithcourse = pd.merge(holesandscores, courseinfo,  how='left', left_on=['hole'], right_on = ['hole'])
            
            # add the date and location
            timeandplace = pd.read_csv('/Users/jonsa/OneDrive/Documents/code/tournaments/' + tournamentname + 'additionalinfo.csv')
            location = timeandplace.iloc[0]['location']
            dayone = datetime.strptime(timeandplace.iloc[0]['startdate'], '%Y-%m-%d')
            #dayone = timeandplace.iloc[0]['startdate']
            #print(type(dayone))

            #print(location)
            #print(playerdatawithcourse[round])
            playerdatawithcourse['location']= location
            #playerdatawithcourse['date'] = dayone + timedelta(days=(playerdatawithcourse['round'] - 1) )

            #rounddate = [dayone + timedelta(days=(int(roundnum) -1)) for roundnum in playerdatawithcourse[round]]

            playerdatawithcourse['date'] = [dayone + timedelta(days=(int(roundnum) -1)) for roundnum in playerdatawithcourse['round']]
            #print(playerdatawithcourse)

            weatherinfo = pd.read_csv('/Users/jonsa/OneDrive/Documents/code/golfweather.csv')
            tournamentweather = weatherinfo.loc[weatherinfo['tournament-w'] == course]
            
            finalplayerdata = pd.merge(playerdatawithcourse, tournamentweather,  how='left', left_on=['round'], right_on = ['round-w'])
            finalplayerdata.drop(['tournament-w', 'date-w' , 'round-w'], axis=1, inplace=True)
            #print(finalplayerdata)

            #3.4 add to the main player file
            extratournament = pd.DataFrame(np.array([[str(course)]]))
            #print(extratournament)
            finalplayerdata.to_csv('/Users/jonsa/OneDrive/Documents/code/players/' + str(player) + '.csv', mode = 'a', header=False)
            # add the tournament to the read tournaments list
    
    with open('/Users/jonsa/OneDrive/Documents/code/tournamentsread.csv', 'a') as f:
        writerobject = writer(f)
        writerobject.writerow(['',course])
        f.close()



#playerupdate("Jan262022farmers-insurance-open", "farmers-insurance-open")
playerupdate("Sep162021fortinet championship", "fortinet championship")


#"Jan262022farmers-insurance-open.csv"