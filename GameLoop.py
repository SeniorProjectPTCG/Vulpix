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

#import gameboard as display
from setlists import SUM
#from PyQt5 import QtCore, QtGui, QtWidgets
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

        #gui = display.Ui_MainWindow()

        

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


##        def attackT():  #used to pass arguements
##                gui.attack(gameboard)
##        def retreatT():
##                gui.retreat(gameboard, 0)
##

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
        'PreEvolution' : 'Cosmoem',
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
        'Resistance' : 'P',
        'Pokemon_Type' : 'M'}



card2 = {'Name' : 'Cosmoem',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Cosmog',
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
        'Resistance' : '',
        'Pokemon_Type' : 'P'}

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
        'Resistance' : '',
        'Pokemon_Type' : 'P'}

card4 = {'Name' : 'Metang',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Beldum',
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
        'Resistance' : 'P',
        'Pokemon_Type' : 'M'}

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
        'Resistance' : 'P',
        'Pokemon_Type' : 'M'}

card6 = {'Name' : 'Slowbro',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Slowpoke',
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
        'Resistance' : '',
        'Pokemon_Type' : 'P'}

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
        'Resistance' : '',
        'Pokemon_Type' : 'P'}

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
        'Resistance' : 'F',
        'Pokemon_Type' : 'P'}

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
        'Resistance' : '',
        'Pokemon_Type' : 'P'}

card10 = {'Name' : 'Bewear',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Stufful',
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
        'Resistance' : '',
        'Pokemon_Type' : 'C'}

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
        'Resistance' : '',
        'Pokemon_Type' : 'C'}

card12 = {'Name' : 'Swellow',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Taillow',
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
        'Resistance' : 'F',
        'Pokemon_Type' : 'C'}

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
        'Resistance' : 'F',
        'Pokemon_Type' : 'C'}

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
        'Resistance' : '',
        'Pokemon_Type' : 'C'}

card15 = {'Name' : 'Altar of the Sunne',
        'Card_Type' : 'Stadium',
        'Effect' : ''}

card16 = {'Name' : 'Big Malasada',
        'Card_Type' : 'Item',
        'Effect' : ''}

card17 = {'Name' : 'Energy Retrieval',
        'Card_Type' : 'Item',
        'Effect' : ''}

card18 = {'Name' : 'Hau',
        'Card_Type' : 'Supporter',
        'Effect' : ''}

card19 = {'Name' : 'Nest Ball',
        'Card_Type' : 'Item',
        'Effect' : ''}

card20 = {'Name' : 'Professor Kukui',
        'Card_Type' : 'Supporter',
        'Effect' : ''}

card21 = {'Name' : 'Rescue Stretcher',
        'Card_Type' : 'Item',
        'Effect' : ''}

card22 = {'Name' : 'Switch',
        'Card_Type' : 'Item',
        'Effect' : ''}

card23 = {'Name' : 'Timer Ball',
        'Card_Type' : 'Item',
        'Effect' : ''}

card24 = {'Name' : 'Metal Energy',
        'Card_Type' : 'Energy',
        'Effect' : ''}

card25 = {'Name' : 'Psychic Energy',
        'Card_Type' : 'Energy',
        'Effect' : ''}

card26 = {'Name' : 'Gothita',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 0,
        'Attack1Name' : 'Blown Kiss',
        'Attack1Cost' : 'P',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'PP',
        'Resistance' : '',
        'Pokemon_Type' : 'P'}

card27 = {'Name' : 'Gothorita',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Gothita',
        'Hp' : 80,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Name' : 'Slap',
        'Attack1Cost' : 'P',
        'Attack2Damage' : 30,
        'Attack2Name' : 'Psybeam',
        'Attack2Cost' : 'PC',
        'RetreatCost' : 2,
        'Weakness' : 'PP',
        'Resistance' : '',
        'Pokemon_Type' : 'C'}

card28 = {'Name' : 'Litwick',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 50,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : 'Flickering Flames',
        'Attack1Cost' : 'F',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'WW',
        'Resistance' : '',
        'Pokemon_Type' : 'F'}

card29 = {'Name' : 'Lampent',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Litwick',
        'Hp' : 80,
        'Power' : False,
        'Attack1Damage' : 30,
        'Attack1Name' : 'Will-O-Wisp',
        'Attack1Cost' : 'F',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'WW',
        'Resistance' : '',
        'Pokemon_Type' : 'F'}

card30 = {'Name' : 'Lunala',
        'Card_Type' : 'Pokemon',
        'Stage' : 2,
        'PreEvolution' : 'Cosmoem',
        'Hp' : 160,
        'Power' : False,
        'Attack1Damage' : 40,                            #x40
        'Attack1Name' : 'Shatter Shot',
        'Attack1Cost' : 'P',
        'Attack2Damage' : 130,
        'Attack2Name' : 'Wings of the Moone',
        'Attack2Cost' : 'PPP',
        'RetreatCost' : 2,
        'Weakness' : '',                                 #Wasn't able to recognize it
        'Resistance' : '',                               #Wasn't able to recognize it 
        'Pokemon_Type' : 'P'}  

card31 = {'Name' : 'Salandit',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 70,
        'Power' : False,
        'Attack1Damage' : 10,                            
        'Attack1Name' : 'Scratch',
        'Attack1Cost' : 'F',
        'Attack2Damage' : 20,                            #+20
        'Attack2Name' : 'Venoshock',
        'Attack2Cost' : 'CC',
        'RetreatCost' : 1,
        'Weakness' : 'WW',
        'Resistance' : '',
        'Pokemon_Type' : 'F'}

card32 = {'Name' : 'Salazzle',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'PreEvolution' : 'Salandit',
        'Hp' : 110,
        'Power' : False,
        'Attack1Damage' : 90,
        'Attack1Name' : 'Flamethrower',
        'Attack1Cost' : 'FCC',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'WW',
        'Resistance' : '',
        'Pokemon_Type' : 'F'}

card33 = {'Name' : 'Mimikyu',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 70,
        'Power' : False,
        'Attack1Damage' : 0,            #Special attack
        'Attack1Name' : 'Filch',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 0,
        'Attack2Name' : 'Copycat',
        'Attack2Cost' : 'PC',
        'RetreatCost' : 1,
        'Weakness' : '',
        'Resistance' : '',
        'Pokemon_Type' : 'P'}

## MAIN ##

GameLoop()



        
