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
import random
debug = True
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

    def randomizeDecks(self):
        temp = []
        if debug:
            print("Size of Player's Deck: " + str(len(self.playerDeck)))
            
            

        random.shuffle(self.playerDeck)
        random.shuffle(self.oppDeck)
        if debug:
            for i in range(len(self.playerDeck)):
                print("Card " + str(i) + " of Player's deck is " + self.playerDeck[i]["Name"])
            print("\n")
            print("Size of Opponent's Deck: " + str(len(self.oppDeck)))
            for i in range(len(self.oppDeck)):
                print("Card " + str(i) + " of Opponent's deck is " + self.oppDeck[i].Name)


    def playerDrawCard(self):
        
        self.playerHand.append(self.playerDeck.pop(self.playerDeckIndex))
        #self.playerDeckIndex += 1
        
    
    def oppDrawCard(self):
        self.oppHand.append(self.oppDeck.pop(self.oppDeckIndex))
        #self.oppDeckIndex += 1

    def playerIsBasic(self, i):
        #Searches player's hand for a basic pokemon
        if self.playerHand[i]["Basic"] == True: #This will need to be changed once the card structure is finalized. Currently each card is a dict and the hand is a list of card dicts
            return True
        else:
            return False

    def playerSetPrize(self):
        if debug:
            print("Setting up player prizes")
        self.playerPrize.append(self.playerDeck.pop(self.playerDeckIndex))
        #self.playerDeckIndex += 1

    def oppIsBasic(self, i):
        #Searches player's hand for a basic pokemon
        return self.oppHand[i].isBasic()
    
        

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
                print(self.playerPrize[i]["Name"])

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
            

class Card():
    ##Option #1 - Class based cards
    Name = ''
    Card_Type = ''
    Type = ''
    Basic = False
    HP = 0
    Attack_One = 0
    Attack_Two = 0

    def __init__(self, name, card_type, Type, basic, hp, atk1, atk2):
        self.Name = name
        self.Card_Type = card_type
        self.Type = Type
        self.Basic = basic
        self.HP = hp
        self.Attack_One = atk1
        self.Attack_Two = atk2
    def isBasic(self):
        return self.Basic

    
    
## Option #2 - Dioctionary based cards        
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
Card1 = Card("Pikachu", "Pokemon", "Electric", True, 60, 10, 30)
Card2 = Card("Raichu", "Pokemon", "Electric", False, 120, 50, 100)
Card3 = Card("Pokeball", "Item", "None", False, 0, 0, 0)
Card4 = Card("Bridgett", "Supporter", "None", False, 0, 0, 0)
Card5 = Card("Electric Energy", "Energy", "Electric", False, 0, 0, 0)
obb.playerDeck = [card1, card2, card3, card4, card5, card1, card2, card3, card2 , card1, card2 , card3, card1, card4, card3, card5, card5, card5, card5, card5]
obb.oppDeck = [Card1, Card2, Card3, Card2 , Card1, Card2 , Card3, Card1, Card4, Card3, Card5, Card5, Card5, Card5, Card5, Card5]

obb.setup()
if debug:
    for i in range(len(obb.playerDeck)):
        print("Card " + str(i) + " of Player's deck is " + obb.playerDeck[i]["Name"])
    for i in range(len(obb.playerHand)):
        print("Card " + str(i) + " of Player's hand is " + obb.playerHand[i]["Name"])
