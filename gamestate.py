class gameboard():
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



    def playerDrawCard():
        playerHand.append(playerDeck[playerDeckIndex])
        playerDeckIndex += 1
        #return(playerHand)
    
    def oppDrawCard():
        oppHand.append(oppDeck[oppDeckIndex])
        oppDeckIndex += 1
        #return(playerHand)

    def setup():
        # Need to randomize deck amd assign it to the deck list
        # Then draw 7 cards
        # Check for a basic
        # If Basics in hand then place a basic on bench and fill up the prize list
        # If no basics then set mulligan and shuffle/redraw
        i = 1

        #Draw cards from player hand
        for i in range(8): # should do this 7 times...need to test to be sure  
            playerDrawCard()
            oppDrawCard()
            
