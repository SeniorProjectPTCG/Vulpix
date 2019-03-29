def nestBall(turn):
	if turn == 'p':
		for i in len(playerDeck):
			choiceList = []
			if playerDeck[i].isBasic:
				choiceList.append(i)
		counter = 1
		for i in choiceList:
			print(str(counter) + " " + str(playerDeck[i].Name))
			counter += 1
		input(choice)
		playerBench.append(playerDeck.pop(choiceList[choice]))
	elif turn == 'o':
		for i in len(oppDeck):
			choiceList = []
			if oppDeck[i].isBasic:
				choiceList.append(i)
		counter = 1
		for i in choiceList:
			print(str(counter) + " " + str(oppDeck[i].Name))
			counter += 1
		input(choice)
		oppBench.append(oppDeck.pop(choiceList[choice]))

def timerBall(turn):
	counter = 0
	for i in range(2):
		x = randint(0,1)
		if x == 1:
			counter += 1
	for i in range(counter):
		choiceList = []
		if turn == 'p':
			for i in len(playerDeck):
				if playerDeck[i].Card_Type == "Pokemon":
					choiceList.append(i)
			for i in choiceList:
				print(str(counter) + " " + str(playerDeck[i].Name))
				counter += 1
			input(choice)
			playerHand.append(playerDeck.pop[choiceList[choice]])
		if turn == 'o':
			for i in len(oppDeck):
				if oppDeck[i].Card_Type == "Pokemon":
					choiceList.append(i)
			for i in choiceList:
				print(str(counter) + " " + str(oppDeck[i].Name))
				counter += 1
			input(choice)
			oppHand.append(oppDeck.pop[choiceList[choice]])

def bigMalasada(turn):
	if turn == 'p':
		playerActive[0].Hp += 20
		playerBurned = False
		playerParalyzed = False
		playerPoisoned = False
		playerAsleep = False
		playerConfused = False
	elif turn == 'o':
		oppActive[0].Hp += 20
		oppBurned = False
		oppParalyzed = False
		oppPoisoned = False
		oppAsleep = False
		oppConfused = False

def energyRetreival(turn):
	pass

def hau(turn):
	if turn == 'p':
		for i in range(3):
			playerDrawCard()
	elif turn == 'o':
		for i in range(3):
			oppDrawCard()

def professorKukui(turn):
	if turn == 'p':
		for i in range(2):
			playerDrawCard()
	if turn == 'o':
		for i in range(2):
			oppDrawCard()
	bonusDamage += 20

# NEED TO CHECK IF POKEMON IN DISCARD BEFORE CALLING !!!
def rescueStretcher(turn):
	choice = randint(1,2)
	pokemonList = []
	if turn == 'p':
		for i in len(playerDiscard):
			if playerDiscard[i].Card_Type == "Pokemon":
				pokemonList.append(i)
		if choice == 1:
			choice == randint(0,len(pokemonList))
			playerHand.append(playerDiscard.pop(pokemonList[choice]))
		elif choice == 2:
			count = 0
			while (count < 4) or (len(pokemonList) > 0):
				playerDeck.append(playerDiscard.pop(pokemonList[0]))
				trash = pokemonList.pop(0)
				count += 1
			playerDeck.shuffle()
	elif turn == 'o':
		for i in len(oppDiscard):
			if oppDiscard[i].Card_Type == "Pokemon":
				pokemonList.append(i)
		if choice == 1:
			choice == randint(0,len(pokemonList))
			oppHand.append(oppDiscard.pop(pokemonList[choice]))
		elif choice == 2:
			count = 0
			while (count < 4) or (len(pokemonList) > 0):
				oppDeck.append(oppDiscard.pop(pokemonList[0]))
				trash = pokemonList.pop(0)
				count += 1
			oppDeck.shuffle()