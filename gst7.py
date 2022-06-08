import csv
import numpy
import pandas as pd
from datetime import timedelta
from datetime import datetime
#aim: add on the latest player scores for a given player, or create a file for them if it doesn't exist
tournament = 'genesis-invitational'


def addplayerdata(tournamentname):

	newdata = []         #create a dataframe that will be filled with the player's hole data from the tournament
	tournamentdata = pd.read_csv(tournamentname + '2021.csv')        #read in all the tournament data
	coursedata = pd.read_csv(tournamentname + 'course21.csv')        #read in all the tournament data
	extradata = pd.read_csv(tournamentname + 'additionalinfo2020.csv')     #read in additional tournament info
	tournamentdata = tournamentdata.drop(tournamentdata.columns[0], axis=1)   #drop the numerical index
	tournamentdata.set_index('0', inplace = True) #make the player name an index
	#tournamentdata.drop('0', axis = 1, inplace = True)
	print(tournamentdata.head())
	print(tournamentdata.dtypes)

	#print(type(tournamentdata.loc[playername],))
	#print(tournamentdata.columns.values.tolist())
	#for player in tournamentdata['0']:
	tournamentdata = tournamentdata.transpose().to_dict(orient = 'list') #create a dictionary with player names as keys and values are a list of tournament scores
	print(tournamentdata['Adam Scott'])
	#next section creates the hole data for each player in turn and adds it to the players' overall data
	#for player in tournamentdata.keys():
	for player in ['Adam Scott']:
		#start creating columns of data as lists
		thole = []
		tround = []
		scores = tournamentdata[player]
		for hole in range(len(scores)):
			tournamenthole = hole + 1
			roundhole = tournamenthole % 18
			if roundhole == 0:
				roundhole += 18
			thole.append(roundhole)
			round = (int(hole) // 18) + 1
			tround.append(round)
	

	playerscores = pd.DataFrame({'hole' : thole, 'roundnumber': tround, 'score': scores})
	courseinfo = coursedata[['hole','par','yards','averagescore']]
	playerrowstobeadded = pd.merge(playerscores, courseinfo, how='left', on='hole')
	location = extradata.loc[0,'location']
	day1 = extradata.loc[0,'startdate']
	day1 = datetime.strptime(day1, '%Y-%m-%d')
	playerrowstobeadded['location'] = location
	date =[]
	for round in tround:
		holedate = day1 + timedelta(days = (round - 1))
		date.append(holedate)
	print(len(date))
	playerrowstobeadded['date'] = date




	print('hi again')
	print(thole)
	print(tround)
	print(playerrowstobeadded)

	

		

	'''
	score = tournamentdata[tournamentdata['0'] == playername]
	print(score)
	print(type(score))
	for hole in range(1,73):
				
		print(str(score.iloc[0,(hole +1)]) + ' hole' + str(hole))

				#holedata = [tournamentname, 'dateholder', hole, ]
	'''

	'''
	with open( tournamentname + '.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
'''

addplayerdata(tournament)






