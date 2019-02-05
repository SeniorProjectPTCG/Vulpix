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

class Card():
    Name = ''
    Card_Type = ''
    Type = ''
    Basic = False
    HP = 0
    Attack_One = 0
    Attack_Two = 0

    def __init__(self, obj):
        self.Name = obj['Name']
        self.Card_Type = obj['Card_Type']
        if self.Card_Type == 'Pokemon':
            self.Stage = obj['Stage']
            self.Hp = obj['Hp']
            self.Power = obj['Power']
            self.Attack_One_Damage = obj['Attack1Damage']
            self.Attack_One_Effect = obj['Attack1Effect']
            self.Attack_One_Cost = obj['Attack1Cost']
            self.Attack_Two_Damage = obj['Attack2Damage']
            self.Attack_Two_Effect = obj['Attack2Effect']
            self.Attack_Two_Cost = obj['Attack2Cost']
    def isBasic(self):
        if self.Card_Type == 'Pokemon':
            return self.Stage == 0
        else:
            return False

