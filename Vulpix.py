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

import GameManager
import mcts
import sys

def newGame():
        input("Press enter to start a new game")
        GameLoop()

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
        #Start a new game
        
        
        turn = ''
        winner = False
        
        ## Initialize the gameboard
        gameboard = GameManager.Gameboard()
        ## Initialize the decks
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

        # Set the gameboard to the default state
        gameboard.setup()

        #Control game
        go = True

        while go == True:
                
                # Get players board state from the user
                getPlayerActive(gameboard)
                
                # Get players benched pokemon
                getPlayerBench(gameboard)

                #Get player's hand
                getPlayerHand(gameboard)

                #Get player's discard
                getPlayerDiscard(gameboard)

                #Get stadium in play
                getStadium(gameboard)

                #get player's prizes
                getPlayerPrize(gameboard)

                # Get opponents active pokemon
                getOppActive(gameboard)

                #Get opponent's benched pokemon
                getOppBench(gameboard)

                #Get opponents discard
                getOppDiscard(gameboard)

                #Get opponent's hand
                getOppHand(gameboard)

                #Get opponents prizes
                getOppPrize(gameboard)

                ## Check for win condition
                gameOver = gameboard.checkWinCon(gameboard.turn)
                if gameOver != 1 and gameOver != 0:
                        selectedMove = str(mcts.uct(gameboard,50))
                        move = parseMove(selectedMove)
                        print("The suggested move is " + move)
                elif gameOver == 1:
                        print("Player has won")
                        newGame()
                elif gameOver == 0:
                        print("Opponent has won")
                        newGame()

                del gameboard
                input("Press enter to continue.")
                GameLoop()

# Parse the move object to display the move in a user friendly way
def parseMove(move):
        temp = move
        string = ""
        done = False
        i = 0
        #Find period in the string
        while done == False:
                if temp[i] == ".":
                        done = True
                i += 1
        done = False
        #Find captal letter to denote new word
        while done == False:
                if temp[i].isupper():
                        string = string + " " + temp[i].lower()
                elif temp[i] != ' ':
                        string = string + temp[i]
                else:
                        done = True
                i += 1
        return string

# The following functions get the gamestate information
# from the user
def getStadium(gameboard):
        entered = True
        while entered == True:
                print("What stadium is in play?")
                temp = input()
                if temp == '':
                        entered = False
                else:
                        print("Who played the stadium?")
                        temp2 = input()
                        i = 0
                        found = False
                        end = False
                        if temp2 == 'p':
                                while found == False and end == False:
                                        if i >= len(gameboard.playerDeck):
                                                print("Not found")
                                                end = True
                                        elif temp.upper() == gameboard.playerDeck[i].Name.upper():
                                                gameboard.stadium.append(gameboard.playerDeck.pop(i))
                                                found = True
                                                entered = False #Exit the loop
                                        i += 1
                        elif temp2 == 'o':
                                while found == False and end == False:
                                        if i >= len(gameboard.oppDeck):
                                                print("Not found")
                                                end = True
                                        elif temp.upper() == gameboard.oppDeck[i].Name.upper():
                                                gameboard.stadium.append(gameboard.oppDeck.pop(i))
                                                found = True
                                                #exit the loop
                                                entered = False
                                        i += 1

def getPlayerPrize(gameboard):
        goodData = False
        while goodData == False:
                print("How many prizes does the player have left")
                temp = input()
                if temp == '':
                        temp = 1
                try:
                        x = int(temp)
                        goodData = True
                        for i in range(x):
                                if len(gameboard.playerDeck) > 0:
                                        gameboard.playerPrize.append(gameboard.playerDeck.pop(0))
                except Exception as e:
                        print("You must enter a numerical value")
        
        

def getOppPrize(gameboard):
        print("How many prizes does the opponent have left?")
        temp = input()
        if temp == '':
                temp = 1
        x = int(temp)
        for i in range(x):
                if len(gameboard.oppDeck) > 0:
                        gameboard.oppPrize.append(gameboard.oppDeck.pop(0))

def getPlayerHand(gameboard):
        entered = True
        more = True
        i = 0
        while more == True:
                while entered == True:
                        print("What card is in the players hand?")
                        temp = input()
                        if temp == '':
                                entered = False
                                more = False
                        else:
                                i = 0
                                found = False
                                end = False
                                while found == False and end == False:
                                        if i >= len(gameboard.playerDeck):
                                                print("Not found")
                                                end = True
                                        elif temp.upper() == gameboard.playerDeck[i].Name.upper():
                                                gameboard.playerHand.append(gameboard.playerDeck.pop(i))
                                                found = True
                                        i += 1

def getOppHand(gameboard):
        print("How many cards are in the opponent's hand")
        temp = input()
        if temp == '':
                temp = 0
        x = int(temp)
        for i in range(x):
                if len(gameboard.oppDeck) > 0:
                        gameboard.oppHand.append(gameboard.oppDeck.pop(0))

def getPlayerDiscard(gameboard):
        entered = True
        more = True
        i = 0
        while more == True:
                while entered == True:
                        print("What card is in the players discard?")
                        temp = input()
                        if temp == '':
                                entered = False
                                more = False
                        else:
                                i = 0
                                found = False
                                end = False
                                while found == False and end == False:
                                        if i >= len(gameboard.playerDeck):
                                                print("Not found")
                                                end = True
                                        elif temp.upper() == gameboard.playerDeck[i].Name.upper():
                                                gameboard.playerDiscard.append(gameboard.playerDeck.pop(i))
                                                found = True
                                        i += 1

def getOppDiscard(gameboard):
        entered = True
        more = True
        i = 0
        while more == True:
                while entered == True:
                        print("What card is in the opponent's discard?")
                        temp = input()
                        if temp == '':
                                entered = False
                                more = False
                        else:
                                i = 0
                                found = False
                                end = False
                                while found == False and end == False:
                                        if i >= len(gameboard.playerDeck):
                                                print("Not found")
                                                end = True
                                        elif temp.upper() == gameboard.oppDeck[i].Name.upper():
                                                gameboard.oppDiscard.append(gameboard.oppDeck.pop(i))
                                                found = True
                                        i += 1

def getPlayerActive(gameboard):
        flag = True
        i = 0
        print("What is the players active pokemon?")
        temp = input()
        while flag == True:
                if i >= len(gameboard.playerDeck):
                        print("Not found. What is the players active pokemon?")
                        i = -1
                        temp = input()
                if temp.upper() == gameboard.playerDeck[i].Name.upper():
                        flag = False
                        gameboard.playerActive.append(gameboard.playerDeck.pop(i))
                        # Handle evolved pokemon
                        if gameboard.playerActive[0].Stage == 2:
                                i = 0
                                foundS1 = False
                                while i < len(gameboard.playerDeck) and foundS1 == False:
                                        if gameboard.playerActive[0].PreEvolution.upper() == gameboard.playerDeck[i].Name.upper():
                                                gameboard.playerActive[0].Pokemon.append(gameboard.playerDeck.pop(i))
                                                foundS1 = True
                                        i += 1
                                i = 0 
                                foundS0 = False
                                while i < len(gameboard.playerDeck) and foundS0 == False:
                                        if gameboard.playerActive[0].Pokemon[0].PreEvolution.upper() == gameboard.playerDeck[i].Name.upper():
                                                print(gameboard.playerActive[0].Pokemon[0].PreEvolution.upper())
                                                print(gameboard.playerDeck[i].Name.upper())
                                                gameboard.playerActive[0].Pokemon[0].Pokemon.append(gameboard.playerDeck.pop(i))
                                                foundS0 = True
                                        i += 1
                        elif gameboard.playerActive[0].Stage == 1:
                                i = 0
                                foundS0 = False
                                while i < len(gameboard.playerDeck) and foundS0 == False:
                                        if gameboard.playerActive[0].PreEvolution.upper() == gameboard.playerDeck[i].Name.upper():
                                                gameboard.playerActive[0].Pokemon.append(gameboard.playerDeck.pop(i))
                                                foundS0 = True
                                        i += 1
                i += 1
        #Get energy for active
        entered = True
        found = True
        if entered == True and found == True:
                moreEnergy = True
                while moreEnergy == True:
                        print("What energy is attached to the active Pokemon?")
                        temp = input()
                        if temp == '':
                                moreEnergy = False
                        else:
                                i = 0
                                found = False
                                end = False
                                while found == False and end == False:
                                        if i >= len(gameboard.playerDeck):
                                                print("Not found.")
                                                end = True
                                                i = -1
                                        elif temp.upper() == gameboard.playerDeck[i].Name.upper():
                                                found = True
                                                gameboard.playerActive[0].Energies.append(gameboard.playerDeck.pop(i))
                                        i += 1
        #Get damage for active
        print("How much damage is on the player's active pokemon?")
        temp = input()
        if temp == '':
                temp = 0
        gameboard.playerActive[0].Hp -= int(temp)

def getOppActive(gameboard):
        flag = True
        i = 0
        print("What is the opponent's active pokemon?")
        temp = input()
        while flag == True:
                if i >= len(gameboard.oppDeck):
                        print("Not found. What is the opponent's active pokemon?")
                        i = -1
                        temp = input()
                if temp.upper() == gameboard.oppDeck[i].Name.upper():
                        flag = False
                        gameboard.oppActive.append(gameboard.oppDeck.pop(i))
                        #Handle evolved pokemon
                        if gameboard.oppActive[0].Stage == 2:
                                i = 0
                                foundS1 = False
                                while i < len(gameboard.oppDeck) and foundS1 == False:
                                        if gameboard.oppActive[0].PreEvolution.upper() == gameboard.oppDeck[i].Name.upper():
                                                gameboard.oppActive[0].Pokemon.append(gameboard.oppDeck.pop(i))
                                                foundS1 = True
                                        i += 1
                                i = 0 
                                foundS0 = False
                                while i < len(gameboard.oppDeck) and foundS0 == False:
                                        if gameboard.oppActive[0].Pokemon[0].PreEvolution.upper() == gameboard.oppDeck[i].Name.upper():
                                                gameboard.oppActive[0].Pokemon[0].Pokemon.append(gameboard.oppDeck.pop(i))
                                                foundS0 = True
                                        i += 1
                        elif gameboard.oppActive[0].Stage == 1:
                                i = 0
                                foundS0 = False
                                while i < len(gameboard.oppDeck) and foundS0 == False:
                                        if gameboard.oppActive[0].PreEvolution.upper() == gameboard.oppDeck[i].Name.upper():
                                                gameboard.oppActive[0].Pokemon.append(gameboard.oppDeck.pop(i))
                                                foundS0 = True
                                        i += 1
                i += 1
        #Get energy for active
        entered = True
        found = True
        if entered == True and found == True:
                moreEnergy = True
                while moreEnergy == True:
                        print("What energy is attached to the active Pokemon?")
                        temp = input()
                        if temp == '':
                                moreEnergy = False
                        else:
                                i = 0
                                found = False
                                end = False
                                while found == False and end == False:
                                        if i >= len(gameboard.oppDeck):
                                                print("Not found.")
                                                end = True
                                                i = -1
                                        elif temp.upper() == gameboard.oppDeck[i].Name.upper():
                                                found = True
                                                gameboard.oppActive[0].Energies.append(gameboard.oppDeck.pop(i))
                                        i += 1
        #Get damage for active
        print("How much damage is on the opponent's active pokemon?")
        temp = input()
        if temp == '':
                temp = 0
        gameboard.oppActive[0].Hp -= int(temp)

def getPlayerBench(gameboard):
        morePokemon = True
        benchIndex = 0
        while morePokemon == True and benchIndex < 5:
                print("What is the players benched pokemon?")
                temp = input()
                entered = True
                if temp == '':
                        morePokemon = False
                        entered = False
                else:
                        i = 0
                        found = False
                        end = False
                        while found == False and end == False:
                                if i >= len(gameboard.playerDeck):
                                        print("Not found.")
                                        end = True
                                        i = -1
                                elif temp.upper() == gameboard.playerDeck[i].Name.upper():
                                        found = True
                                        gameboard.playerBench.append(gameboard.playerDeck.pop(i))
                                        #Handle evolved pokemon
                                        if gameboard.playerBench[benchIndex].Stage == 2:
                                                i = 0
                                                foundS1 = False
                                                while i < len(gameboard.playerDeck) and foundS1 == False:
                                                        if gameboard.playerBench[benchIndex].PreEvolution.upper() == gameboard.playerDeck[i].Name.upper():
                                                                gameboard.playerBench[benchIndex].Pokemon.append(gameboard.playerDeck.pop(i))
                                                                foundS1 = True
                                                        i += 1
                                                i = 0 
                                                foundS0 = False
                                                while i < len(gameboard.playerDeck) and foundS0 == False:
                                                        if gameboard.playerBench[benchIndex].Pokemon[0].PreEvolution.upper() == gameboard.playerDeck[i].Name.upper():
                                                                gameboard.playerBench[benchIndex].Pokemon[0].Pokemon.append(gameboard.playerDeck.pop(i))
                                                                foundS0 = True
                                                        i += 1
                                        elif gameboard.playerBench[benchIndex].Stage == 1:
                                                i = 0
                                                foundS0 = False
                                                while i < len(gameboard.playerDeck) and foundS0 == False:
                                                        if gameboard.playerBench[benchIndex].PreEvolution.upper() == gameboard.playerDeck[i].Name.upper():
                                                                gameboard.playerBench[benchIndex].Pokemon.append(gameboard.playerDeck.pop(i))
                                                                foundS0 = True
                                                        i += 1
                                i += 1
                        if entered == True and found == True:
                                moreEnergy = True
                                while moreEnergy == True:
                                        print("What energy is attached to the benched Pokemon?")
                                        temp = input()
                                        if temp == '':
                                                moreEnergy = False
                                        else:
                                                i = 0
                                                found = False
                                                end = False
                                                while found == False and end == False:
                                                        if i >= len(gameboard.playerDeck):
                                                                print("Not found.")
                                                                end = True
                                                                i = -1
                                                        elif temp.upper() == gameboard.playerDeck[i].Name.upper():
                                                                found = True
                                                                gameboard.playerBench[benchIndex].Energies.append(gameboard.playerDeck.pop(i))
                                                        i += 1
                                #Get damage for active
                                print("How much damage is on the benched pokemon?")
                                temp = input()
                                if temp == '':
                                        temp = 0
                                gameboard.playerBench[benchIndex].Hp -= int(temp)
                                benchIndex += 1

def getOppBench(gameboard):
        morePokemon = True
        benchIndex = 0
        while morePokemon == True and benchIndex < 5:
                print("What is the opponent's benched pokemon?")
                temp = input()
                entered = True
                if temp == '':
                        morePokemon = False
                        entered = False
                else:
                        i = 0
                        found = False
                        end = False
                        while found == False and end == False:
                                if i >= len(gameboard.oppDeck):
                                        print("Not found.")
                                        end = True
                                        i = -1
                                elif temp.upper() == gameboard.oppDeck[i].Name.upper():
                                        found = True
                                        gameboard.oppBench.append(gameboard.oppDeck.pop(i))
                                        #Handle evolved pokemon
                                        if gameboard.oppBench[benchIndex].Stage == 2:
                                                i = 0
                                                foundS1 = False
                                                while i < len(gameboard.oppDeck) and foundS1 == False:
                                                        if gameboard.oppBench[benchIndex].PreEvolution.upper() == gameboard.oppDeck[i].Name.upper():
                                                                gameboard.oppBench[benchIndex].Pokemon.append(gameboard.oppDeck.pop(i))
                                                                foundS1 = True
                                                        i += 1
                                                i = 0 
                                                foundS0 = False
                                                while i < len(gameboard.oppDeck) and foundS0 == False:
                                                        if gameboard.oppBench[benchIndex].Pokemon[0].PreEvolution.upper() == gameboard.oppDeck[i].Name.upper():
                                                                gameboard.oppBench[benchIndex].Pokemon[0].Pokemon.append(gameboard.oppDeck.pop(i))
                                                                foundS0 = True
                                                        i += 1
                                        elif gameboard.oppBench[benchIndex].Stage == 1:
                                                i = 0
                                                foundS0 = False
                                                while i < len(gameboard.oppDeck) and foundS0 == False:
                                                        if gameboard.oppBench[benchIndex].PreEvolution.upper() == gameboard.oppDeck[i].Name.upper():
                                                                gameboard.oppBench[benchIndex].Pokemon.append(gameboard.oppDeck.pop(i))
                                                                foundS0 = True
                                                        i += 1
                                i += 1
                        if entered == True and found == True:
                                moreEnergy = True
                                while moreEnergy == True:
                                        print("What energy is attached to the benched Pokemon?")
                                        temp = input()
                                        if temp == '':
                                                moreEnergy = False
                                        else:
                                                i = 0
                                                found = False
                                                end = False
                                                while found == False and end == False:
                                                        if i >= len(gameboard.oppDeck):
                                                                print("Not found.")
                                                                end = True
                                                                i = -1
                                                        elif temp.upper() == gameboard.oppDeck[i].Name.upper():
                                                                found = True
                                                                gameboard.oppBench[benchIndex].Energies.append(gameboard.oppDeck.pop(i))
                                                        i += 1
                                #Get damage for active
                                print("How much damage is on the benched pokemon?")
                                temp = input()
                                if temp == '':
                                        temp = 0
                                gameboard.oppBench[benchIndex].Hp -= int(temp)
                                benchIndex += 1


# These are the dictionaries to build the Card objects from
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

newGame()
