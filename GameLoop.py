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

def GameLoop():
        ## Initialize the gameboard
        gameboard = GameManager.Gameboard()

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
        gameboard.playerDeck.append(obj)
        gameboard.oppDeck.append(obj)
        obj = GameManager.Card(card15)
        gameboard.playerDeck.append(obj)
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

        

        gameboard.setup()
        gameboard.attackDamage(gameboard.playerHand[1], 10)

card1 = {'Name' : 'Solgaleo',
        'Card_Type' : 'Pokemon',
        'Stage' : 2,
        'Hp' : 160,
        'Power' : False,
        'Attacl1Damage' : 0,
        'Attack1Effect' : '',
        'Attack1Cost' : 'MC',
        'Attacl2Damage' : 170,
        'Attack2Effect' : '',
        'Attack2Cost' : 'MMC',
        'RetreatCost' : 3,
        'Weakness' : 'R',
        'Resistance' : 'P'}



card2 = {'Name' : 'Cosmoem',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'Hp' : 90,
        'Power' : False,
        'Attacl1Damage' : 0,
        'Attack1Effect' : 'Switch this Pokémon with 1 of your Benched Pokémon',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 0,
        'Attack2Effect' : 'None',
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
        'Attack1Effect' : 'Draw a card',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 0,
        'Attack2Effect' : 'None',
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
        'Attack1Effect' : 'None',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 80,
        'Attack2Effect' : 'None',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'M',
        'Attack2Damage' : 0,
        'Attack2Effect' : 'None',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 50,
        'Attack2Effect' : '',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 60,
        'Attack2Effect' : '',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'PCC',
        'Attack2Damage' : 0,
        'Attack2Effect' : '',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'PC',
        'Attack2Damage' : 0,
        'Attack2Effect' : '',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'CCC',
        'Attack2Damage' : 0,
        'Attack2Effect' : '',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 60,
        'Attack2Effect' : '',
        'Attack2Cost' : 'None',
        'RetreatCost' : 2,
        'Weakness' : 'F',
        'Resistance' : ''}

card12 = {'Name' : 'Swellow',
        'Card_Type' : 'Pokemon',
        'Stage' : 1,
        'Hp' : 90,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Effect' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 40,
        'Attack2Effect' : '',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'L',
        'Resistance' : 'F'}

card13 = {'Name' : 'Taillow',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 20,
        'Attack1Effect' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 0,
        'Attack2Effect' : '',
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
        'Attack1Effect' : '',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 30,
        'Attack2Effect' : '',
        'Attack2Cost' : 'CC',
        'RetreatCost' : 1,
        'Weakness' : 'F',
        'Resistance' : ''}

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

GameLoop()


        
