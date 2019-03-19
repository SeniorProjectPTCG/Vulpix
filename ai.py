from random import randint
def ai(gameboard):
	print(gameboard)
	for i in range(len(gameboard.playerHand)):
		if gameboard.playerHand[i].Card_Type == "Energy":
			if gameboard.energyPlayed == "False":
				return 3
		else:
			return 6
