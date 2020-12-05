##  This file is used to manually test features of the engine.
##  This allows me to see where the errors are in the game logic and not the AI
##  Most of the basic features of the game engine are present in the menu


import GameManager_clean as GameManager
import Deck
import attacks
import sys

## Helper fucntions

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


def startGame():
    gameboard = GameManager.Gameboard()
    #set up decks
    Deck.newDeck(gameboard)
    print("Setting up player...")
    gameboard.playerSetUp()
    print("Setting up opponent...")
    gameboard.oppSetUp()
    if gameboard.turn == 'p':
        gameboard.playerDrawCard()
    elif gameboard.turn == 'o':
        gameboard.oppDrawCard()
    gameLoop(gameboard)


def gameLoop(gameboard):
    go = True
    
    while go:
        if gameboard.turn == 'p':
                turn = 'player'
        elif gameboard.turn == 'o':
                turn = 'opponent'
        
        # Check for winner
        gameOver = gameboard.checkWinCon(gameboard.turn)
        print(gameOver)
        ## Print out menu
        print("Currently is " + turn + "'s turn!")
        print("----Menu----")
        print("1. Play Energy")
        print("2. Play Basic")
        print("3. Attack")
        print("4. Pass")
        print("5. Show Board")
        ## Get menu choice
        choice = input("Choose an action: ")

        

        if choice == '1':   # Choice is play energy
            if turn == 'player':
                for i in range(len(gameboard.playerHand)):
                    if gameboard.playerHand[i].Card_Type == "Energy":
                        #gameboard.energyPlayed = False
                        gameboard.playEnergy('p',i)
                        gameboard.energyPlayed = True
                        print("Player actually played energy!")
                        break
                    else:
                        print("No energy to play!")

            elif turn == 'opponent':
                for i in range(len(gameboard.oppHand)):
                    if gameboard.oppHand[i].Card_Type == "Energy":
                        #gameboard.energyPlayed = False
                        gameboard.playEnergy('o',i)
                        gameboard.energyPlayed = True
                        print("Opponent actually played energy!")
                        break
                    else:
                        print("No energy to play!")

        elif choice == '2':  # Choice is play basic
            pass
        
        elif choice == '3':  # Choice is attack
            if turn == 'player':
                print("Player is attempting to attack")
                if gameboard.checkEnergyCost(gameboard.playerActive[0].Attack_One_Cost, gameboard.playerActive[0].Energies):
                    #print(gameboard.oppActive[0].Name + "'s HP went down to " + str(gameboard.oppActive[0].Hp - gameboard.playerActive[0].Attack_One_Damage) + " from " + str(gameboard.oppActive[0].Hp))
                    gameboard.attack(gameboard.turn, gameboard.playerActive[0].Attack_One_Name, gameboard.playerActive[0].Attack_One_Damage, gameboard.playerActive[0].Attack_One_Cost)
                    gameOver = gameboard.checkWinCon(gameboard.turn)
                    if gameOver == 1:
                        print("Player has won")
                        go = False
                        break
                        del gameboard
            
                    elif gameOver == 0:
                        print("Opponent has won")
                        go = False
                        break
                        del gameboard
                    print(turn + " attacked " + gameboard.oppActive[0].Name + " for " + str(gameboard.playerActive[0].Attack_One_Damage))
                else:
                    print("Not enough energy to attack")
                    
            elif turn == 'opponent':
                if gameboard.checkEnergyCost(gameboard.oppActive[0].Attack_One_Cost, gameboard.oppActive[0].Energies):
                    #print(gameboard.playerActive[0].Name + "'s HP went down to " + str(gameboard.playerActive[0].Hp - gameboard.oppActive[0].Attack_One_Damage) + " from " + str(gameboard.playerActive[0].Hp))
                    gameboard.attack(gameboard.turn, gameboard.oppActive[0].Attack_One_Name, gameboard.oppActive[0].Attack_One_Damage, gameboard.oppActive[0].Attack_One_Cost)
                    gameOver = gameboard.checkWinCon(gameboard.turn)
                    if gameOver == 1:
                        print("Player has won")
                        go = False
                        break
                        #del gameboard
            
                    elif gameOver == 0:
                        print("Opponent has won")
                        go = False
                        break
                        #del gameboard
                    print(turn + " attacked " + gameboard.playerActive[0].Name + " for " + str(gameboard.oppActive[0].Attack_One_Damage))
                    #gameboard.turn = 'p'
            #gameboard.passTurn(gameboard.turn)
        
        elif choice == '4':  # Choice is to pass turn
            if turn == 'player':
                gameboard.passTurn(gameboard.turn)
                #print(turn + " " + move)
                gameboard.energyPlayed = False
                gameboard.turn = 'o'
                #gameboard.oppDrawCard()

            elif turn == 'opponent':
                gameboard.passTurn(gameboard.turn)
                gameboard.energyPlayed = False
                #print(turn + " " + move)
                gameboard.turn = 'p'
                #gameboard.playerDrawCard()

        elif choice == '5':  # Choice is to show board
            displayBoard(gameboard)

        if gameOver == 1:
            print("Player has won")
            go = False
            del gameboard
            break
            
        elif gameOver == 0:
            print("Opponent has won")
            go = False
            del gameboard
            break
            

        
startGame()
