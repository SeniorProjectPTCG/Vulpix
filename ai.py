from random import randint
def ai(gameboard):
	for i in range(len(gameboard.playerHand)):
		if (gameboard.playerIsBasic(i)) and (len(gameboard.playerBench) < 6):
			print("ai player is playing basic")
			input("press enter")
			return 1
		if gameboard.playerHand[i].Card_Type == "Energy":
			if gameboard.energyPlayed == "False":
				return 3
		else:
			return 6
