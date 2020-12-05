######################################################
##                 Project Vulpix                   ##
##                Senior Project 2                  ##
##                 Andrew Siddall                   ##
##                 Chris Crisson                    ##
##               January 31, 2019                   ##
######################################################

###################DESCRIPTION########################
## This file will run a main game loop for the AI to automatically play 

import GameManager_clean as GameManager
import mcts
import sys

debug = False
maxIteration = 20

def newGame():
        
        #input("Press enter to start a new game")
        ## Initialize the gameboard
        gameboard = GameManager.Gameboard()
        ## Initialize the decks
        for i in range(3): # adds 3 Buizel to both decks
                obj = GameManager.Card(card1)
                if debug:
                        print("Buizel added to player's deck")
                gameboard.playerDeck.append(obj)
                if debug:
                        print("Buizel added to opponent's deck")
                gameboard.oppDeck.append(obj)
                
                obj = GameManager.Card(card4) #add 3 Totodile to both deck
                if debug:
                        print("Totodile added to player's deck")
                gameboard.playerDeck.append(obj)
                if debug:
                        print("Totodile added to opponent's deck")
                gameboard.oppDeck.append(obj)

        for i in range(4):
                obj = GameManager.Card(card2) #adds 4 froakie
                gameboard.playerDeck.append(obj)
                gameboard.oppDeck.append(obj)
                

                obj = GameManager.Card(card3)  #adds 4 remoraid
                gameboard.playerDeck.append(obj)
                gameboard.oppDeck.append(obj)
                

                obj = GameManager.Card(card5) #adds 4 wingull
                gameboard.playerDeck.append(obj)
                gameboard.oppDeck.append(obj)        
        
        for i in range(42): #add 42 energy
                obj = GameManager.Card(card24)
                gameboard.playerDeck.append(obj)
                gameboard.oppDeck.append(obj)

        # Set the gameboard to the default state
        #gameboard.setup()
        with open('gamelog.txt', 'w') as file:
                file.write("\n")
        print("Setting up player...")
        gameboard.playerSetUp()
        print("Setting up opponent...")
        gameboard.oppSetUp()
        GameLoop(gameboard)

def GameLoop(gameboard, count=0):
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
        
        #0 - Player
        #1 - Opponent
        print("___________________Start of Next ACTION______________________________")
        counter = count
        if gameboard.turn == 'p':
                turn = 'player'
        elif gameboard.turn == 'o':
                turn = 'opponent'
                counter -= 1
        
        
        

        #Control game
        go = True
        
        while go == True:
                

                ## Check for win condition
                gameOver = gameboard.checkWinCon(gameboard.turn)
                displayBoard(gameboard)
                counter += 1
                with open('gamelog.txt', 'a') as file:
                        file.write("Turn: " + str(count) + " of " + turn + "\n")
                        
                        if gameOver != 1 and gameOver != 0:
                                selectedMove = str(mcts.uct(gameboard,maxIteration))
                                move = parseMove(selectedMove)
                                print("The suggested move for " + turn + " is " + move)
                                if move == 'play energy':
                                        if turn == 'player':
                                                for i in range(len(gameboard.playerHand)):
                                                        if gameboard.playerHand[i].Card_Type == "Energy":
                                                            gameboard.energyPlayed = False
                                                            gameboard.playEnergy('p',i)
                                                            gameboard.energyPlayed = True
                                                            print("Player actually played energy!")
                                                            file.write("Player actually played energy!\n")
                                                            file.write("___________________END OF ACTION______________________________\n")
                                                            break
                                        if turn == 'opponent':
                                                for i in range(len(gameboard.oppHand)):
                                                        if gameboard.oppHand[i].Card_Type == "Energy":
                                                            gameboard.energyPlayed = False
                                                            gameboard.playEnergy('o',i)
                                                            gameboard.energyPlayed = True
                                                            print("Opponent actually played energy!")
                                                            file.write("Opponent actually played energy!\n")
                                                            file.write("___________________END OF ACTION______________________________\n")
                                                            break
                                                
                                elif move == 'attack' and turn == 'player' :
                                        if gameboard.checkEnergyCost(gameboard.playerActive[0].Attack_One_Cost, gameboard.playerActive[0].Energies):
                                                #print(gameboard.oppActive[0].Name + "'s HP went down to " + str((gameboard.oppActive[0].Hp - gameboard.playerActive[0].Attack_One_Damage)) + " from " + str(gameboard.oppActive[0].HP))
                                                gameboard.attack(gameboard.turn, gameboard.playerActive[0].Attack_One_Name, gameboard.playerActive[0].Attack_One_Damage, gameboard.playerActive[0].Attack_One_Cost)
                                                gameOver = gameboard.checkWinCon(gameboard.turn)
                                                if gameOver == 1:
                                                        print("Player has won")
                                                        file.write("Player has won!\n")
                                                        del gameboard
                                                        break
                                                elif gameOver == 0:
                                                        print("Opponent has won")
                                                        file.write("Opponent has won!\n")
                                                        del gameboard
                                                        break
                                                print(turn + " attacked " + gameboard.oppActive[0].Name + " for " + str(gameboard.playerActive[0].Attack_One_Damage))
                                                #gameboard.turn = 'o'
                                                #gameboard.oppDrawCard()
                                                file.write("Player attacked!\n")
                                                file.write("------------------------------END OF TURN-----------------------------\n-")
                                elif move == 'attack' and turn == 'opponent' :
                                        if gameboard.checkEnergyCost(gameboard.oppActive[0].Attack_One_Cost, gameboard.oppActive[0].Energies):
                                                #print(gameboard.playerActive[0].Name + "'s HP went down to " + str((gameboard.playerActive[0].Hp - gameboard.oppActive[0].Attack_One_Damage)) + " from " + str(gameboard.playerActive[0].HP))
                                                gameboard.attack(gameboard.turn, gameboard.oppActive[0].Attack_One_Name, gameboard.oppActive[0].Attack_One_Damage, gameboard.oppActive[0].Attack_One_Cost)
                                                gameOver = gameboard.checkWinCon(gameboard.turn)
                                                if gameOver == 1:
                                                        print("Player has won")
                                                        file.write("Player has won!\n")
                                                        go = False
                                                        del gameboard
                                                        break
                                                elif gameOver == 0:
                                                        print("Opponent has won")
                                                        file.write("Opponent has won!\n")
                                                        go = False
                                                        break
                                                        del gameboard
                                                print(turn + " attacked " + gameboard.playerActive[0].Name + " for " + str(gameboard.oppActive[0].Attack_One_Damage))
                                                #gameboard.turn = 'p'
                                                #gameboard.playerDrawCard()
                                                file.write("Opponent attacked!\n")
                                                file.write("------------------------------END OF TURN-----------------------------\n-")

                                elif (move == 'pass turn' or move == 'retreat') and turn == 'player':
                                        gameboard.passTurn(gameboard.turn)
                                        print(turn + " " + move)
                                        gameboard.turn = 'o'
                                        gameboard.oppDrawCard()
                                        file.write(turn + " " + move + "\n")
                                        file.write("------------------------------END OF TURN-----------------------------\n-")
                                elif (move == 'pass turn' or move == 'retreat') and turn == 'opponent':
                                        gameboard.passTurn(gameboard.turn)
                                        print(turn + " " + move)
                                        gameboard.turn = 'p'
                                        gameboard.playerDrawCard()
                                        file.write(turn + " " + move + "\n")
                                        file.write("------------------------------END OF TURN-----------------------------\n-")

                                elif move == 'play basic' and turn == 'player':
                                        if len(gameboard.playerBench) < 5:
                                            #print("Attempted to play bench pokemon")
                                            for i in range(len(gameboard.playerHand)):
                                                if gameboard.playerHand[i].Card_Type == "Pokemon":
                                                    if gameboard.playerHand[i].Stage == 0 and len(gameboard.playerBench) < 5:
                                                        print("Player played " + gameboard.playerHand[i].Name + " to the bench")
                                                        file.write("Player played " + gameboard.playerHand[i].Name + " to the bench\n")
                                                        gameboard.playBasic(i, gameboard.turn)
                                                        file.write("___________________END OF ACTION______________________________\n")
                                                        break

                                elif move == 'play basic' and turn == 'opponent':
                                        if len(gameboard.oppBench) < 5:
                                            #print("Attempted to play bench pokemon")
                                            for i in range(len(gameboard.oppHand)):
                                                if gameboard.oppHand[i].Card_Type == "Pokemon":
                                                    if gameboard.oppHand[i].Stage == 0 and len(gameboard.oppBench) < 5:
                                                        print("Opponent played " + gameboard.oppHand[i].Name + " to the bench")
                                                        file.write("Oppenent played " + gameboard.oppHand[i].Name + " to the bench\n")
                                                        gameboard.playBasic(i, gameboard.turn)
                                                        file.write("___________________END OF ACTION______________________________\n")
                                                        break
                        
                        elif gameOver == 1:
                                print("Player has won")
                                file.write("Player has won!\n")
                                go = False
                                del gameboard
                                break
                        elif gameOver == 0:
                                print("Opponent has won")
                                file.write("Opponent has won!\n")
                                go = False
                                del gameboard
                                break

                
                #input("Press enter to continue.")
                #gameboard.energyPlayed = False
                
                
                saveBoard(gameboard)
                
                #displayBoard(gameboard)
                GameLoop(gameboard, counter)

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



def displayBoard(gameboard):
        print("---Player's Board---")
        print("Active: " + gameboard.playerActive[0].Name + " HP: " + str(gameboard.playerActive[0].Hp))
        print(str(len(gameboard.playerActive[0].Energies)) + " Energies Attached: ")
##        for i in range(len(gameboard.playerActive[0].Energies)):
##            print(gameboard.playerActive[0].Energies[i].Name)
        print("\n")
        print("---Bench Pokemon---")
        for i in range(len(gameboard.playerBench)):
            print("Name: " + gameboard.playerBench[i].Name + " HP: " + str(gameboard.playerBench[i].Hp))
            print(str(len(gameboard.playerBench[i].Energies)) + " Energies Attached: ")
##            for j in range(len(gameboard.playerBench[i].Energies)):
##                print(gameboard.playerBench[i].Energies[j].Name)
        print("\n")
        print("Prize Count is : " + str(len(gameboard.playerPrize)))
        print("Deck Size is: " + str(len(gameboard.playerDeck)))
        print("\n")
        print("--Player Hand--")
        for i in range(len(gameboard.playerHand)):
                print(gameboard.playerHand[i].Name)
        print("\n")

        print("---Opponent's Board---")
        print("Active: " + gameboard.oppActive[0].Name + " HP: " + str(gameboard.oppActive[0].Hp))
        print(str(len(gameboard.oppActive[0].Energies)) + " Energies Attached: ")
##        for i in range(len(gameboard.oppActive[0].Energies)):
##            print(gameboard.oppActive[0].Energies[i].Name)
        print("\n")
        print("---Bench Pokemon---")
        for i in range(len(gameboard.oppBench)):
            print("Name: " + gameboard.oppBench[i].Name + " HP: " + str(gameboard.oppBench[i].Hp))
            print(str(len(gameboard.oppBench[i].Energies)) + " Energies Attached: ")
##            for j in range(len(gameboard.oppBench[i].Energies)):
##                print(gameboard.oppBench[i].Energies[j].Name)
        print("\n")
        print("Prize Count is : " + str(len(gameboard.oppPrize)))
        print("Deck Size is: " + str(len(gameboard.oppDeck)))
        print("\n")
        print("--Opponent's Hand--")
        for i in range(len(gameboard.oppHand)):
                print(gameboard.oppHand[i].Name)
        print("\n")
        
def saveBoard(gameboard):
        with open('gamelog.txt', 'a') as file:
                file.write("---Player's Board---\n")
        
                file.write("Active: " + gameboard.playerActive[0].Name + " HP: " + str(gameboard.playerActive[0].Hp))
                file.write("\n")
                file.write(str(len(gameboard.playerActive[0].Energies)) + " Energies Attached: ")
                file.write("\n")
##                for i in range(len(gameboard.playerActive[0].Energies)):
##                    file.write(gameboard.playerActive[0].Energies[i].Name)
##                    file.write("\n")
                file.write("\n")
                file.write("---Bench Pokemon---\n")
                for i in range(len(gameboard.playerBench)):
                    file.write("Name: " + gameboard.playerBench[i].Name + " HP: " + str(gameboard.playerBench[i].Hp))
                    file.write("\n")
                    file.write(str(len(gameboard.playerBench[i].Energies)) + " Energies Attached: ")
                    file.write("\n")
##                    for j in range(len(gameboard.playerBench[i].Energies)):
##                        file.write(gameboard.playerBench[i].Energies[j].Name)
##                        file.write("\n")
                file.write ("\n")
                file.write("Prize Count is : " + str(len(gameboard.playerPrize)))
                file.write("\n")
                file.write("Deck Size is: " + str(len(gameboard.playerDeck)))
                file.write("\n")
                file.write("--Player Hand--\n")
                for i in range(len(gameboard.playerHand)):
                        file.write(gameboard.playerHand[i].Name)
                        file.write("\n")
                file.write("\n")

                file.write("---Opponent's Board---\n")
                file.write("Active: " + gameboard.oppActive[0].Name + " HP: " + str(gameboard.oppActive[0].Hp))
                file.write("\n")
                file.write(str(len(gameboard.oppActive[0].Energies)) + " Energies Attached: ")
                file.write("\n")
##                for i in range(len(gameboard.oppActive[0].Energies)):
##                    file.write(gameboard.oppActive[0].Energies[i].Name)
##                    file.write("\n")
                file.write("\n")
                file.write("---Bench Pokemon---")
                file.write("\n")
                for i in range(len(gameboard.oppBench)):
                    file.write("Name: " + gameboard.oppBench[i].Name + " HP: " + str(gameboard.oppBench[i].Hp))
                    file.write("\n")
                    file.write(str(len(gameboard.oppBench[i].Energies)) + " Energies Attached: ")
                    file.write("\n")
##                    for j in range(len(gameboard.oppBench[i].Energies)):
##                        file.write(gameboard.oppBench[i].Energies[j].Name)
##                        file.write("\n")
                file.write("\n")
                file.write("Prize Count is : " + str(len(gameboard.oppPrize)))
                file.write("\n")
                file.write("Deck Size is: " + str(len(gameboard.oppDeck)))
                file.write("\n")
                file.write("--Opponent's Hand--")
                file.write("\n")
                for i in range(len(gameboard.oppHand)):
                        file.write(gameboard.oppHand[i].Name)
                        file.write("\n")
                file.write("\n")


# These are the dictionaries to build the Card objects from
card1 = {'Name' : 'Buizel',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : 'Razor Fin',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 40,
        'Attack2Name' : 'Water Gun',
        'Attack2Cost' : 'MCC',
        'RetreatCost' : 1,
        'Weakness' : 'R',
        'Resistance' : '',
        'Pokemon_Type' : 'M',
        'Energies' : []}



card2 = {'Name' : 'Froakie',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : 'Pound',
        'Attack1Cost' : 'M',
        'Attack2Damage' : 20,
        'Attack2Name' : 'Water Drip',
        'Attack2Cost' : 'MC',
        'RetreatCost' : 1,
        'Weakness' : 'P',
        'Resistance' : '',
        'Pokemon_Type' : 'P',
        'Energies' : []}

card3 = {'Name' : 'Remoraid',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 30,
        'Attack1Name' : 'Water Gun',
        'Attack1Cost' : 'MC',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'P',
        'Resistance' : '',
        'Pokemon_Type' : 'P',
        'Energies' : []}

card4 = {'Name' : 'Totodile',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 70,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : 'Water Gun',
        'Attack1Cost' : 'C',
        'Attack2Damage' : 20,
        'Attack2Name' : 'Bite',
        'Attack2Cost' : 'MC',
        'RetreatCost' : 1,
        'Weakness' : 'P',
        'Resistance' : '',
        'Pokemon_Type' : 'P',
        'Energies' : []}

card5 = {'Name' : 'Wingull',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : 'Water Gun',
        'Attack1Cost' : 'M',
        'Attack2Damage' : 0,
        'Attack2Name' : 'None',
        'Attack2Cost' : 'None',
        'RetreatCost' : 1,
        'Weakness' : 'P',
        'Resistance' : '',
        'Pokemon_Type' : 'P',
        'Energies' : []}


card24 = {'Name' : 'Metal Energy',
        'Card_Type' : 'Energy',
        'Effect' : ''}

## MAIN ##

newGame()
