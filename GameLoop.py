######################################################
##                 Project Vulpix                   ##
##                Senior Project 2                  ##
##                 Andrew Siddall                   ##
##                 Chris Crisson                    ##
##               Matthew Bedillion                  ##
##               Adlene Bellaoucha                  ##
##               January 31, 2019                   ##
######################################################

###################DESCRIPTION########################
## This file will run a main game loop 

import SetListTest
import GameManager
from setlists import SUM

class GameLoop():
	## Initialize the gameboard
	gameboard = GameManager.Gameboard()
	
	## Populate player deck
	for i in range(60):
		obj = GameManager.Card(SUM.SUM001)
		gameboard.playerDeck.append(obj)

	for i in gameboard.playerDeck:
		print(i.Name)