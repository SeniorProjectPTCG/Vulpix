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
debug = True
import random
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
        
        self.playerHand.append(self.playerDeck.pop(self.playerDeckIndex))
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



    ###  OPPONENT MEMBER FUNCTIONS  ###


    def oppDrawCard(self):
        self.oppHand.append(self.oppDeck.pop(self.oppDeckIndex))
        #self.oppDeckIndex += 1

    def oppIsBasic(self, i):
        #Searches player's hand for a basic pokemon
        return self.oppHand[i].isBasic()

    def oppSetPrize(self):
        if debug:
            print("Setting up opponent's prizes")
        self.oppPrize.append(self.oppDeck.pop(self.oppDeckIndex))

    
        

    def setup(self):
        # Need to randomize deck amd assign it to the deck list
        # Then draw 7 cards
        # Check for a basic
        # If Basics in hand then place a basic on bench/active and fill up the prize list
        # If no basics then set mulligan and shuffle/redraw
        
        i = 0
        basic = False
        count = 0
        mulligan = 0
        if debug:
            print("Shuffling Decks...")
            
        self.randomizeDecks()
        
        if debug:
            print("Starting to set up Player's board...")
            
        
        #Draw cards from player hand
        for i in range(7): # should do this 7 times...need to test to be sure
            
            self.playerDrawCard()
            self.oppDrawCard()
        #print(self.playerHand)
        #print(self.oppHand)

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
            print("No basic found!! Take a Mulligan!")


        #If player has basic set up pries#
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
##                temp = []
##                num = count
##                i =0
##                while i < len(self.playerHand):
##                    if self.playerIsBasic(i):
##                        temp.append(self.playerHand.pop(i))
##                        num -= 1
##                    if num == 0:
##                        break
##                    i+=1    
##                    
##                
##                    
##                random.shuffle(temp)
##                for i in range(len(temp)):
##                    print(temp[i].Name)
##                self.playerActive.append(temp.pop(0)) #Randomly selects the active from list of basics
##                if count <= 5:
##                    for i in range(count-1):
##                        for i in range(len(temp)):
##                            print(temp[i].Name)
##                        self.playerBench.append(temp.pop(i)) #Fills bench up with all basics  NOT IDEAL!!!! TESTING PURPOSES ONLY!!!!
##                ## Needs an option for user to select active or AI in our case.
                print("Too many basics")
                
                        

        if debug:
            print("Starting to set up Opponent's board...")
        basic = False
        count = 0

        for i in range(len(self.oppHand)):  #loop length of player hand - 1
            if self.oppIsBasic(i):
                basic = True #if atleast one basic is found
                count += 1
                print(str(count) + " basic(s) found!!")
            else:
                continue
                ## Need to add support for mulligan
        if count is 0:
            print("No basic found!! Take a Mulligan!")

        #If player has basic set up pries#
        if basic: 
            for i in range(6):
                self.oppSetPrize()
                #print(self.oppPrize[i]["Name"])
            # If Player only has one basic it must go to active spot
            if count == 1:
                for i in range(len(self.oppHand)):
                    if self.oppIsBasic(i):
                        self.oppActive.append(self.oppHand.pop(i)) # pops the basic from hand to active spot
                        break
            else: # more than one basic
                ## Needs an option for user to select active or AI in our case.
                pass

    def turn(self):
        # Player's Turn
        if turn == 'p':
            break

        # Opponent's Turn
        elif turn == 'o':
            pass

    def winConditions(self):

        ## Opponent Win Conditions ##
        if len(playerActive) == 0 and len(playerBench) == 0:
            print("Opponent wins!")
        if len(oppPrize) == 0:
            print("Opponent wins!")
        if len(playerDeck) == 0:
            print("Opponent wins!")

        ## Player Win Conditions ##
        if len(oppActive) == 0 and len(oppBench) == 0:  # Empty bench and active
            print("Opponent wins!")
        if len(playerPrize) == 0:  # No prizes left
            print("Opponent wins!")
        #Deckout may need to be re-evaluated since deckouts only occur when the player draws for turn. This shoould work but I didn't spend too much time on it
        if len(oppDeck) == 0:  # Deckout
            print("Opponent wins!")

class Card():
    Name = ''
    Card_Type = ''
    Type = ''
    Basic = False
    HP = 0
    Attack_One_Damage = 0
    Attack_One_Effect = ''
    Attack_One_Cost = ''
    Attack_Two_Damage = 0
    Attack_Two_Effect = ''
    Attack_Two_Cost = ''
    
    Retreat_Cost = 0
    Pokemon_Type = ''
    Weakness = ''
    Resistance = ''
    #Pre-Evolution = ''

    Effect = ''

    def __init__(self, obj):
        self.Name = obj['Name']
        self.Card_Type = obj['Card_Type']
        if self.Card_Type == 'Pokemon':
            self.Stage = obj['Stage']
            self.Hp = obj['Hp']
            self.Power = obj['Power']
            #self.Attack_One_Damage = obj['Attack1Damage']
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

