##Senior Project 2
##Project Vulpix


pokemon = []
pkmnCount = []
pkmnSetNum = []

trainers = []
trainerCount = []
trainerSetNum = []

energy = []
energyCount = []
energySetNum = []


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



    def playerDrawCard():
        playerHand.append(playerDeck[playerDeckIndex])
        playerDeckIndex += 1
        #return(playerHand)

    def setup():
        # Need to randomize deck amd assign it to the deck list
        # Then draw 7 cards
        # Check for a basic
        # If Basics in hand then place a basic on bench and fill up the prize list
        # If no basics then set mulligan and shuffle/redraw

    
    
    
def pkmnWordSplit(line, test, i):
    global pokemon
    global pkmnCount
    global pkmnSetNum
    j = 0

    for word in line.split(): #splits the words from the line
        
        if '*' in word:
            continue  #ignores the *
        elif word.isdigit():
            if j == 0:
                pkmnCount.append(int(word))
                j = 1
            elif j == 1:
                pkmnSetNum.append(int(word))
                j = 0
                
        elif word.isspace():
            continue  #ignores spaces
        else:
            i += 1  #one at least one word was found
            if i >= 1:  #if one word was found then we need to combine it with other words on line
                test += word  #adds word to a temp string
                test += " "
                #print(i)
                #print("Test is: "+ test)
            if i > 1:  #All pokemon have a name and a set, so i would be greater than 1(ie name and set)
                #pokemon.append(test) #adds the string to pokemon array
                #### ****NEEDS DONE****  ####
                #here we would want to split the set from the pokemon name(might be better to do it before this point, but we could have a setlist array and look for the set list and pull it out or something)
                #and then create a pokemon object and add it's set number
                #we may also want to call the lookup funtion to lookup the card
                #in database and input all the other information
                pass
        #print("Line is: " + line)
        #print("Word is: " + word)
    pokemon.append(test)

def trainerWordSplit(line, test, i):
    global trainer
    global trainerCount
    global trainerSetNum
    j = 0

    for word in line.split(): #splits the words from the line
        
        if '*' in word:
            continue  #ignores the *
        elif word.isdigit():
            if j == 0:
                trainerCount.append(int(word))
                j = 1
            elif j == 1:
                trainerSetNum.append(int(word))
                j = 0
                
        elif word.isspace():
            continue  #ignores spaces
        else:
            i += 1  #one at least one word was found
            if i >= 1:  #if one word was found then we need to combine it with other words on line
                test += word  #adds word to a temp string
                test += " "
                #print(i)
                #print("Test is: "+ test)
            if i > 1:  #All pokemon have a name and a set, so i would be greater than 1(ie name and set)
                #pokemon.append(test) #adds the string to pokemon array
                #### ****NEEDS DONE****  ####
                #here we would want to split the set from the pokemon name(might be better to do it before this point, but we could have a setlist array and look for the set list and pull it out or something)
                #and then create a pokemon object and add it's set number
                #we may also want to call the lookup funtion to lookup the card
                #in database and input all the other information
                pass
        #print("Line is: " + line)
        #print("Word is: " + word)
    trainers.append(test)

def energyWordSplit(line, test, i):
    global energy
    global energyCount
    global energySetNum
    j = 0

    for word in line.split(): #splits the words from the line
        
        if '*' in word:
            continue  #ignores the *
        elif word.isdigit():
            if j == 0:
                energyCount.append(int(word))
                j = 1
            elif j == 1:
                energySetNum.append(int(word))
                j = 0
                
        elif word.isspace():
            continue  #ignores spaces
        else:
            i += 1  #one at least one word was found
            if i >= 1:  #if one word was found then we need to combine it with other words on line
                test += word  #adds word to a temp string
                test += " "
                #print(i)
                #print("Test is: "+ test)
            if i > 1:  #All pokemon have a name and a set, so i would be greater than 1(ie name and set)
                #pokemon.append(test) #adds the string to pokemon array
                #### ****NEEDS DONE****  ####
                #here we would want to split the set from the pokemon name(might be better to do it before this point, but we could have a setlist array and look for the set list and pull it out or something)
                #and then create a pokemon object and add it's set number
                #we may also want to call the lookup funtion to lookup the card
                #in database and input all the other information
                pass
        #print("Line is: " + line)
        #print("Word is: " + word)
    energy.append(test)    
def deckList(filename):
    global pokemon
    flag = ''
    
    test2 = ''
    file = open(filename, "r")
    i = -1
    for line in file:
        i = 0
        test = ''
        if "##Pokémon" in line:  ##Start of the pokemon group
            flag = 'p'  #sets a flag for later tests I need this to parse the words in each line
            print("Pokemon start here!")
        elif "##Trainer Cards" in line:
            flag = 't'
            print("Trainers start here!")
        elif "##Energy" in line:
            flag = 'e'
            print("Energies start here!")

        if flag == 'p' and '*' in line:  #checks for the flag and the * since that is how PCTGO does thier items in thier decklists

            pkmnWordSplit(line, test, i)
        elif flag == 't' and '*' in line:
            trainerWordSplit(line, test, i)

        elif flag == 'e' and '*' in line:
            energyWordSplit(line, test, i)
    print(pokemon)
    print(" Length is: " + str(len(pokemon)))
    print(pkmnCount)
    print(" Length is: " + str(len(pkmnCount)))
    print(pkmnSetNum)
    print(" Length is: " + str(len(pkmnSetNum)))
    print(trainers)
    print(energy)
    file.close()


filename = input("Enter a file name: ")
deckList(filename)

