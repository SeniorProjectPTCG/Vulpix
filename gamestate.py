######################################################
##                 Project Vulpix                   ##
##                Senior Project 2                  ##
##                 Andrew Siddall                   ##
##                 Chris Crisson                    ##
##               Matthew Bedillion                  ##
##               Adlene Bellaoucha                  ##
##               January 30, 2019                   ##
######################################################

###################DESCRIPTION########################
## This is the game state file that handles all the game actions. It will serve as a kind of game engine for the Ai to use.
## 

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

    def playerDrawCard(self):
        
        self.playerHand.append(self.playerDeck[self.playerDeckIndex])
        self.playerDeckIndex += 1
        
    
    def oppDrawCard(self):
        self.oppHand.append(self.oppDeck[self.oppDeckIndex])
        self.oppDeckIndex += 1

    def playerIsBasic(self, i):
        #Searches player's hand for a basic pokemon
        if self.playerHand[i]["Basic"] == True: #This will need to be changed once the card structure is finalized. Currently each card is a dict and the hand is a list of card dicts
            return True
        else:
            return False

    def playerSetPrize(self):
        self.playerPrize.append(self.playerDeck[self.playerDeckIndex])
        self.playerDeckIndex += 1

    
        

    def setup(self):
        # Need to randomize deck amd assign it to the deck list
        # Then draw 7 cards
        # Check for a basic
        # If Basics in hand then place a basic on bench and fill up the prize list
        # If no basics then set mulligan and shuffle/redraw
        i = 0
        basic = False

        #Draw cards from player hand
        for i in range(7): # should do this 7 times...need to test to be sure  
            self.playerDrawCard()
            self.oppDrawCard()
        #print(self.playerHand)
        #print(self.oppHand)

        ###CHECK FOR BASIC HERE!!!  ##
        for i in range(len(self.playerHand)-1):  #loop length of player hand - 1
            if self.playerIsBasic(i):
                basic = True #if atleast one basic is found
                print("Basic found!!")
            else:
                print("No basic found!!")
            

        #If player has basic set up prices#
        if basic: 
            for i in range(6):
                self.playerSetPrize()
                print(self.playerPrize[i]["Name"])

    
        
card1 = {"Name" : "Zorua",
         "Type" : "Pokemon",
         "Basic" : True,
         "Hp" : 60,
         "Attack 1" : 20,
         "Attack 2" : 50}
card2 = {"Name" : "Ultra Ball",
         "Type" : "Item",
         "Basic" : False,
         "Hp" : False,
         "Attack 1" : "None", #Handle effects here in attacks
         "Attack 2" : "None"}
card3 = {"Name" : "Zoroark",
         "Type" : "Pokemon",
         "Basic" : False,
         "Hp" : 100,
         "Attack 1" : 50,
         "Attack 2" : 100}
card4 = {"Name" : "Guzma",
         "Type" : "Supporter",
         "Basic" : False,
         "Hp" : False,
         "Attack 1" : "None", #Handle effects here in attacks
         "Attack 2" : "None"}
card5 = {"Name" : "Dark Energy",
         "Type" : "Energy",
         "Basic" : False,
         "Hp" : False,
         "Attack 1" : "None", #Handle effects here in attacks
         "Attack 2" : "None"}
         
obb = Gameboard()
obb.playerDeck = [card1, card2, card3, card4, card5, card1, card2, card3, card2 , card1, card2 , card3, card1, card4, card3, card5, card5, card5, card5, card5,]
obb.oppDeck = [card1, card2, card3, card2 , card1, card2 , card3, card1, card4, card3, card5]
obb.setup()
