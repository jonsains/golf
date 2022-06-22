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
#url = "https://www.pgatour.com/competition/2019/safeway-open/leaderboard.html"
#browser.get(url) 
#WebDriverWait(browser,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="TrustArc Cookie Consent Manager"]')))
#WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button onetrust-lg ot-close-icon"]'))).click()
#browser.implicitly_wait(10)
#frame_reference = browser.find_element_by_id("pop-frame008392052294596386")
#browser.switch_to.frame(frame_reference)
#cookieclose = browser.find_element_by_xpath("//a[@class = 'close']")
#cookieclose = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='close']")))
#cookieclose.click()
#browser.switch_to.default_content()


def getinfo():
	rounddata = {}
	try:
		WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH,"//tr[@class='scorecard-data-row playerData']")))
	except:
		print('player data class FAIL!')

	innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	soup = BeautifulSoup(innerHTML, "html.parser")
	#print(soup.prettify().encode("utf8"))
	file = open('html2.txt','w') 
 
	file.write(str(soup.prettify().encode("utf8"))) 
	file.close() 
	scorestable = soup.find('table', class_ = 'score-card wide')
	body = scorestable.find('tr', class_ = 'scorecard-data-row playerData')
	#print(body.encode("utf8"))
	scores = body.find_all('td')
	
	for i in scores:
		if i.find('div', class_ = 'score-wrapper'):
			rounddata[int(i['data-hole-number'])] = i.find('div', class_ = 'score-wrapper').text
	return rounddata

def tdata(element):
	#element = browser.find_element_by_class_name('player-name-col')
	element.click()
	#WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//td[@data-hole-number='10']")))
	try:
		round = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='round active']"))).text
	except:
		round = '1'
	#round = browser.find_element_by_class_name("round active").text
	front4 = []
	front3 = []
	front2 = []
	front1 = []
	#holes = browser.find_elements_by_class_name('player-name-col')
	if round == '4':
		back4 = getinfo()
		#print back4
		frontnine = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//td[@class='change-page']")))
		inorout = browser.find_element_by_class_name('in-out').text
		frontnine.click()
		if inorout == 'IN':
			WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='OUT']")))
		else:
			WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='IN']")))
		front4 = getinfo()
		#print front4
		front4.update(back4)    # modifies z with y's keys and values & returns None
		#print front4
		print(WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='round'][text()='3']"))).text)
		WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='round'][text()='3']"))).click()
		WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='round active'][text()='3']")))
		round = '3'
	if round == '3':   	
		back3 = getinfo()
		#print back3
		frontnine = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//td[@class='change-page']")))
		inorout = browser.find_element_by_class_name('in-out').text
		frontnine.click()
		if inorout == 'IN':
			WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='OUT']")))
		else:
			WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='IN']")))
		front3 = getinfo()
		#print front3
		front3.update(back3)    # modifies z with y's keys and values & returns None
		#print front3
		print(WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='round'][text()='2']"))).text)
		WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='round'][text()='2']"))).click()
		WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='round active'][text()='2']")))
		round = '2'
	if round == '2':
		back2 = getinfo()
		print(back2)
		frontnine = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//td[@class='change-page']")))
		inorout = browser.find_element_by_class_name('in-out').text
		frontnine.click()
		if inorout == 'IN':
			WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='OUT']")))
		else:
			WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='IN']")))

		front2 = getinfo()
		print(front2)
		front2.update(back2)    # modifies z with y's keys and values & returns None
		print(front2)
		print(WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='round'][text()='1']"))).text)
		WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='round'][text()='1']"))).click()
		WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='round active'][text()='1']")))
		round = '1'

	back1 = getinfo()
	print(back1)
	frontnine = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//td[@class='change-page']")))
	inorout = browser.find_element_by_class_name('in-out').text
	frontnine.click()
	if inorout == 'IN':
		WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='OUT']")))
	else:
		WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//td[@class='in-out'][text()='IN']")))

	front1 = getinfo()
	print(front1)
	front1.update(back1)
	print('about to close')
	

	
	#playerparent = element.find_element_by_xpath('.//ancestor::tr')
	#print(element.get_attribute("class"))
	#print(playerparent.get_attribute("class"))
	time.sleep(2)
	
	#closebutton = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='close-drawer-button']"))).click()
	element.click()
	time.sleep(2)

	stillopen = browser.find_elements_by_class_name('close-drawer-button')
	print('still open:' + str(len(stillopen)))
	for i in stillopen:
		i.click()
	time.sleep(1)
	'''
	def closecheck():
		parentclass = playerparent.get_attribute("class")
		print(parentclass[-4:])
		if parentclass[-4:] == 'open':
			WebDriverWait(browser,20)
			print('still open')
			
			closecheck()
		else:
			print('closed!')

	closecheck()

	'''
	#WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,".//td[@class='tourcast']")))

	#close = WebDriverWait(playerparent,10).until(EC.element_to_be_clickable((By.XPATH,".//descendant::div[@class='close-drawer-button']"))).click()
	#checkproperclose = WebDriverWait(playerparent,10).until(EC.element_to_be_clickable((By.XPATH,".//descendant::td[@class='tourcast']")))
	
	print('should be closed')
	return front1, front2, front3, front4

def tlist(player,dflist, pdata):
	
	playerrow = []
	playerrow.append(player.text)
	for i in pdata:
		for j in i:
			playerrow.append(i[j])
	dflist.append(playerrow)


def get_year_sched(url):
	browser.get(url) 
	WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]'))).click()
	innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	soup = BeautifulSoup(innerHTML, "html.parser")
	tourneys = soup.find_all('a', class_ = 'bottom-string js-tournament-name')
	tourneylist = []
	for i in tourneys:
		tourneylist.append(i.text)
	return tourneylist
'''
schedule = get_year_sched('https://www.pgatour.com/tournaments/schedule.html')
print(schedule)
'''
	



def playerupdate(results,tinfo):
	pass

class player:
	pass


def tournament(tname, course = 'notentered'):
	tnameurl = tname.replace(' ','-').lower()
	scorecardurl = "https://www.pgatour.com/competition/2022/" + tnameurl + "/leaderboard.html"
	
	browser.get(scorecardurl)
	try:
		WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]'))).click()
	except:
		pass
	
	playerlist = browser.find_elements_by_class_name('player-name-col')
	dfdata = []
	for p in playerlist:
		print(p.text)
		playertournament = tdata(p)
		tlist(p, dfdata, playertournament)
	
			
	
	
	dates = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='dates']"))).text
	print(dates)
	datespieces = dates.split()
	if len(datespieces[2]) == 1:
		datespieces[2] = '0' + datespieces[2]
	sdate = datespieces[1][0:3] + datespieces[2] + datespieces[-1]
	print(sdate)
	startdate = datetime.strptime(sdate, '%b%d%Y')
	print(startdate)

	location = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='name']"))).text

	df = pd.DataFrame(dfdata)
	df.to_csv(sdate + tname + '.csv', encoding='utf-8')
	df2 = pd.DataFrame({'location': [location], 'startdate': [startdate]})
	df2.to_csv(sdate + tname + 'additionalinfo.csv', encoding='utf-8')

def course(tname):
	tnameurl = tname.replace(' ','-').lower()
	url = "https://www.pgatour.com/tournaments/" + tnameurl + "/course.html"
	browser.get(url)
	try:
		WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button onetrust-lg ot-close-icon"]'))).click()
	except:
		pass
	browser.execute_script("window.scrollTo(0, 500);")
	WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,"//span[@class='title-main']")))
	
	innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	soup = BeautifulSoup(innerHTML, "html.parser")
	h = []
	p = []
	y = []
	aves = []
	holes = soup.find_all('span', class_ = 'title-main')[1:-1]
	print(len(holes))
	for i in holes:
		j = i.text[6:]
		h.append(j)
	paryards = soup.find_all('span', class_ = 'title-second')[1:-1]
	for i in paryards:
		parts = i.text.split()
		pars = parts[1][:-1]
		yards = parts[2]
		p.append(pars)
		y.append(yards)
		
	scoreav = soup.find_all('div', class_ = 'hole-by-hole-avg')[1:-1]
	for i in scoreav:
		aves.append(i.text.split()[0])
	df2 = pd.DataFrame({'hole': h, 'par': p, 'yards': y, 'averagescore': aves})
	df2.to_csv(tname + 'course21.csv', encoding='utf-8', index=False)
'''
tournament('shriners-childrens-open')
'''

course('farmers-insurance-open'.lower())

'''
schedule = ['genesis-invitational', 'the-honda-classic']
for i in schedule:
	try:
		tournament(i)
	except:
		print(i + ' fail')

'''
#		url = "https://www.pgatour.com/competition/2019/safeway-open/leaderboard.html"
#tournament('safeway.csv', 'https://www.pgatour.com/competition/2019/safeway-open/leaderboard.html')
#print(tournament.tname)	 
#WebDriverWait(browser,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="TrustArc Cookie Consent Manager"]')))
#WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button onetrust-lg ot-close-icon"]'))).click()

	
'''https://www.pgatour.com/competition/2019/safeway-open/leaderboard.html'''


	

'''innerHTML = browser.execute_script("return document.body.innerHTML")
soup = BeautifulSoup(innerHTML, "html.parser")
playerlist = soup.find_all('div', class_ = 'player-name-col')
print(len(playerlist))
for p in playerlist[0:3]:
	player = (p.text)
	print(player)
	retrieve(p)
'''
#print(innerHTML.encode("utf8"))

	

#tabledata = browser.find_element_by_xpath("//td[@data-hole-number='10']")
#print(tabledata.get_attribute('innerHTML'))
#holes = []
#scores = []
#html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
#soup = BeautifulSoup(html, "html.parser")
#data = soup.select(".scorecard-data-row playerData")

'''get back nine data and set up to do front nine
data = soup.find(attrs = {'class': 'scorecard-data-row playerData'})
for i in data.children:
	print(i)


WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//td[@data-hole-number='1']")))

html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")
'''

#data = soup.select(".scorecard-data-row playerData")
'''
playerchunk = soup.find_all(attrs = {'class': 'leaderboard leaderboard-table large'})
print(len(playerchunk))

chunk = playerchunk[0]
print(type(chunk))
print(len(chunk.contents))

for i in playerchunk:
	playerdata = []
	playername = i.find(attrs = {'class': 'player-name-col'})
	playerdata.append(playername)

	print('here is the current list ' + str(playerdata))

	'''


'''
for i in playerchunk:
	playerdata = []
	if i.descendents != None:
		for j in i.descendents:
			if j['class'] == 'player-name-col':
				playerdata.append(j.get_text())
		print(playerdata)




data = soup.find(attrs = {'class': 'scorecard-data-row playerData'})
for i in data.children:
	print(i)
'''


#file = open('html.txt','w') 
 
#file.write(soup.prettify().encode("utf8")) 
#file.close() 

#print(html.encode('utf8'))

#holes = browser.find_elements_by_xpath("//td[@class='row-data par' or @class='row-data birdie' or @class = 'row-data bogey']")
#for i in range(len(holes)):
#	print(holes[i].get_attribute('innerHTML'))
'''for i in holes:
	print(i)
	holenumber = i.get_attribute('innerHTML')
	holes.append(holenumber)
print(holes)

'''


#data = tabledata.get_attribute('innerHTML')
#print(data)
'''

<span class="icon-backward"></span> #back button element to view first 9 holes

<div data-hole-number="10">10</div> #hole number in players hole score table
<td class="row-data" data-hole-number="10">4</td> 
<td class="row-data par" data-hole-number="10">4</td> # or row data .bogey etc... (try regex?)
<td class="row-data par" data-hole-number="16">5</td>

#innerHTML = browser.page_source

#innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
#print(innerHTML.encode("utf8"))

soup = BeautifulSoup(innerHTML, "html.parser")
#print(soup.prettify().encode("utf8"))

rounds = []
table = soup.find_all("table", class_="score-card wide")
print(table)
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    rounds.append([ele for ele in cols if ele])


print(rounds)

'''
#pop-frame09071467976874186

'''
['Safeway Open', 'U.S. Open', 'Corales Puntacana Resort & Club Championship', 'Sanderson Farms Championship', 'Shriners Hospitals for Children Open', 'THE CJ CUP @ SHADOW CREEK', 'ZOZO CHAMPIONSHIP @ SHERWOOD', 'Bermuda Championship', 'Vivint Houston Open', 'Masters Tournament', 'The RSM Classic', 'Mayakoba Golf Classic presented by UNIFIN', 'Sentry Tournament of Champions', 'Sony Open in Hawaii', 'The American Express', 'Farmers Insurance Open', 'Waste Management Phoenix Open', 'AT&T Pebble Beach Pro-Am', 'The Genesis Invitational', 'Puerto Rico Open', 'World Golf Championships-Workday Championship at The Concession', 'Arnold Palmer Invitational presented by Mastercard', 'THE PLAYERS Championship', 'The Honda Classic', 'World Golf Championships-Dell Technologies Match Play', 'Corales Puntacana Resort & Club Championship', 'Valero Texas Open', 'Masters Tournament', 'RBC Heritage', 'Zurich Classic of New Orleans', 'Valspar Championship', 'Wells Fargo Championship', 'AT&T Byron Nelson', 'PGA Championship', 'Charles Schwab Challenge', 'the Memorial Tournament presented by Nationwide', 'Palmetto Championship at Congaree', 'U.S. Open', 'Travelers Championship', 'Rocket Mortgage Classic', 'John Deere Classic', 'Barbasol Championship', 'The Open Championship', '3M Open', 'Barracuda Championship', 'World Golf Championships-FedEx St. Jude Invitational', 'Wyndham Championship', 'THE NORTHERN TRUST', 'BMW Championship', 'TOUR Championship']
['Safeway Open', 'U.S. Open', 'Corales Puntacana Resort & Club Championship', 'Sanderson Farms Championship', 'Shriners Hospitals for Children Open', 'THE CJ CUP @ SHADOW CREEK', 'ZOZO CHAMPIONSHIP @ SHERWOOD', 'Bermuda Championship', 'Vivint Houston Open', 'Masters Tournament', 'The RSM Classic', 'Mayakoba Golf Classic presented by UNIFIN', 'Sentry Tournament of Champions', 'Sony Open in Hawaii', 'The American Express', 'Farmers Insurance Open', 'Waste Management Phoenix Open', 'AT&T Pebble Beach Pro-Am', 'The Genesis Invitational', 'Puerto Rico Open', 'World Golf Championships-Workday Championship at The Concession', 'Arnold Palmer Invitational presented by Mastercard', 'THE PLAYERS Championship', 'The Honda Classic', 'World Golf Championships-Dell Technologies Match Play', 'Corales Puntacana Resort & Club Championship', 'Valero Texas Open', 'Masters Tournament', 'RBC Heritage', 'Zurich Classic of New Orleans', 'Valspar Championship', 'Wells Fargo Championship', 'AT&T Byron Nelson', 'PGA Championship', 'Charles Schwab Challenge', 'the Memorial Tournament presented by Nationwide', 'Palmetto Championship at Congaree', 'U.S. Open', 'Travelers Championship', 'Rocket Mortgage Classic', 'John Deere Classic', 'Barbasol Championship', 'The Open Championship', '3M Open', 'Barracuda Championship', 'World Golf Championships-FedEx St. Jude Invitational', 'Wyndham Championship', 'THE NORTHERN TRUST', 'BMW Championship', 'TOUR Championship']

'''

