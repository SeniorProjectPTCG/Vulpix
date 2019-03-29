import random

def nestBall(self, turn):
	if turn == 'p':
		for i in len(self.playerDeck):
			choiceList = []
			if self.playerDeck[i].isBasic:
				choiceList.append(i)
		counter = 1
		for i in choiceList:
			print(str(counter) + " " + str(self.playerDeck[i].Name))
			counter += 1
		input(choice)
		self.playerBench.append(self.playerDeck.pop(choiceList[choice]))
	elif turn == 'o':
		for i in len(self.oppDeck):
			choiceList = []
			if self.oppDeck[i].isBasic:
				choiceList.append(i)
		counter = 1
		for i in choiceList:
			print(str(counter) + " " + str(self.oppDeck[i].Name))
			counter += 1
		input(choice)
		self.oppBench.append(self.oppDeck.pop(choiceList[choice]))

def timerBall(self, turn):
	counter = 0
	for i in range(2):
		x = random.randint(0,1)
		if x == 1:
			counter += 1
	for i in range(counter):
		choiceList = []
		if turn == 'p':
			for i in len(self.playerDeck):
				if self.playerDeck[i].Card_Type == "Pokemon":
					choiceList.append(i)
			for i in choiceList:
				print(str(counter) + " " + str(self.playerDeck[i].Name))
				counter += 1
			input(choice)
			self.playerHand.append(self.playerDeck.pop[choiceList[choice]])
		if turn == 'o':
			for i in len(self.oppDeck):
				if self.oppDeck[i].Card_Type == "Pokemon":
					choiceList.append(i)
			for i in choiceList:
				print(str(counter) + " " + str(self.oppDeck[i].Name))
				counter += 1
			input(choice)
			self.oppHand.append(self.oppDeck.pop[choiceList[choice]])

def bigMalasada(self, turn):
	if turn == 'p':
		self.playerActive[0].Hp += 20
		self.playerBurned = False
		self.playerParalyzed = False
		self.playerPoisoned = False
		self.playerAsleep = False
		self.playerConfused = False
	elif turn == 'o':
		self.oppActive[0].Hp += 20
		self.oppBurned = False
		self.oppParalyzed = False
		self.oppPoisoned = False
		self.oppAsleep = False
		self.oppConfused = False

def energyRetreival(self, turn):
	energyList = []
	count = 0
	if turn == 'p':
		for i in len(self.playerDiscard):
			if self.playerDiscard[i].Card_Type == "Energy":
				energyList.append(i)
		while (count < 2) and (len(energyList) > 0):
			self.playerHand.append(self.playerDiscard.pop(energyList[0]))
			count += 1
	elif turn == 'o':
		for i in len(self.oppDiscard):
			if self.oppDiscard[i].Card_Type == "Energy":
				energyList.append(i)
		while (count < 2) and (len(energyList) > 0):
			self.oppHand.append(self.oppDiscard.pop(energyList[0]))
			count += 1

def hau(self, turn):
	if turn == 'p':
		for i in range(3):
			self.playerDrawCard()
	elif turn == 'o':
		for i in range(3):
			self.oppDrawCard()

def professorKukui(turn):
	if turn == 'p':
		for i in range(2): 
			self.playerDrawCard()
	if turn == 'o':
		for i in range(2):
			self.oppDrawCard()
	bonusDamage += 20

# NEED TO CHECK IF POKEMON IN DISCARD BEFORE CALLING !!!
def rescueStretcher(self, turn):
	choice = random.randint(1,2)
	pokemonList = []
	if turn == 'p':
		for i in len(self.playerDiscard):
			if self.playerDiscard[i].Card_Type == "Pokemon":
				pokemonList.append(i)
		if choice == 1:
			choice == random.randint(0,len(pokemonList))
			self.playerHand.append(self.playerDiscard.pop(pokemonList[choice]))
		elif choice == 2:
			count = 0
			while (count < 4) and (len(pokemonList) > 0):
				self.playerDeck.append(self.playerDiscard.pop(pokemonList[0]))
				trash = pokemonList.pop(0)
				count += 1
			random.shuffle(self.playerdeck)
	elif turn == 'o':
		for i in len(self.oppDiscard):
			if self.oppDiscard[i].Card_Type == "Pokemon":
				pokemonList.append(i)
		if choice == 1:
			choice == random.randint(0,len(pokemonList))
			self.oppHand.append(self.oppDiscard.pop(pokemonList[choice]))
		elif choice == 2:
			count = 0
			while (count < 4) or (len(pokemonList) > 0):
				self.oppDeck.append(self.oppDiscard.pop(pokemonList[0]))
				trash = pokemonList.pop(0)
				count += 1
			random.shuffle(self.oppDeck) 