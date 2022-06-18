from cmath import nan
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import numpy
import pandas as pd
import time
from datetime import timedelta
from datetime import datetime
from os.path import exists 



#create a function that creates/updates the player files
def playerupdate(tournamentfilename):  
    #1 read in the data and get it in a nice format
    
    tourneyscores = pd.read_csv(tournamentfilename)
    #print(tourneyscores.columns)
    newcols = ['index','name']
    holes = range(1,73,1)
    newcols += holes
    #print(newcols)
    tourneyscores.columns = newcols

    tourneyscores.set_index('name', inplace=True)
    tourneyscores.drop('index', axis=1, inplace=True)
    print(tourneyscores.head())
    print('vhel')
    
    #2 for each player name, check if the csv exists and create it if it doesn't
    playercols = ['hole','par','length','average_score','score']
    for player in tourneyscores.index[-1:]:
        if os.path.exists('/Users/jonsa/OneDrive/Documents/code/players/' + str(player) + '.csv'):
            print(str(player))
        else:
            print('creating file for ' + str(player))
            df = pd.DataFrame(columns= playercols)
            print(df.head)
            df.to_csv('/Users/jonsa/OneDrive/Documents/code/players/' + str(player) + '.csv')
    
    #3 for each player name create a list of data for each new hole played and add it to the player file

        newrows = tourneyscores.loc[player].values.tolist()
        newrows = [x for x in newrows if str(x) != "nan"]
        print(newrows)
        print(len(newrows))
        print(type(newrows[-1]))
    #this looks to be working. next filter out if there are any nans and create the hole and score lists
        listj = [4,5,5]
        print(type(listj))


    #3.1 first set up the course data

    #3.2 get hole number and score

    #3.3 add extra fields from course data

    #3.4 add to the player file


playerupdate("Jan262022farmers-insurance-open.csv")



#"Jan262022farmers-insurance-open.csv"