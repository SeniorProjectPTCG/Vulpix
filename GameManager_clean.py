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
import items
import sys
import mcts

#import gamedisplay
## This class will control the entire Gameboard
class Gameboard():
    def __init__(self):
        self.turn = 'p'
        #Player Lists
        self.playerDeck = []
        self.playerHand = []
        self.playerDiscard = []
        self.playerPrize = []
        self.playerBench = []
        self.playerActive = []

        #Opponent Lists
        self.oppDeck = []
        self.oppHand = []
        self.oppDiscard = []
        self.oppPrize = []
        self.oppBench = []
        self.oppActive = []

        #Helper Structures
        self.playerDeckIndex = 0
        self.oppDeckIndex = 0
        self.stadium = []
        self.playerMulligan = 0
        self.oppMulligan = 0

        #Limit Supporters to one per turn
        self.supporterPlayed = False
        self.stadiumPlayed = False
        self.energyPlayed = False

        #Status effect bools
        self.playerBurned = False
        self.playerParalyzed = False
        self.playerPoisoned = False
        self.playerAsleep = False
        self.playerConfused = False
        self.oppBurned = False
        self.oppParalyzed = False
        self.oppPoisoned = False
        self.oppAsleep = False
        self.oppConfused = False
        self.drawForTurn = False
        #Attack not available boolean used in attacks like amnesia
        self.playerAttackNotAvail = 0
        self.oppAttackNotAvail = 0

        #Agility bool
        self.playerAgility = False
        self.oppAgility = False

        #Pokemon cant retreat next turn bool
        self.playerCantRetreat = False
        self.oppCantRetreat = False

        #Last attack used var is used for copycat attack
        self.playerLastAttack = ""
        self.oppLastAttack = ""

        #Can only retreat once per turn
        self.retreated = False

    ## All of the player/opp member functions could possibly be combined into one function each and have a flag based on turn or access.
    ## Just a thought to reduce redundant code. Currently, I am just trying to get code down, but if we choose to do this we can edit it in Phase 3.
    ## This will also depend on how we handle turns and stuff like that. We can discuss it during our next weekly team meeting.

    def Clone(self):
        st = self
        return st

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



    ### PLAYER MEMBER FUCNTIONS  ###

    def playerDrawCard(self):
        if len(self.playerDeck) > 0:
            self.playerHand.append(self.playerDeck.pop(self.playerDeckIndex))
            #print("Player drew a Card!")
            
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
                if debug:
                    print(str(count) + " basic(s) found!!")
            else:
                continue
                ## Need to add support for mulligan
        if count == 0:
            if debug:
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
                if debug:
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

                if debug:
                    print("Temp list of basics:")
                random.shuffle(temp)
                self.playerActive.append(temp[0])
                for i in range(1, count):
                    self.playerBench.append(temp[i])
                for i in range(len(self.playerBench)):
                    if debug:
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
                    if debug:
                        print("I : ", i)
                        print("Temp2: ", temp2)
                        print("i = ", i)
                        print(self.playerHand[i])
                    self.playerHand.pop(i)  
                    

            print("Player hand after settting up play: ")
            for i in range(len(self.playerHand)):
                print(self.playerHand[i].Name)
                
            print("Player's hand done showing") 



    ###  OPPONENT MEMBER FUNCTIONS  ###


    def oppDrawCard(self):
        if len(self.oppDeck) > 0:
            self.oppHand.append(self.oppDeck.pop(self.oppDeckIndex))
            #print("Opponent drew a Card!")
        
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
                if debug:
                    print(str(count) + " basic(s) found!!")
            else:
                continue
                ## Need to add support for mulligan
        if count == 0:
            if debug:
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
                if debug:
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

                if debug:
                    print("Temp list of basics:")
                random.shuffle(temp)
                self.oppActive.append(temp[0])
                for i in range(1, count):
                    self.oppBench.append(temp[i])
                for i in range(len(self.oppBench)):
                    if debug:
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
                    if debug:
                        print("I : ", i)
                        print("Temp2: ", temp2)
                    self.oppHand.pop(i)  
                                   
            print("Opponent's hand done showing")                


    def checkEnergyCost(self, cost, attached):
        #print("Checking energy costs...")
        test = attached.copy()
        count = 0
        for i in cost:
            if i == "M":
                if "Metal Energy" in test:
                    test.remove("Metal Energy")
                    count += 1
            elif i == "P":
                if "Psychic Energy" in test:
                    test.remove("Psychic Energy")
                    count += 1
            else:
                if len(test) != 0:
                    test.pop(0)
                    count += 1
        
        if count == len(cost):
            #print("Has enough energy to attack")
            return True
        else:
            #print("Does not have enough energy to attack")
            
            return False

    ##  THINGS THAT CAN BE DONE DURING TURNS
    def attack(self, turn, attackName, damage, cost):
        ## Use one of the card's attack. This ends the turn
        ## Must have proper amount and type of energy
        #global turn
        if turn == 'p':
            if self.checkEnergyCost(cost, self.playerActive[0].Energies) == True:
                attacks.basicAttack(self.playerActive[0],self.oppActive[0],self.playerActive[0].Attack_One_Damage)
                print(self.playerActive[0].Name + " did " + str(self.playerActive[0].Attack_One_Damage) + " to " + self.oppActive[0].Name)
                
                if(self.oppActive[0].Hp <= 0):
                    print(self.oppActive[0].Name + " knocked out!")
                    for i in reversed(range(len(self.oppActive[0].Energies))):
                        self.oppDiscard.append(self.oppActive[0].Energies.pop(i))
                    if len(self.oppBench) > 0:
                        self.oppDiscard.append(self.oppActive.pop(0))
                        self.oppActive.append(self.oppBench.pop(0))
                        print(self.oppActive[0].Name + " moved to opponents active slot")
                        self.playerHand.append(self.playerPrize.pop(0))
                        print("player has " + str(len(self.playerPrize)) + " left")
        elif turn == 'o':
            if self.checkEnergyCost(cost, self.oppActive[0].Energies):
                attacks.basicAttack(self.oppActive[0],self.playerActive[0],self.oppActive[0].Attack_One_Damage)
                print(self.oppActive[0].Name + " did " + str(self.oppActive[0].Attack_One_Damage) + " to " + self.playerActive[0].Name)
                
                if(self.playerActive[0].Hp <= 0):
                    print(self.playerActive[0].Name + " knocked out!")
                    for i in reversed(range(len(self.playerActive[0].Energies))):
                        self.playerDiscard.append(self.playerActive[0].Energies.pop(i))
                    self.playerDiscard.append(self.playerActive.pop(0))
                    if len(self.playerBench) > 0:
                        self.playerActive.append(self.playerBench.pop(0))
                        print(self.playerActive[0].Name + " moved to players active slot")
                        self.oppHand.append(self.oppPrize.pop(0))
                        print("opponent has " + str(len(self.oppPrize)) + " left")
                        
        self.passTurn(turn)



    def passTurn(self, t):
        print(t)
        if t == 'p':
            self.checkWinCon(t)
            self.turn = 'o'
            self.oppDrawCard()
            print("Opp drew card for turn!")
        elif t == 'o':
            self.checkWinCon(t)
            self.turn = 'p'
            self.playerDrawCard()
            print("Player drew card for turn!")
        #reset turn flags
        supporterPlayed = False
        stadiumPlayed = False
        energyPlayed = False
        playerAttackNotAvail = 0
        oppAttackNotAvail = 0
        playerAgility = False
        oppAgility = False
        playerCantRetreat = False
        oppCantRetreat = False
        retreated = False

    def getMoves(self, turn):
        legalMoves = []
        #print("checkWinCon = " + str(self.checkWinCon(turn)))
        #print("turn: " + turn)
        # If someone has won return an empty list to indicate terminal state
        # Flag to add pass turn only if nothing else is available
        passFlag = True
        if self.checkWinCon(turn) != 1 and self.checkWinCon(turn) != 0:
            if turn == 'p':
                
                if self.energyPlayed == False:
                    #print("Player Added energy play here " + str(self.energyPlayed))
                    for i in range(len(self.playerHand)):
                        if self.playerHand[i].Card_Type == "Energy":
                            legalMoves.append((self.playEnergy,turn,i))
                            passFlag = False
                            self.energyPlayed = True
                if len(self.playerBench) < 5:
                    #print("Attempted to play bench pokemon")
                    for i in range(len(self.playerHand)):
                        if self.playerHand[i].Card_Type == "Pokemon":
                            if self.playerHand[i].Stage == 0 and len(self.playerBench) < 5:
                                legalMoves.append((self.playBasic,i, turn))
                                passFlag = False

                if self.retreated == False and (self.playerActive[0].RetreatCost <= len(self.playerActive[0].Energies)):
                    #print("Attempted to retreat")
                    for i in range(len(self.playerBench)):
                        legalMoves.append((self.retreat,i,turn))
                        passFlag = False
                if self.checkEnergyCost(self.playerActive[0].Attack_One_Cost, self.playerActive[0].Energies):
                    legalMoves.append((self.attack, turn, self.playerActive[0].Attack_One_Name, self.playerActive[0].Attack_One_Damage, self.playerActive[0].Attack_One_Cost))
                    passFlag = False
                if passFlag == True:
                    legalMoves.append((self.passTurn, turn))
                    #print("passed turn")

            elif turn == 'o':
                if self.energyPlayed == False:
                    #print("Opponent Added energy play here")
                    for i in range(len(self.oppHand)):
                        if self.oppHand[i].Card_Type == "Energy":
                            legalMoves.append((self.playEnergy,turn,i))
                            passFlag = False
                            self.energyPlayed = True
                for i in range(len(self.oppHand)):
                    if self.oppHand[i].Card_Type == "Pokemon":
                        if self.oppHand[i].Stage == 0 and len(self.oppBench) < 5:
                            legalMoves.append((self.playBasic,i, turn))
                            passFlag = False

                if self.retreated == False and (self.oppActive[0].RetreatCost <= len(self.oppActive[0].Energies)):
                    for i in range(len(self.oppBench)):
                        legalMoves.append((self.retreat,i,turn))
                        passFlag = False
                if self.checkEnergyCost(self.oppActive[0].Attack_One_Cost, self.oppActive[0].Energies):
                    legalMoves.append((self.attack, turn, self.oppActive[0].Attack_One_Name, self.oppActive[0].Attack_One_Damage, self.oppActive[0].Attack_One_Cost))
                    passFlag = False
 
                if passFlag == True:
                    legalMoves.append((self.passTurn, turn))
        return legalMoves
 
    
    def makeMove(self, move):
 
        move[0](*move[1:])
        return

    def playEnergy(self, turn, index):
        ## ONCE PER TURN (Typically)
        ## Plays an energy from hand to a pokemon
        #print("Energy played flag is: " + str(self.energyPlayed) + " at start of function")
        if self.energyPlayed is not True:
            if turn == 'p':
                if index < len(self.playerHand):
                    if self.playerHand[index].Card_Type == "Energy":
                        #print("Player attached " + self.playerHand[index].Name)
                        self.playerActive[0].Energies.append(self.playerHand.pop(index))
                        
                    if debug:
                        for i in range(len(self.playerActive[0].Energies)):
                            print(self.playerActive[0].Energies[i].Name)
                        print("Player's Energy count is " + str(len(self.playerActive[0].Energies)))
            if turn == 'o':
                if index < len(self.oppHand):
                    if self.oppHand[index].Card_Type == "Energy":
                        #print("Opponent attached " + self.oppHand[index].Name)
                        self.oppActive[0].Energies.append(self.oppHand.pop(index))
                    if debug:
                        for i in range(len(self.oppActive[0].Energies)):
                            print(self.oppActive[0].Energies[i].Name)
                        print("Opponent's Energy count is " + str(len(self.oppActive[0].Energies)))
        
        self.energyPlayed = True
        #print("Energy played flag is: " + str(self.energyPlayed) + " at end of function")
#
    def checkWinCon(self, turn):
        if len(self.oppDeck) <= 0 or len(self.playerPrize) <= 0 or len(self.oppActive) <= 0:
            if turn == 'p':
                return 1
            elif turn == 'o':
                return 0
        elif len(self.playerDeck) <= 0 or len(self.oppPrize) <= 0 or len(self.playerActive) <= 0:
            if turn == 'p':
                return 0
            elif turn == 'o':
                return 1
        else:
            return 0.5

 
    def retreat(self, pokemonIndex, turn):
        ## ONCE PER TURN (typically)
        ## Switches active with a bench pokemon
        if turn == 'p':
            #print("active before: " + self.playerBench[0].Name)
            if self.playerActive[0].RetreatCost <= len(self.playerActive[0].Energies):
                for i in range(self.playerActive[0].RetreatCost):
                    self.playerDiscard.append(playerActive[0].Energies.pop(0))
                self.switch(pokemonIndex, turn)
                self.retreated = True
            #else:
                #print("thats not a pokemon")

    def switch(self, pokemonIndex, turn):
        if len(self.playerBench) > 0:
            temp = self.playerActive.pop(0)
            self.playerActive.append(self.playerBench.pop(pokemonIndex))
            self.playerBench.append(temp)
            #print("active after: " + self.playerActive[0].Name)
            
    
    def playBasic(self, handIndex, turn):
        ## Plays a basic from hand to bench, space permitting)
        
        if turn == 'p':
            
            if len(self.playerBench) < 5:
                
                print("player played " + self.playerHand[handIndex].Name + " to the bench!")
                self.playerBench.append(self.playerHand.pop(handIndex))
        elif turn == 'o':
            
            if len(self.oppBench) < 5:
                print("Oppenent played " + self.oppHand[handIndex].Name + " to the bench!")
                self.oppBench.append(self.oppHand.pop(handIndex))
    

class Card():
    Name = ''
    Card_Type = ''
    #Basic = False
    Hp = 0
    Attack_One_Damage = 0
    Attack_One_Name = ''
    Attack_One_Cost = ''
    Attack_Two_Damage = 0
    Attack_Two_Name = ''
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
            if self.Stage > 0:
                self.PreEvolution = obj['PreEvolution']
            self.Hp = obj['Hp']
            self.Power = obj['Power']
            self.Attack_One_Damage = obj['Attack1Damage']
            self.Attack_One_Name = obj['Attack1Name']
            self.Attack_One_Cost = obj['Attack1Cost']
            self.Attack_Two_Damage = obj['Attack2Damage']
            self.Attack_Two_Name = obj['Attack2Name']
            self.Attack_Two_Cost = obj['Attack2Cost']
            self.Retreat_Cost = obj['RetreatCost']
            self.Weakness = obj['Weakness']
            self.Resistance = obj['Resistance']
            self.Energies = obj['Energies']
        if self.Card_Type == 'Item' or self.Card_Type == 'Supporter' or self.Card_Type == 'Stadium' or self.Card_Type == 'Tool':
            self.Effect = obj['Effect']
    def isBasic(self):
        if self.Card_Type == 'Pokemon':
            return self.Stage == 0
        else:
            return False
    def setOwner(self, owner):
        self.Owner = owner

