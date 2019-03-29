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

import gameboard as display
from setlists import SUM
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def GameLoop():
        # Game loop should keep track of whose turn it is
        # using the turn flag. We can then use this flag to
        # set up the functions in the Gamemanager file to
        # condense the fuctions that are currently seperated
        # like player and opp prize setups. At the begining of
        # the game we can  have a random number generator acting
        # as a coin to select who goes first and sets the flag.
        # Then all the setups will take place for that player then
        # change the flag and setup the next player and so on.
        # We just need to make sure we setup the boardstate before hand,
        # ie have prizes layed out and determine mulligans.

        
        turn = ''
        winner = False
        
        ## Initialize the gameboard
        #ui = display.Ui_MainWindow()
        gameboard = GameManager.Gameboard()

        gui = display.Ui_MainWindow()

        

        ## Populate player deck
        print("Starting player deck Population...")
        obj = GameManager.Card(card1)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card1)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card2)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card2)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card3)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card3)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card3)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card4)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card4)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card5)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card5)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        

        obj = GameManager.Card(card6)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card7)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card7)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card8)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card9)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card10)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card10)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card11)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card11)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card12)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card13)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card13)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card14)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card15)
        obj.setOwner('p')
        gameboard.playerDeck.append(obj)
        obj.setOwner('o')
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card15)
        obj.setOwner('p')
        gameboard.playerDeck.append(obj)
        obj.setOwner('o')
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card16)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card17)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        for i in range(3):
                obj = GameManager.Card(card18)
                gameboard.playerDeck.append(obj)
                gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card19)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card19)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card20)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card20)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card21)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card22)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card22)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        obj = GameManager.Card(card23)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card23)
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)

        for i in range(12):
                obj = GameManager.Card(card24)
                gameboard.playerDeck.append(obj)
                gameboard.oppDeck.append(obj)
        for i in range(8):
                obj = GameManager.Card(card25)
                gameboard.playerDeck.append(obj)
                gameboard.oppDeck.append(obj)

        print("Player deck created")


        def attackT():  #used to pass arguements
                gui.attack(gameboard)
        def retreatT():
                gui.retreat(gameboard, 0)


        gameboard.setup()
        #gameboard.playEnergy()
        #app = QtWidgets.QApplication(sys.argv)
        #MainWindow = QtWidgets.QMainWindow()
        #ui = Ui_MainWindow()
        #gui.setupUi(MainWindow)
        #gui.setActive()
        #gui.setBench()
        #gui.setPrize()
        #gui.setDiscard()
        #gui.setDeck()
        #gui.atkButton.clicked.connect(attackT)  #Doesn't allow the passing of arguements
        #gui.retreatButton.clicked.connect(retreatT)
        #gameboard.turn('p')
        ##MainWindow.show()
        ##sys.exit(app.exec_())
        while winner == False:
                turn = 'p'
                gameboard.turn(turn)
      

        
card1 = {'Name' : 'Solgaleo',
        'Card_Type' : 'Pokemon',
        'Stage' : 2,
        'Hp' : 160,
        'Power' : False,
        'Attack1Damage' : 0,
        'Attack1Name' : 'Shining Arrow',
        'Attack1Cost' : 'MC',
        'Attack2Damage' : 170,
        'Attack2Name' : 'Fangs of the Sunne',
        'Attack2Cost' : 'MMC',
        'RetreatCost' : 3,
        'Weakness' : 'R',
        'Resistance' : 'P'}



card2 = {'Name' : 'Cosmoem',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'Hp' : 90,
        'Power' : False,
        'Attack1Damage' : 0,
        'Attack1Name' : 'Teleport',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 3,
        'Weakness' : 'P',
        'Resistance' : ''}

card3 = {'Name' : 'Cosmog',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 0,
        'Attack1Name' : 'Dust Gathering',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'P',
        'Resistance' : ''}

card4 = {'Name' : 'Metang',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'Hp' : 90,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Name' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 80,
        'Attack2Name' : 'Core Beam',
        'Attack2Cost' : 'MMC',
        'RetreatCost' : 3,
        'Weakness' : 'R',
        'Resistance' : 'P'}

card5 = {'Name' : 'Beldum',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Name' : 'Core Beam',
        'Attack1Cost' : 'M',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'R',
        'Resistance' : 'P'}

card6 = {'Name' : 'Slowbro',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'Hp' : 110,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Name' : 'Amnesia',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 50,
        'Attack2Name' : 'Facade',
        'Attack2Cost' : 'PCC',
        'RetreatCost' : 3,
        'Weakness' : 'P',
        'Resistance' : ''}

card7 = {'Name' : 'Slowpoke',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 70,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 60,
        'Attack2Name' : 'Whimsy Tackle',
        'Attack2Cost' : 'PCC',
        'RetreatCost' : 3,
        'Weakness' : 'P',
        'Resistance' : ''}

card8 = {'Name' : 'Dhelmise',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 120,
        'Power' : True,
        'Attack1Damage' : 70,
        'Attack1Name' : 'Anchor Shot',
        'Attack1Cost' : 'PCC',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 2,
        'Weakness' : 'D',
        'Resistance' : 'F'}

card9 = {'Name' : 'Oricorio',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 90,
        'Power' : True,
        'Attack1Damage' : 30,
        'Attack1Name' : '',
        'Attack1Cost' : 'PC',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'P',
        'Resistance' : ''}

card10 = {'Name' : 'Bewear',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'Hp' : 130,
        'Power' : False,
        'Attack1Damage' : 60,
        'Attack1Name' : 'Dangerous Blow',
        'Attack1Cost' : 'CCC',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 2,
        'Weakness' : 'F',
        'Resistance' : ''}

card11 = {'Name' : 'Stufful',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 70,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 60,
        'Attack2Name' : '',
        'Attack2Cost' : 'CCC',
        'RetreatCost' : 2,
        'Weakness' : 'F',
        'Resistance' : ''}

card12 = {'Name' : 'Swellow',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'Hp' : 90,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Name' : 'Agility',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 40,
        'Attack2Name' : 'Swallow Dive',
        'Attack2Cost' : 'C',
        'RetreatCost' : 1,
        'Weakness' : 'L',
        'Resistance' : 'F'}

card13 = {'Name' : 'Taillow',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Name' : 'Reckless Charge',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'L',
        'Resistance' : 'F'}

card14 = {'Name' : 'Castform',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 70,
        'Power' : False,
        'Attack1Damage' : 0,
        'Attack1Name' : 'Weather Teller',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 30,
        'Attack2Name' : 'Water Pulse',
        'Attack2Cost' : 'CC',
        'RetreatCost' : 1,
        'Weakness' : 'F',
        'Resistance' : ''}

card15 = {'Name' : 'Altar of the Sunne',
        'Card_Type' : 'Stadium',
        'Name' : ''}

card16 = {'Name' : 'Big Malasada',
        'Card_Type' : 'Item',
        'Name' : ''}

card17 = {'Name' : 'Energy Retrieval',
        'Card_Type' : 'Item',
        'Name' : ''}

card18 = {'Name' : 'Hau',
        'Card_Type' : 'Supporter',
        'Name' : ''}

card19 = {'Name' : 'Nest Ball',
        'Card_Type' : 'Item',
        'Name' : ''}

card20 = {'Name' : 'Professor Kukui',
        'Card_Type' : 'Supporter',
        'Name' : ''}

card21 = {'Name' : 'Rescue Stretcher',
        'Card_Type' : 'Item',
        'Name' : ''}

card22 = {'Name' : 'Switch',
        'Card_Type' : 'Item',
        'Name' : ''}

card23 = {'Name' : 'Timer Ball',
        'Card_Type' : 'Item',
        'Name' : ''}

card24 = {'Name' : 'Metal Energy',
        'Card_Type' : 'Energy',
        'Name' : ''}

card25 = {'Name' : 'Psychic Energy',
        'Card_Type' : 'Energy',
        'Name' : ''}



## MAIN ##

#GameLoop()



        
