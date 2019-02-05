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

