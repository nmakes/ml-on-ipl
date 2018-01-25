import csv

dataset_folder = "../dataset/"

delivFile = 'deliveries.csv'
matchFile = 'matches.csv'


# MATCHES ANALYSIS

with open(dataset_folder+matchFile) as matchesCSV:

	reader = csv.reader(matchesCSV)

	headerFlag = True
	header = []
	datas = []

	for line in reader:

		if headerFlag == True:
			header = line
			headerFlag = False

		else:
			
			data = {}

			for i in range(len(header)):
				
				key = header[i]
				data[key] = line[i]

			datas.append(data)

	# Find winRatio
	winnerCount = {}
	gameCount = {}
	winRatio = {}

	for data in datas:

		winner = data['winner']
		
		team1 = data['team1']
		team2 = data['team2']

		if team1 in gameCount:
			gameCount[team1] += 1
		else:
			gameCount[team1] = 1

		if team2 in gameCount:
			gameCount[team2] += 1
		else:
			gameCount[team2] = 1

		if winner in winnerCount:
			winnerCount[winner] += 1
		else:
			winnerCount[winner] = 1

	for team in gameCount:

		winRatio[team] = float(winnerCount[team])/float(gameCount[team])

	'''
	for key, value in sorted(winRatio.iteritems(), key=lambda (k,v): (v,k)):
	    print "%s: %s" % (key, value)
	'''

	# Find player of the match
	pomCount = {}
	
	for data in datas:

		pom = data['player_of_match']

		if pom in pomCount:
			pomCount[pom] += 1
		else:
			pomCount[pom] = 1
	
	'''
	for key, value in sorted(pomCount.iteritems(), key=lambda (k,v): (v,k)):
		print "%s: %s" % (key, value)
	'''

	histogram = {}

	for player in pomCount:

		count = pomCount[player]

		if count in histogram:
			histogram[count] += 1
		else:
			histogram[count] = 1

	for key in sorted(histogram.keys()):
		print str(key) + ": " + str(histogram[key])

	import matplotlib.pyplot as plt

	X = histogram.keys()
	Y = []

	for k in X:
		Y.append(histogram[k])

	plt.scatter(X,Y)
	plt.xlabel('number of player_of_match awards')
	plt.ylabel('number of players')
	plt.show()