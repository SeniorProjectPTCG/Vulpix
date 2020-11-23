from GameLoop import *
import GameManager
import attacks
import items
import mcts

playerWins = 0
oppWins = 0
go = True

while go == True:
	print("What is the players active pokemon?")
	temp = input()
	flag = True
	i = 0
	while flag or i < len(playerDeck):
		print(gameboard.playerDeck[i].Name)


