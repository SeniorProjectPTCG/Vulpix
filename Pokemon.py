pokemon = []
pkmnCount = []
pkmnSetNum = []
class Pokemon:
    name = ''
    setAbbr = ''
    setNum = ''
    def __init__(self, name, setAbbr, setNum):
        self.name = name
        self.setAbbr = setAbbr
        self.setNum = setNum

    
def createObjects():
    global pokemon
    global pkmnCount
    global pkmnSetNum

    #for i in range(len(pokemon)):
        #pokemon[i] = Pokemon(pokemon[i], 
    
def wordSplit(line, test, i):
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
##            #This should probably be split into a function since we will need to call it for each flag type
##            for word in line.split(): #splits the words from the line
##                if '*' in word:
##                    continue  #ignores the *
##                elif word.isdigit():
##                    continue  #ignores the numbers
##                elif word.isspace():
##                    continue  #ignores spaces
##                else:
##                    i += 1  #one at least one word was found
##                    if i >= 1:  #if one word was found then we need to combine it with other words on line
##                        test += word  #adds word to a temp string
##                        #print(i)
##                        #print("Test is: "+ test)
##                    if i > 1:  #All pokemon have a name and a set, so i would be greater than 1(ie name and set)
##                        pokemon.append(test) #adds the string to pokemon array
##                        #### ****NEEDS DONE****  ####
##                        #here we would want to split the set from the pokemon name(might be better to do it before this point, but we could have a setlist array and look for the set list and pull it out or something)
##                        #and then create a pokemon object and add it's set number
##                        #we may also want to call the lookup funtion to lookup the card
##                        #in database and input all the other information
##                #print("Line is: " + line)
##                #print("Word is: " + word)
            wordSplit(line, test, i)
    print(pokemon)
    print(" Length is: " + str(len(pokemon)))
    print(pkmnCount)
    print(" Length is: " + str(len(pkmnCount)))
    print(pkmnSetNum)
    print(" Length is: " + str(len(pkmnSetNum)))
    file.close()


filename = input("Enter a file name: ")
deckList(filename)
