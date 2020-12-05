## Created this file to hold all the deck related funcitons
## Earlier iteration of the program had the deck functions in the Game Loop file
## Seperated the deck from game loop to better organize 

## Deck file holds all of the deck and deck creation functions


import GameManager_clean as GameManager
debug = False

def newDeck(gameboard):
        
        ##Creates a new deck. During testing we only have one deck
        ## When out of testing, each funtion will be a complete deck.
        

        for i in range(3): # adds 3 Buizel to both decks
                obj = GameManager.Card(buizel)
                if debug:
                        print("Buizel added to player's deck")
                gameboard.playerDeck.append(obj)
                obj = GameManager.Card(buizel)
                if debug:
                        print("Buizel added to opponent's deck")
                gameboard.oppDeck.append(obj)
                
                obj = GameManager.Card(totodile) #add 3 Totodile to both deck
                if debug:
                        print("Totodile added to player's deck")
                gameboard.playerDeck.append(obj)
                obj = GameManager.Card(totodile)
                if debug:
                        print("Totodile added to opponent's deck")
                gameboard.oppDeck.append(obj)

        for i in range(4):
                obj = GameManager.Card(froakie) #adds 4 froakie
                gameboard.playerDeck.append(obj)
                obj = GameManager.Card(froakie)
                gameboard.oppDeck.append(obj)
                

                obj = GameManager.Card(remoraid)  #adds 4 remoraid
                gameboard.playerDeck.append(obj)
                obj = GameManager.Card(remoraid) 
                gameboard.oppDeck.append(obj)
                

                obj = GameManager.Card(wingull) #adds 4 wingull
                gameboard.playerDeck.append(obj)
                obj = GameManager.Card(wingull)
                gameboard.oppDeck.append(obj)        
        
        for i in range(42): #add 42 energy
                obj = GameManager.Card(metal)
                gameboard.playerDeck.append(obj)
                obj = GameManager.Card(metal)
                gameboard.oppDeck.append(obj)

## Templates for the exact cards being used
## These will either be inside the functions for the deck or in a database/different file in the future
buizel = {'Name' : 'Buizel',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Pokemon_Type' : "W",
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



froakie = {'Name' : 'Froakie',
        'Card_Type' : 'Pokemon',
        'Stage' : 0,
        'Pokemon_Type' : "W",
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

remoraid = {'Name' : 'Remoraid',
        'Card_Type' : 'Pokemon',
        'Pokemon_Type' : "W",
        'Stage' : 0,
        'Hp' : 60,
        'Power' : False,
        'Attack1Damage' : 30,
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

totodile = {'Name' : 'Totodile',
        'Card_Type' : 'Pokemon',
        'Pokemon_Type' : "W",
        'Stage' : 0,
        'Hp' : 70,
        'Power' : False,
        'Attack1Damage' : 10,
        'Attack1Name' : 'Water Gun',
        'Attack1Cost' : 'M',
        'Attack2Damage' : 20,
        'Attack2Name' : 'Bite',
        'Attack2Cost' : 'MC',
        'RetreatCost' : 1,
        'Weakness' : 'P',
        'Resistance' : '',
        'Pokemon_Type' : 'P',
        'Energies' : []}

wingull = {'Name' : 'Wingull',
        'Card_Type' : 'Pokemon',
        'Pokemon_Type' : "W",
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


metal = {'Name' : 'Metal Energy',
        'Card_Type' : 'Energy',
        'Effect' : ''}
