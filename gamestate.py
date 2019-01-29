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



    def playerDrawCard(self):
        
        self.playerHand.append(self.playerDeck[self.playerDeckIndex])
        self.playerDeckIndex += 1
        
    
    def oppDrawCard(self):
        self.oppHand.append(self.oppDeck[self.oppDeckIndex])
        self.oppDeckIndex += 1

    def playerIsBasic(self):
        #Searches player's hand for a basic pokemon
        for i in range(self.playerHand.length()-1):  #loop length of player hand - 1
            if playerHand[i] == 'Basic': #This will need to be changed once the card structure is finalized
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

        #Draw cards from player hand
        for i in range(7): # should do this 7 times...need to test to be sure  
            self.playerDrawCard()
            self.oppDrawCard()
        print(self.playerHand)
        print(self.oppHand)

        ###CHECK FOR BASIC HERE!!!  ##

        #If player has basic#
        for i in range(6):
            self.playerSetPrize()
        print(self.playerPrize)

    
        
            
obb = Gameboard()
obb.playerDeck = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8', 'card9', 'card01', 'card02', 'card03', 'card04', 'card05', 'card06']
obb.oppDeck = ['card11', 'card12', 'card13', 'card14', 'card15', 'card16', 'card17']
obb.setup()
