from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import numpy
import time
import pandas as pd
from datetime import timedelta
from datetime import datetime
'''
address = "https://www.pgatour.com/competition/2019/safeway-open/leaderboard.html"
website = requests.get(address)
soup = BeautifulSoup(website.content, "html.parser")
browser = webdriver.Firefox()
rounds = []
rounddata = soup.find_all("td", class_="row-title")
for i in rounddata:
	rounds.append(i.get_text())

print(rounds)


'''
#class="truste_overlay"

browser = webdriver.Chrome() 
browser.get('https://www.pgatour.com/competition/2021/the-american-express/leaderboard.html')

try:
	WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]'))).click()
except:
	pass
	
playerlist = browser.find_elements_by_class_name('player-name-col')

'''
playerlist[1].click()
time.sleep(5)
print(playerlist[1].text)
playerlist[1].click()
time.sleep(5)
'''
for p in playerlist[0:3]:
	p.click()
	time.sleep(5)
	print(p.text)
	p.click()
	time.sleep(5)
	
	
