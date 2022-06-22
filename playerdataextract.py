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



#create a function that creates/updates the player files
def playerupdate(tournamentname, course):  
    #1 read in the data and get it in a nice format
  
    tourneyscores = pd.read_csv(tournamentname + '.csv')
    #print(tourneyscores.columns)
    newcols = ['index','name']
    holes = range(1,73,1)
    newcols += holes
    #print(newcols)
    tourneyscores.columns = newcols

    tourneyscores.set_index('name', inplace=True)
    tourneyscores.drop('index', axis=1, inplace=True)
    #print(tourneyscores.head())
    #print('vhel')
    
    #2 for each player name, check if the csv exists and create it if it doesn't
    playercols = ['hole','par','length','average_score','score']
    for player in tourneyscores.index[-1:]:
        if os.path.exists('/Users/jonsa/OneDrive/Documents/code/players/' + str(player) + '.csv'):
            pass
            #print(str(player))
        else:
            print('creating file for ' + str(player))
            df = pd.DataFrame(columns= playercols)
            #print(df.head)
            df.to_csv('/Users/jonsa/OneDrive/Documents/code/players/' + str(player) + '.csv')
    
    #3 for each player name create a list lists comprised of hole number and score, making sure hole number is still correct after nans are removed

        #newrows = tourneyscores.loc[player].values.tolist()
        test = tourneyscores.loc[player]
        print(range(len(test)))
        newrows = [[test.index[x]%18 , test[test.index[x]]]  for x in range(0, len(test))]
        for x in newrows:
            if x[0] == 0:
                x[0] += 18
        newrows = [x for x in newrows if str(x[1]) != "nan"]
        #newrows = [[y, x] for x in newrows if str(x) != "nan"]   [test.index[x], test[x]]
        print(newrows)
        holesandscores = pd.DataFrame(np.array(newrows), columns=['hole', 'score'])
    
    #this looks to be working up to here
   
    #3.1 first set up the course data
        tourneyscores = pd.read_csv(course + 'course21.csv')
        tourneyscores.index.name = 'ind2'
        #print(tourneyscores)
        playerdatawithcourse = pd.merge(holesandscores, tourneyscores,  how='left', left_on=['hole'], right_on = ['hole'])
        print(playerdatawithcourse)

    #3.2 get hole number and score

    #3.3 add extra fields from course data

    #3.4 add to the player file


playerupdate("Jan262022farmers-insurance-open", "farmers-insurance-open")



#"Jan262022farmers-insurance-open.csv"