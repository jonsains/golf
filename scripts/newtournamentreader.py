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

tname = 'sanderson-farms-championship'

#step 1: Open a browser and close cookies
def pga_page_load(url):
    global browser
    browser = webdriver.Chrome()
    browser.get(url)
    try:
        WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]'))).click()
    except:
        pass


def closewait():
    time.sleep(1)
    if len(browser.find_elements(By.CLASS_NAME, 'close-drawer-button-column')) != 0:
        print('STILL OPEN!!!')
        closewait()
    else:
        pass

def nineholegetinfo():
    try:
        WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH,"//tr[@class='scorecard-data-row playerData']")))
    except:
        print('player data class FAIL!')
    scores = browser.find_elements_by_xpath("//*[@class='score-card wide']/tbody/*[@class='scorecard-data-row playerData']/td")
    holenumber = browser.find_elements_by_xpath("//*[@class='score-card wide']/tbody/*[@class='hole']/td")
    holelist = [int(i.text) for i in holenumber[1:10]]
    scorelist = [j.text for j in scores[1:10]]
    #print(str(holelist) + ',' + str(scorelist))
    rounddata = {hole: hits for (hole,hits) in zip(holelist,scorelist) }
    return rounddata

def playertournament():
    roundsplayed = browser.find_elements_by_xpath("//*[@class='round-selector']/span")
    rplist = [i.text for i in roundsplayed]
    #print(rplist)
    fullt = {}
    playerrowdata = []
    roundcheck = 1
    for round in roundsplayed[1:5]:
        try:
            round.click()
            #print(round.text)
            WebDriverWait(browser,40).until(EC.presence_of_element_located((By.XPATH,"//span[@class='round active'][(text()='" + round.text + "')]")))
            firsthalf = nineholegetinfo()
            #print('here1' + str(firsthalf))
            frontnine = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//td[@class='change-page']")))
            inorout = browser.find_element_by_class_name('in-out').text
            frontnine.click()
            if inorout == 'IN':
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='OUT']")))
            else:
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='IN']")))
            secondhalf = nineholegetinfo()
            firsthalf.update(secondhalf)
            fullt[round.text] = firsthalf
            for i in range(1,19):
                playerrowdata.append(firsthalf[i])
            roundcheck += 1
        except:
            print('cant click')
    return playerrowdata  

#step 2: Create a loop to open and close every players scores on a tournament results page such as https://www.pgatour.com/competition/2022/bmw-championship/leaderboard.html
def playersloop():
    playerlist = browser.find_elements(By.CLASS_NAME, 'player-name-col')
    dfdata = []
    for p in playerlist:
        p.click()
        try:
            WebDriverWait(browser,40).until(EC.presence_of_element_located((By.XPATH,"//tr[@class='scorecard-data-row playerData']")))
        except:
            print('player data class FAIL!')
        #print(p.text)
        #print(playertournament())
        thisplayersrow = [str(p.text)] + playertournament()
        dfdata.append(thisplayersrow)

        p.click()
        closewait()
    print('here is the output')
    return dfdata
    
        #playertournament = tdata(p)
        #tlist(p, dfdata, playertournament)

#step 3: Write a function to collect the scores from a front/back 9



pga_page_load('https://www.pgatour.com/competition/2023/' + tname + '/leaderboard.html')
dfdata = playersloop()
df = pd.DataFrame(dfdata)
dates = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='dates']"))).text
datespieces = dates.split()
if len(datespieces[2]) == 1:
    datespieces[2] = '0' + datespieces[2]
sdate = datespieces[1][0:3] + datespieces[2] + datespieces[-1]
df.to_csv('/Users/jonsa/OneDrive/Documents/code/tournaments/' + sdate + tname + '.csv', encoding='utf-8')

#step 4: Write a function to run through all the rounds a player played in a tournament and collect all their scores



    





#step 5: add player's name and scores to a dataframe
#step 6: when complete, store round info as a csv