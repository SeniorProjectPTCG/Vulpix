
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
## This file contains methods for controling game objects
## and performing actions on them
debug = False
import random
import attacks
import ai
import sys
turn = 'p'
#import gamedisplay
## This class will control the entire Gameboard
class Gameboard():
    #Player Lists
    playerDeck = []
    playerHand = []
    playerDiscard = []
    playerPrize = []
    playerBench = []
    playerActive = []

    #Opponent Lists
    oppDeck = []
    oppHand = []
    oppDiscard = []
    oppPrize = []
    oppBench = []
    oppActive = []

    #Helper Structures
    playerDeckIndex = 0
    oppDeckIndex = 0
    stadium = []
    playerMulligan = 0
    oppMulligan = 0

    #Limit Supporters to one per turn
    supporterPlayed = False
    stadiumPlayed = False
    energyPlayed = False

    #Status effect bools
    playerBurned = False
    playerParalyzed = False
    playerPoisoned = False
    playerAsleep = False
    playerConfused = False
    oppBurned = False
    oppParalyzed = False
    oppPoisoned = False
    oppAsleep = False
    oppConfused = False
    drawForTurn = False
    #Attack not available boolean used in attacks like amnesia
    playerAttackNotAvail = 0
    oppAttackNotAvail = 0

    #Agility bool
    playerAgility = False
    oppAgility = False

    #Pokemon cant retreat next turn bool
    playerCantRetreat = False
    oppCantRetreat = False

    #Last attack used var is used for copycat attack
    playerLastAttack = ""
    oppLastAttack = ""


    ## All of the player/opp member functions could possibly be combined into one function each and have a flag based on turn or access.
    ## Just a thought to reduce redundant code. Currently, I am just trying to get code down, but if we choose to do this we can edit it in Phase 3.
    ## This will also depend on how we handle turns and stuff like that. We can discuss it during our next weekly team meeting.

    

    ###  GENRAL MEMBER FUNCTIONS  ###
    def randomizeDecks(self):
        temp = []
        if debug:
            print("Size of Player's Deck: " + str(len(self.playerDeck)))
            
            

        random.shuffle(self.playerDeck)
        random.shuffle(self.oppDeck)
        if debug:
            for i in range(len(self.playerDeck)):
                print("Card " + str(i) + " of Player's deck is " + self.playerDeck[i].Name)
            print("\n")
            print("Size of Opponent's Deck: " + str(len(self.oppDeck)))
            for i in range(len(self.oppDeck)):
                print("Card " + str(i) + " of Opponent's deck is " + self.oppDeck[i].Name)

    def displayBoard(self):
        #displays the current boardstate. Should show everything known to the user on both sides. Including user's hand
        # Does nothing curently.
        print("Active: ")

    ### PLAYER MEMBER FUCNTIONS  ###

    def playerDrawCard(self):
        if len(self.playerDeck) > 0:
            self.playerHand.append(self.playerDeck.pop(self.playerDeckIndex))
        else:
            print("player decked out - opponent wins")
            sys.exit()
        #self.playerDeckIndex += 1

    def playerIsBasic(self, i):
        #Searches player's hand for a basic pokemon
        if self.playerHand[i].isBasic() == True: #This will need to be changed once the card structure is finalized. Currently each card is a dict and the hand is a list of card dicts
            return True
        else:
            return False

    def playerSetPrize(self):
        if debug:
            print("Setting up player prizes")
        self.playerPrize.append(self.playerDeck.pop(self.playerDeckIndex))
        #self.playerDeckIndex += 1

    def playerSetUp(self):
        count = 0
        basic = False
        if debug:
            print("Starting to set up Player's board...")


        ###CHECK FOR BASIC HERE!!!  ##
        for i in range(len(self.playerHand)):  #loop length of player hand - 1
            if self.playerIsBasic(i):
                basic = True #if atleast one basic is found
                count += 1
                print(str(count) + " basic(s) found!!")
            else:
                continue
                ## Need to add support for mulligan
        if count == 0:
            print("No basic found!! Player Take a Mulligan!")
            self.playerMulligan += 1
            for i in range(0, len(self.playerHand)+ 1, -1):
                self.playerDeck.append(self.playerHand.pop(i))
            random.shuffle(self.playerDeck)
            for i in range(7): # should do this 7 times...need to test to be sure
                self.playerDrawCard()
            self.playerSetUp()


        #If player has basic set up prizes#
        if basic: 
            for i in range(6):
                self.playerSetPrize()
                print(self.playerPrize[i].Name)
            # If Player only has one basic it must go to active spot
            if count == 1:
                for i in range(len(self.playerHand)):
                    if self.playerIsBasic(i):
                        self.playerActive.append(self.playerHand.pop(i)) # pops the basic from hand to active spot
                        break
            else: # more than one basic
                temp = []
                for i in range(len(self.playerHand)):
                    if self.playerIsBasic(i):
                        temp.append(self.playerHand[i])


                print("Temp list of basics:")
                random.shuffle(temp)
                self.playerActive.append(temp[0])
                for i in range(1, count):
                    self.playerBench.append(temp[i])
                for i in range(len(self.playerBench)):
                    print(self.playerBench[i].Name)

    ##          Delete from hand

                #### ISSUE HERE CAUSING INDEX OUTOF BOUND ERROR DOUBLES SOME NUMBER
                temp2 = []
                for i in range(len(temp)):
                    for j in range(len(self.playerHand)):
                        if temp[i].Name == self.playerHand[j].Name:
                            temp2.append(j)
                temp2.sort(reverse=True)   
                for i in temp2:
                    print("I : ", i)
                    print("Temp2: ", temp2)
                    print("i = ", i)
                    print(self.playerHand[i])
                    self.playerHand.pop(i)  
                    

            print("Player hand after settting up play: ")
            for i in range(len(self.playerHand)):
                print(self.playerHand[i].Name)
#               if count <= 5:
 #                  for i in range(count-1):
  #                     for i in range(len(temp)):
   #                        print(temp[i].Name)
    #                   self.playerBench.append(temp.pop(i)) #Fills bench up with all basics  NOT IDEAL!!!! TESTING PURPOSES ONLY!!!!
               ## Needs an option for user to select active or AI in our case.
              #print("Too many basics")
                
            print("Player's hand done showing") 



    ###  OPPONENT MEMBER FUNCTIONS  ###


    def oppDrawCard(self):
        if len(self.oppDeck) > 0:
            self.oppHand.append(self.oppDeck.pop(self.oppDeckIndex))
        else:
            print("opponent decked out - player wins")
            sys.exit()
        #self.oppDeckIndex += 1

    def oppIsBasic(self, i):
        #Searches player's hand for a basic pokemon
        return self.oppHand[i].isBasic()

    def oppSetPrize(self):
        if debug:
            print("Setting up opponent's prizes")
        self.oppPrize.append(self.oppDeck.pop(self.oppDeckIndex))

    def oppSetUp(self):
        count = 0
        basic = False
        if debug:
            print("Starting to set up Opponenet's board...")
            


        ###CHECK FOR BASIC HERE!!!  ##
        for i in range(len(self.oppHand)):  #loop length of player hand - 1
            if self.oppIsBasic(i):
                basic = True #if atleast one basic is found
                count += 1
                print(str(count) + " basic(s) found!!")
            else:
                continue
                ## Need to add support for mulligan
        if count == 0:
            print("No basic found!! Opp Take a Mulligan!")
            self.oppMulligan += 1
            #pop hand back into deck
            
            for i in range(0, len(self.oppHand)+ 1, -1):
                self.oppDeck.append(self.oppHand.pop(i))
            random.shuffle(self.oppDeck)
            for i in range(7): # should do this 7 times...need to test to be sure
                self.oppDrawCard()
            self.oppSetUp()
        
            


        #If player has basic set up prizes#
        if basic: 
            for i in range(6):
                self.oppSetPrize()
                print(self.oppPrize[i].Name)
            # If Player only has one basic it must go to active spot
            if count == 1:
                for i in range(len(self.oppHand)):
                    if self.oppIsBasic(i):
                        self.oppActive.append(self.oppHand.pop(i)) # pops the basic from hand to active spot
                        break
            else: # more than one basic
                temp = []
                for i in range(len(self.oppHand)):
                    if self.oppIsBasic(i):
                        temp.append(self.oppHand[i])


                print("Temp list of basics:")
                random.shuffle(temp)
                self.oppActive.append(temp[0])
                for i in range(1, count):
                    self.oppBench.append(temp[i])
                for i in range(len(self.oppBench)):
                    print(self.oppBench[i].Name)

    ##          Delete from hand

                #### ISSUE HERE CAUSING INDEX OUTOF BOUND ERROR DOUBLES SOME NUMBER
                temp2 = []
                for i in range(len(temp)):
                    for j in range(len(self.oppHand)):
                        if temp[i].Name == self.oppHand[j].Name:
                            temp2.append(j)
                temp2.sort(reverse=True)   
                for i in temp2:
                    print("I : ", i)
                    print("Temp2: ", temp2)
                    self.oppHand.pop(i)  
                    
##
##            print("Player hand after settting up play: ")
##            for i in range(len(self.playerHand)):
##                print(self.playerHand[i].Name)
###               if count <= 5:
## #                  for i in range(count-1):
##  #                     for i in range(len(temp)):
##   #                        print(temp[i].Name)
##    #                   self.playerBench.append(temp.pop(i)) #Fills bench up with all basics  NOT IDEAL!!!! TESTING PURPOSES ONLY!!!!
##               ## Needs an option for user to select active or AI in our case.
##              #print("Too many basics")
##                
            print("Opponent's hand done showing")                



    
        

    def setup(self):
        # Need to randomize deck and assign it to the deck list - DONE
        # Then draw 7 cards - DONE
        # Check for a basic - DONE
        # If Basics in hand then place a basic on bench/active and fill up the prize list - DONE
        # If no basics then set mulligan and shuffle/redraw
        
        i = 0
        basic = False
        count = 0

        if debug:
            print("Shuffling Decks...")
            
        self.randomizeDecks()
        #Draw cards from player hand
        for i in range(7): # should do this 7 times...need to test to be sure
            
            self.playerDrawCard()
            self.oppDrawCard()
        self.playerSetUp()
        self.oppSetUp()
        if self.playerMulligan - self.oppMulligan > 0:
            for i in range(self.playerMulligan - self.oppMulligan):
                self.oppDrawCard()
                print("Opponent drew a mulligan!")
        if self.oppMulligan - self.playerMulligan > 0:
            for i in range(self.oppMulligan - self.playerMulligan):
                self.playerDrawCard()
                print("Player drew a mulligan!")

    ##  THINGS THAT CAN BE DONE DURING TURNS
    def attack(self, turn):
        ## Use one of the card's attack. This ends the turn
        ## Must have proper amount and type of energy
        #global turn
        if turn == 'p':
            print(self.oppActive[0].Name + " HP: " + str(self.oppActive[0].Hp))
            print(self.playerActive[0].Name + " deals " + str(self.playerActive[0].Attack_One_Damage) + " damage")
            attacks.basicAttack(self.playerActive[0],self.oppActive[0],self.playerActive[0].Attack_One_Damage)
            print(self.oppActive[0].Hp)
            if(self.oppActive[0].Hp <= 0):
                print(self.oppActive[0].Name + " knocked out!")
                if len(self.oppBench) > 0:
                    self.oppDiscard.append(self.oppActive.pop(0))
                    self.oppActive.append(self.oppBench.pop(0))
                    print(self.oppActive[0].Name + " moved to opponents active slot")
                    self.playerHand.append(self.playerPrize[0])
                    print("player has " + str(len(self.playerPrize)) + " left")
                    if len(self.playerPrize) <= 0:
                        print("Player has taken all prizes - Player wins")
                else:
                    print("opponent out of Pokemon - Player wins")
                    sys.exit()
        elif turn == 'o':
            print(self.playerActive[0].Name + " HP: " + str(self.playerActive[0].Hp))
            print(self.oppActive[0].Name + " deals " + str(self.oppActive[0].Attack_One_Damage) + " damage")
            attacks.basicAttack(self.oppActive[0],self.playerActive[0],self.oppActive[0].Attack_One_Damage)
            print(self.playerActive[0].Hp) 
            if(self.playerActive[0].Hp <= 0):
                print(self.playerActive[0].Name + " knocked out!")
                self.playerDiscard.append(self.playerActive.pop(0))
                if len(self.playerBench) > 0:
                    self.playerActive.append(self.playerBench.pop(0))
                    print(self.playerActive[0].Name + " moved to players active slot")
                    self.oppHand.append(self.oppPrize[0])
                    print("opponent has " + str(len(self.oppPrize)) + " left")
                    if len(self.oppPrize) <= 0:
                        print("Opponent has taken all prizes - Opponent wins")
                else:
                    print("player out of Pokemon - opponent wins")
                    sys.exit()

    # def attackDamage(self, attacker, defender, choice):

    #     print(defender.Name + " HP: " + str(defender.Hp));
    #     defender.Hp = defender.Hp - attacker.Attack_One_Damage;
    #     print("Attack succesful");
    #     print(defender.Name + " HP: " + str(defender.Hp));

    def evolve(self, pokemonIndex, loc, benchIndex, turn):
        ## Evolves a pokemon on the bench with card in hand
        if turn == 'p':
            if loc == 'active':
                if self.playerActive[0].Name == self.playerHand[pokemonIndex].PreEvolution: #Pokemon evolves into pokemon in active
                    for i in range(len(self.playerActive.Energies),-1,-1):
                        self.playerHand[pokemonIndex].Energies.append(self.playerActive.Energies.pop(i))
                    if len(self.playerActive[0].Tools) > 0:
                        self.playerHand[pokemonIndex].Tools.append(self.playerActive[0].Tools.pop(0))
                    self.playerHand[pokemonIndex].Pokemon.append(self.playerActive.pop(0))
                    self.playerActive[0].append(self.playerHand[pokemonIndex])
            elif loc == 'bench':
                if self.playerBench[benchIndex].Name == self.playerHand[pokemonIndex].PreEvolution: #Pokemon evolves into pokemon in active
                    for i in range(len(self.playerBench.Energies),-1,-1):
                        self.playerHand[pokemonIndex].Energies.append(self.playerBench.Energies.pop(i))
                    if len(self.playerBench[benchIndex].Tools) > 0:
                        self.playerHand[pokemonIndex].Tools.append(self.playerBench[benchIndex].Tools.pop(0))
                    self.playerHand[pokemonIndex].Pokemon.append(self.playerBench.pop(benchIndex))
                    self.playerBench[benchIndex].append(self.playerHand[pokemonIndex])
                # do the same for bench

    
    def playEnergy(self, turn):
        ## ONCE PER TURN (Typically)
        ## Plays an energy from hand to a pokemon
        temp = []
        for i in range(len(self.playerHand)):
            if self.playerHand[i].Card_Type == 'Energy':
               temp.append(i)
        if len(temp) > 0:
            temp.sort(reverse = True)
            for i in temp:
                if self.energyPlayed == False:
                    #print(self.playerHand[i].Name)
                    self.playerActive[0].Energies.append(self.playerHand.pop(i))
                    self.energyPlayed = True
                    print("Energy played")
        
    def playItem(self, turn):
        ## Plays an item from hand and does the effect
        pass
    def playSupporter(self, turn):
        ## ONCE PER TURN (typically)
        ## Plays a supporter from hand
        pass
    def playTool(self, turn):
        ## Plays a tool from hand and places it on the pokemon card in play
        pass
    def playStadium(self, turn):
        ## ONCE PER TURN
        ## Plays a stadium from hand
        ## Can't play if stadium in play shares same name

        ## **CURENTLY I AM ASSUMING ONLY ONE STADIUM IS FOUND
        ## **NEEDS EDITED FOR MULTIPLE AND OPPONENT'S TURN
        temp = []
        #count = 0
        index = 0
        if turn == 'p':
            for i in range(len(self.playerHand)):
                if self.playerHand[i].Card_Type == 'Stadium':
                    temp.append(self.playerHand[i])
                    #count += 1 # Counts total number of stadium type cards
                    index = i # appends the index where the stadium is located in hand for removal later
            if len(temp) == 1: #If there is a stadium in hand
                if len(self.stadium) == 1: # If there is a stdium in play
                    if self.stadium[0].Name == temp[0].Name:  # If the stadium is already in play
                        pass  # Card can't be played so I just pass
                    else:  # Stadium with same name not in play
                        if self.stadium[0].Owner == 'p':
                            self.playerDiscard.append(self.stadium.pop(0)) # Discard current stadium if it is owned by player
                            self.stadium.append(self.playerHand.pop(index)) # moves card from hand to stadium spot
                        if self.stadium[0].Owner == '0':
                            self.oppDiscard.append(self.stadium.pop(0)) # Discard current stadium if it is owned by opponent
                            self.stadium.append(self.playerHand.pop(index)) # moves card from hand to stadium spot
                        
        pass
    def retreat(self, pokemonIndex, turn):
        ## ONCE PER TURN (typically)
        ## Switches active with a bench pokemon
        if turn == 'p':
            print("active before: " + self.playerBench[0].Name)
            if self.playerActive[0].RetreatCost <= len(self.playerActive[0].Energies):
                self.switch(pokemonIndex, turn)
            else:
                print("thats not a pokemon")

    def switch(self, pokemonIndex, turn):
        if len(self.playerBench) > 0:
            temp = self.playerActive.pop(0)
            self.playerActive.append(self.playerBench.pop(pokemonIndex))
            self.playerBench.append(temp)
            print("active after: " + self.playerActive[0].Name)
            
    def useAbility(self, turn):
        ## USAGE AMOUNT VARIES
        ## Uses an ability and processes effects
        pass
    
    def playBasic(self, handIndex, turn):
        ## Plays a basic from hand to bench, space permitting)
        if turn == 'p':

            if len(self.playerBench) < 5:
                self.playerBench.append(self.playerHand.pop(handIndex))
        elif turn == 'o':
            if len(self.oppBench) < 5:

                self.oppBench.append(self.oppHand.pop(handIndex))
    
    def printHand(self, turn):
        if turn == 'p':
            print("Your hand contains:")
            for i in range(len(self.playerHand)):
                print(self.playerHand[i].Name)
        if turn == 'o':
            print("Opponents hand contains:")
            for i in range(len(self.oppHand)):
                print(self.oppHand[i].Name)

    def turn(self, turn):
        # Check for wins
        # Check for statuses(Mainly ones that happen between turns)
        # Player's Turn
        #self.winConditions()
        self.printHand(turn)
        print("Menu")
        print("1. Play Basic")
        print("2. Play Stadium")
        print("3. Play Energy")
        print("4. Play Tool")
        print("5. Play Supporter")
        print("6. Play Attack")
        print("7. End Turn")
        #choice = int(input("What would you like to do?"))
        if turn == 'p':
            choice = ai.playerAI(self)
            print("Player AI chose ", choice)
            ## SHOULD CHECK FOR THINGS BEFORE CALLING FUNCTIONS OR THAT SHOULD BE WHAT WE DO I THINK
            if not self.drawForTurn:
                self.playerDrawCard()
                self.drawForTurn = True
            if choice == 1: #Play Basic

                i = 0
                while i < len(self.playerHand):
                    
               
                    if self.playerHand[i].isBasic():
                        
                        self.playBasic(i, turn)
                        print("basic found")
                        
                    else:
                        print("no valid basics")
                        i += 1

                self.turn(turn)
            elif choice == 2:
                self.playStadium(turn)
                self.turn(turn)
            elif choice == 3:

                self.playEnergy(turn)
                self.energyPlayed = True
                self.turn(turn)
            elif choice == 4:
                self.playTool(turn)
                self.turn(turn)
            elif choice == 5:
                self.supporterPlayed = True
                playSupporter(turn)
                self.turn(turn)
            elif choice == 6:
                self.attack(turn)
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turn("o")
                pass
            elif choice == 7:
                print("EXIT")
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turn("o")

        # Opponent's Turn
        elif turn == 'o':
            choice = ai.oppAI(self)
            print("Opponent AI chose ", choice)
            if not self.drawForTurn:
                self.oppDrawCard()
                self.drawForTurn = True
            if choice == 1: #Play Basic

                i = 0
                while i < len(self.oppHand):
                    if self.oppHand[i].isBasic():
                        

                        self.playBasic(i, turn)
                        print("basic found")
                    else:
                        print("no valid basics")

                        
                        i += 1

                self.turn(turn)
            elif choice == 2:
                self.playStadium(turn)
                self.turn(turn)
            elif choice == 3:

                self.playEnergy(turn)
                self.energyPlayed = True
                self.turn(turn)
            elif choice == 4:
                self.playTool(turn)
                self.turn(turn)
            elif choice == 5:
                self.supporterPlayed = True
                playSupporter(turn)
                self.turn(turn)
            elif choice == 6:
                self.attack(turn)
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turn("p")
                pass
            elif choice == 7:
                print("EXIT")
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turn("p")



    def winConditions(self):

        ## Opponent Win Conditions ##
        if len(playerActive) <= 0 and len(playerBench) <= 0:
            print("Opponent wins!")
            sys.exit()
        if len(oppPrize) <= 0:
            print("Opponent wins!")
            sys.exit()
        if len(playerDeck) <= 0:
            print("Opponent wins!")
            sys.exit()

        ## Player Win Conditions ##
        if len(oppActive) <= 0 and len(oppBench) <= 0:  # Empty bench and active
            print("Player wins!")
            sys.exit()
        if len(playerPrize) <= 0:  # No prizes left
            print("Player wins!")
            sys.exit()





class Card():
    Name = ''
    Card_Type = ''
    #Basic = False
    Hp = 0
    Attack_One_Damage = 0
    Attack_One_Effect = ''
    Attack_One_Cost = ''
    Attack_Two_Damage = 0
    Attack_Two_Effect = ''
    Attack_Two_Cost = ''
    
    RetreatCost = 0
    Pokemon_Type = ''

    Weakness = ''
    Resistance = ''
    PreEvolution = ''
    Pokemon = []
    Stage = 0
    Effect = ''
    Owner = ''
    Energies = []
    Tools = []

    def __init__(self, obj):
        self.Name = obj['Name']
        self.Card_Type = obj['Card_Type']
        if self.Card_Type == 'Pokemon':
            self.Stage = obj['Stage']
            self.Hp = obj['Hp']
            self.Power = obj['Power']
            self.Attack_One_Damage = obj['Attack1Damage']
            self.Attack_One_Effect = obj['Attack1Effect']
            self.Attack_One_Cost = obj['Attack1Cost']
            #self.Attack_Two_Damage = obj['Attack2Damage']
            self.Attack_Two_Effect = obj['Attack2Effect']
            self.Attack_Two_Cost = obj['Attack2Cost']
            self.Retreat_Cost = obj['RetreatCost']
            self.Weakness = obj['Weakness']
            self.Resistance = obj['Resistance']
        if self.Card_Type == 'Item' or self.Card_Type == 'Supporter' or self.Card_Type == 'Stadium' or self.Card_Type == 'Tool':
            self.Effect = obj['Effect']
    def isBasic(self):
        if self.Card_Type == 'Pokemon':
            return self.Stage == 0
        else:
            return False
    def setOwner(self, owner):
        self.Owner = owner

