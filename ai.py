from random import randint
def playerAI(gameboard):
	for i in range(len(gameboard.playerHand)):
		if (gameboard.playerIsBasic(i)) and (len(gameboard.playerBench) < 6):
			print("ai player is playing basic")
			return 1
		if gameboard.playerHand[i].Card_Type == "Energy":
			if gameboard.energyPlayed == "False":
				return 3
		else:
			return 6
def oppAI(gameboard):
	for i in range(len(gameboard.oppHand)):
		if (gameboard.oppIsBasic(i)) and (len(gameboard.oppBench) < 6):
			print("ai opponent is playing basic")
			return 1
		if gameboard.oppHand[i].Card_Type == "Energy":
			if gameboard.energyPlayed == "False":
				return 3
		else:
			return 6