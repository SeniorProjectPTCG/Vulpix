
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
import mcts

#import gamedisplay
## This class will control the entire Gameboard
class Gameboard():
    turn = 'p'
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

    #Can only retreat once per turn
    retreated = False

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
            print("Player drew a Card!")
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
            print("Opponent drew a Card!")
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
        for i in range(len(self.playerHand)):
            print(self.playerHand[i].Name)
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

    def checkEnergyCost(self, cost, attached):
        print("Checking energy costs...")
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
            print("Has enough energy to attack")
            return True
        else:
            print("Does not have enough energy to attack")
            
            return False

    ##  THINGS THAT CAN BE DONE DURING TURNS
    def attack(self, turn, attackName, damage, cost):
        ## Use one of the card's attack. This ends the turn
        ## Must have proper amount and type of energy
        #global turn
        if turn == 'p':
            if self.checkEnergyCost(cost, self.playerActive[0].Energies):
                print(self.oppActive[0].Name + " HP: " + str(self.oppActive[0].Hp))
                print(self.playerActive[0].Name + " uses " + attackName + " deals " + str(self.playerActive[0].Attack_One_Damage) + " damage")
                if attackName == "Dangerous Blow":
                    attacks.dangerousBlow(self.playerActive[0], self.oppActive[0], damage)
                elif attackName == "Whimsy Tackle":
                    attacks.whimsyTackle(self.playerActive[0], self.oppActive[0], damage)
                elif attackName == "Amnesia":
                    attacks.amnesia(self.playerActive[0], self.oppActive[0], damage, 'o', random.randint(1,2)) #Currently does random choice
                elif attackName == "Facade":
                    attacks.facade(self.playerActive[0], self.oppActive[0], damage, turn)
                elif attackName == "Reckless Charge":
                    attacks.recklessCharge(self.playerActive[0], self.oppActive[0], damage)
                elif attackName == "Agility":
                    attacks.agility(self.playerActive[0], self.oppActive[0], damage, turn)
                elif attackName == "Swallow Dive":
                    attacks.swallowDive(self.playerActive[0], self.oppActive[0], damage, turn)
                #elif attackName == "Core Beam":
                #    attacks.coreBeam(self, self.playerActive[0], self.oppActive[0], damage, turn)
                elif attackName == "Dust Gathering":
                    attacks.dustGathering(self,turn)
                elif attackName == "Teleport":
                    attacks.teleport(0, turn)  ### ONLY SWITCHES WITH FIRST BENCH SPOT CURRENTLY NEEDS CHNAGED
                elif attackName == "Shining Arrow":
                    attacks.shiningArrow(self.playerActive[0], self.oppActive[0], "active") #NEEDS SUPPORT FOR BENCH
                elif attackName == "Fangs of the Sunne":
                    attacks.fangsOfTheSunne(self.playerActive[0], self.oppActive[0], damage, turn)
                elif attackName == "Anchor Shot":
                    attacks.anchorShot(self.playerActive[0], self.oppActive[0], damage, turn)
                elif attackName == "Weather Teller":
                    attacks.weatherTeller(self, self.playerActive[0], turn)
                elif attackName == "Water Pulse":
                    attacks.waterPulse(self.playerActive[0], self.oppActive[0], damage, turn)
                else:
                    attacks.basicAttack(self.playerActive[0],self.oppActive[0],self.playerActive[0].Attack_One_Damage)
                print(self.oppActive[0].Hp)
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
                        if len(self.playerPrize) <= 0:
                            print("Player has taken all prizes - Player wins")
                            sys.exit()
                    else:
                        print("opponent out of Pokemon - Player wins")
                        sys.exit()
        elif turn == 'o':
            if self.checkEnergyCost(cost, self.oppActive[0].Energies):
                print(self.playerActive[0].Name + " HP: " + str(self.playerActive[0].Hp))
                print(self.oppActive[0].Name + " uses " + attackName + " deals "  + str(self.oppActive[0].Attack_One_Damage) + " damage")
                if attackName == "Dangerous Blow":
                    attacks.dangerousBlow(self.oppActive[0],self.playerActive[0] , damage)
                elif attackName == "Whimsy Tackle":
                    attacks.whimsyTackle(self.oppActive[0], self.playerActive[0], damage)
                elif attackName == "Amnesia":
                    attacks.amnesia(self.oppActive[0], self.playerActive[0], damamge, turn, randint(1,2)) #Currently does random choice
                elif attackName == "Facade":
                    attacks.facade(self.oppActive[0], self.playerActive[0], damage, turn)
                elif attackName == "Reckless Charge":
                    attacks.recklessCharge(self.oppActive[0], self.playerActive[0], damage)
                elif attackName == "Agility":
                    attacks.agility(self.oppActive[0], self.playerActive[0], damage, turn)
                elif attackName == "Swallow Dive":
                    attacks.swallowDive(self.oppActive[0], self.playerActive[0], damage, turn)
                #elif attackName == "Core Beam":
                #    attacks.coreBeam(self, self.oppActive[0], self.playerActive[0], damage, turn)
                elif attackName == "Dust Gathering":
                    attacks.dustGathering(self, turn)
                elif attackName == "Teleport":
                    attacks.teleport(0, turn)  ### ONLY SWITCHES WITH FIRST BENCH SPOT CURRENTLY NEEDS CHNAGED
                elif attackName == "Shining Arrow":
                    attacks.shiningArrow(self.oppActive[0], self.playerActive[0], "active") #NEEDS SUPPORT FOR BENCH
                elif attackName == "Fangs of the Sunne":
                    attacks.fangsOfTheSunne(self.oppActive[0], self.playerActive[0], damage, turn)
                elif attackName == "Anchor Shot":
                    attacks.anchorShot(self.oppActive[0], self.playerActive[0], damage, turn)
                elif attackName == "Weather Teller":
                    attacks.weatherTeller(self, self.oppActive[0], turn)
                elif attackName == "Water Pulse":
                    attacks.waterPulse(self.oppActive[0], self.playerActive[0], damage, turn)
                else:
                    attacks.basicAttack(self.oppActive[0],self.playerActive[0],self.oppActive[0].Attack_One_Damage)
                print(self.playerActive[0].Hp) 
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
                        if len(self.oppPrize) <= 0:
                            print("Opponent has taken all prizes - Opponent wins")
                            sys.exit()
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
                    for i in range(len(self.playerActive[0].Energies)-1,-1,-1):
                        self.playerHand[pokemonIndex].Energies.append(self.playerActive[0].Energies.pop(i))
                    if len(self.playerActive[0].Tools) > 0:
                        self.playerHand[pokemonIndex].Tools.append(self.playerActive[0].Tools.pop(0))
                    self.playerHand[pokemonIndex].Pokemon.append(self.playerActive.pop(0))
                    self.playerActive.append(self.playerHand[pokemonIndex])
                    #self.playerHand.pop(pokemonIndex)
##            elif loc == 'bench':
##                if self.playerBench[benchIndex].Name == self.playerHand[pokemonIndex].PreEvolution: #Pokemon evolves into pokemon in bench
##                    for i in range(len(self.playerBench[benchIndex].Energies)-1,-1,-1):
##                        self.playerHand[pokemonIndex].Energies.append(self.playerBench[benchIndex].Energies.pop(i))
##                    if len(self.playerBench[benchIndex].Tools) > 0:
##                        self.playerHand[pokemonIndex].Tools.append(self.playerBench[benchIndex].Tools.pop(0))
##                    self.playerHand[pokemonIndex].Pokemon.append(self.playerBench.pop(benchIndex))
##                    self.playerBench[benchIndex].append(self.playerHand[pokemonIndex])
##                # do the same for bench

    def getMoves(self, turn):
        legalMoves = []
        if turn == 'p':
            print("legal moves: "+ str(legalMoves))
            if self.supporterPlayed == False:
                for i in range(len(self.playerHand)):
                    if self.playerHand[i].Card_Type == "Supporter":
                        legalMoves.append((self.playSupporter,turn, i))
            if self.energyPlayed == False:
                print(legalMoves)
                for i in range(len(self.playerHand)):
                    if self.playerHand[i].Card_Type == "Energy":
                        legalMoves.append((self.playEnergy,turn))
                        print(legalMoves)
            for i in range(len(self.playerHand)):
                if self.playerHand[i].Card_Type == "Pokemon":
                    if self.playerHand[i].Stage == 0 and len(self.playerBench) < 5:
                        legalMoves.append((self.playBasic,turn, i))
                    elif self.playerHand[i].Card_Type == "Pokemon" and self.playerHand[i].Stage > 0:
                        if self.playerHand[i].PreEvolution == self.playerActive[0].Name:
                            legalMoves.append((self.evolve,i, "active", 0, turn))
                        else:
                            for j in range(len(self.playerBench)):
                                if self.playerBench[j].Name == self.playerHand[i].PreEvolution:
                                    legalMoves.append((self.evolve,i, "bench", j, turn))
                elif self.playerHand[i].Card_Type == "Item":
                    legalMoves.append((self.playItem,turn, i))
            if self.retreated == False:
                for i in range(len(self.playerBench)):
                    legalMoves.append((self.retreat,i,turn))
            if self.checkEnergyCost(self.playerActive[0].Attack_One_Cost, self.playerActive[0].Energies):
                legalMoves.append((self.attack, turn, self.playerActive[0].Attack_One_Name, self.playerActive[0].Attack_One_Damage, self.playerActive[0].Attack_One_Cost))
            if self.playerActive[0].Attack_Two_Name != "None":
                if self.checkEnergyCost(self.playerActive[0].Attack_Two_Cost, self.playerActive[0].Energies):
                    legalMoves.append((self.attack, turn, self.playerActive[0].Attack_Two_Name, self.playerActive[0].Attack_Two_Damage, self.playerActive[0].Attack_Two_Cost))
        elif turn == 'o':
            if supporterPlayed == False:
                for i in range(len(oppHand)):
                    if oppHand[i].Card_Type == "Supporter":
                        legalMoves.append((self.playSupporter,turn, i))
            if energyPlayed == False:
                for i in range(len(oppHand)):
                    if oppHand[i].Card_Type == "Energy":
                        legalMoves.append((self.playEnergy,turn))
            for i in range(len(oppHand)):
                if oppHand[i].Card_Type == "Pokemon":
                    if oppHand[i].Stage == 0 and len(oppBench) < 5:
                        legalMoves.append((self.playBasic,turn, i))
                    elif self.oppHand[i].Card_Type == "Pokemon" and self.oppHand[i].Stage > 0:
                        if self.oppHand[i].PreEvolution == self.oppActive[0].Name:
                            legalMoves.append((self.evolve,i, "active", 0, turn))
                        else:
                            for j in range(len(self.oppBench)):
                                if self.oppBench[j].Name == self.oppHand[i].PreEvolution:
                                    legalMoves.append((self.evolve,i, "bench", j, turn))
                elif oppHand[i].Card_Type == "Item":
                    legalMoves.append((self.playItem,turn, i))
            if self.retreated == False:
                for i in range(len(oppBench)):
                    legalMoves.append((self.retreat,i,turn))
            if self.checkEnergyCost(self.oppActive[0].Attack_One_Cost, self.oppActive[0].Energies):
                legalMoves.append((self.attack, turn, self.oppActive[0].Attack_One_Name, self.oppActive[0].Attack_One_Damage, self.oppActive[0].Attack_One_Cost))
            if self.oppActive[0].Attack_Two_Name != "None":
                if self.checkEnergyCost(self.oppActive[0].Attack_Two_Cost, self.oppActive[0].Energies):
                    legalMoves.append((self.attack, turn, self.oppActive[0].Attack_Two_Name, self.oppActive[0].Attack_Two_Damage, self.oppActive.Attack_Two_Cost))
        return legalMoves
    #stadiumPlayed = False
    
    
    def playEnergy(self, turn, index):
        ## ONCE PER TURN (Typically)
        ## Plays an energy from hand to a pokemon
        if turn == 'p':
            if self.playerHand[index].Card_Type == "Energy":
                print("Player attached " + self.playerHand[index].Name)
                self.playerActive[0].Energies.append(self.playerHand.pop(index))
            if debug:
                for i in range(len(self.playerActive[0].Energies)):
                    print(self.playerActive[0].Energies[i].Name)
                print("Player's Energy count is " + str(len(self.playerActive[0].Energies)))
        if turn == 'o':
            if self.oppHand[index].Card_Type == "Energy":
                print("Opponent attached " + self.oppHand[index].Name)
                self.oppActive[0].Energies.append(self.oppHand.pop(index))
            if debug:
                for i in range(len(self.oppActive[0].Energies)):
                    print(self.oppActive[0].Energies[i].Name)
                print("Opponent's Energy count is " + str(len(self.oppActive[0].Energies)))
##        temp = []
##        if turn == 'p':
##            for i in range(len(self.playerHand)):
##                if self.playerHand[i].Card_Type == 'Energy':
##                   temp.append(i)
##            if len(temp) > 0:
##                temp.sort(reverse = True)
##                for i in temp:
##                    if self.energyPlayed == False:
##                        #print(self.playerHand[i].Name)
##                        name = self.playerHand[i].Name
##                        self.playerActive[0].Energies.append(self.playerHand.pop(i))
##                        self.energyPlayed = True
##                        print(name + " played")
##        if turn == 'o':
##            for i in range(len(self.oppHand)):
##                if self.oppHand[i].Card_Type == 'Energy':
##                   temp.append(i)
##            if len(temp) > 0:
##                temp.sort(reverse = True)
##                for i in temp:
##                    if self.energyPlayed == False:
##                        name = self.oppHand[i].Name
##                        self.oppActive[0].Energies.append(self.oppHand.pop(i))
##                        self.energyPlayed = True
##                        print(name + " played")
        
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

    def turns(self, turn):
        # Check for wins
        # Check for statuses(Mainly ones that happen between turns)
        # Player's Turn
        #self.winConditions()
        print("\n\nNew Turn STARTED!!!")
        
##        print("Menu")
##        print("1. Play Basic")
##        print("2. Play Stadium")
##        print("3. Play Energy")
##        print("4. Play Tool")
##        print("5. Play Supporter")
##        print("6. Play Attack")
##        print("7. End Turn")
        #choice = int(input("What would you like to do?"))
        if turn == 'p':

            if not self.drawForTurn:
                self.playerDrawCard()
                self.drawForTurn = True
            if debug:
                self.printHand(turn)
            print("Getting moves")
            #print(self.getMoves(turn))
            choice = mcts.uct(self, 5)
            print("Player AI chose ", choice)
            ## SHOULD CHECK FOR THINGS BEFORE CALLING FUNCTIONS OR THAT SHOULD BE WHAT WE DO I THINK

            if choice == 1: #Play Basic
                i = 0
                while i < len(self.playerHand):
                    
               
                    if self.playerHand[i].isBasic():
                        
                        self.playBasic(i, turn)
                        print("basic found")
                        break
                    else:
                        print("no valid basics")
                        i += 1
                self.turns(turn)
            elif choice == 2:
                self.playStadium(turn)
                self.turns(turn)
            elif choice == 3:
                i = 0
                while self.playerHand[i].Card_Type != "Energy":
                    i += 1
                if self.energyPlayed == False:
                    self.playEnergy(turn, i)
                else:
                    print("Energy already played!")
                self.energyPlayed = True
                self.turns(turn)
            elif choice == 4:
                self.playTool(turn)
                self.turns(turn)
            elif choice == 5:
                self.supporterPlayed = True
                playSupporter(turn)
                self.turns(turn)
            elif choice == 6:
                atkNum = random.randint(1,2)
                if atkNum == 1:
                    self.attack(turn, self.playerActive[0].Attack_One_Name, self.playerActive[0].Attack_One_Damage, self.playerActive[0].Attack_One_Cost)
                elif atkNum == 2:
                    if self.playerActive[0].Attack_Two_Name == "None":
                        self.attack(turn, self.playerActive[0].Attack_One_Name, self.playerActive[0].Attack_One_Damage, self.playerActive[0].Attack_One_Cost)
                    else:
                        self.attack(turn, self.playerActive[0].Attack_Two_Name, self.playerActive[0].Attack_Two_Damage, self.playerActive[0].Attack_Two_Cost)
                #self.attack(turn)
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turns("o")
                pass
            elif choice == 7:
                print("EXIT")
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turns("o")

            elif choice == 8:
                #Evolve
                for i in range(len(self.playerHand)):
                    if self.playerHand[i].Card_Type == "Pokemon" and self.playerHand[i].Stage > 0:
                        if self.playerHand[i].PreEvolution == self.playerActive[0].Name:
                            self.evolve(i, "active", 0, turn)
                            index = i
                        else:
                            for j in range(len(self.playerBench)):
                                if self.playerBench[j].Name == self.playerHand[i].PreEvolution:
                                    self.evolve(i, "bench", j, turn)
                self.playerHand.pop(index)
                self.turns(turn)
                            
                        
                

        # Opponent's Turn
        elif turn == 'o':
            if not self.drawForTurn:
                self.oppDrawCard()
                self.drawForTurn = True
            choice = ai.oppAI(self)
            print("Opponent AI chose ", choice)
            
            if choice == 1: #Play Basic
                i = 0
                while i < len(self.oppHand):
                    if self.oppHand[i].isBasic():
                        
                        self.playBasic(i, turn)
                        print("basic found")
                        break
                    else:
                        print("no valid basics")
                        
                        i += 1
                self.turns(turn)
            elif choice == 2:
                self.playStadium(turn)
                self.turns(turn)
            elif choice == 3:
                i = 0
                while self.oppHand[i].Card_Type != "Energy":
                    i += 1
                self.playEnergy(turn, i)
                self.energyPlayed = True
                self.turns(turn)
            elif choice == 4:
                self.playTool(turn)
                self.turns(turn)
            elif choice == 5:
                self.supporterPlayed = True
                playSupporter(turn)
                self.turns(turn)
            elif choice == 6:
                atkNum = random.randint(1,2)
                if atkNum == 1:
                    self.attack(turn, self.oppActive[0].Attack_One_Name, self.oppActive[0].Attack_One_Damage, self.oppActive[0].Attack_One_Cost)
                elif atkNum == 2:
                    if self.oppActive[0].Attack_Two_Name == "None":
                        self.attack(turn, self.oppActive[0].Attack_One_Name, self.oppActive[0].Attack_One_Damage, self.oppActive[0].Attack_One_Cost)
                    else:
                        self.attack(turn, self.oppActive[0].Attack_Two_Name, self.oppActive[0].Attack_Two_Damage, self.oppActive[0].Attack_Two_Cost)
                #self.attack(turn)
 
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turns("p")
                pass
            elif choice == 7:
                print("EXIT")
                self.drawForTurn = False
                self.energyPlayed = False
                self.supporterPlayed = False
                self.stadiumPlayed = False
                self.turns("p")



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
    Attack_One_Nme = ''
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
        if self.Card_Type == 'Item' or self.Card_Type == 'Supporter' or self.Card_Type == 'Stadium' or self.Card_Type == 'Tool':
            self.Effect = obj['Effect']
    def isBasic(self):
        if self.Card_Type == 'Pokemon':
            return self.Stage == 0
        else:
            return False
    def setOwner(self, owner):
        self.Owner = owner

