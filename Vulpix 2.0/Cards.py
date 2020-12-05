class Card():
    Name = ''
    Card_Type = ''
    #Basic = False
    Hp = 0
    Attack_One_Damage = 0
    Attack_One_Name = ''
    Attack_One_Cost = ''
    Attack_Two_Damage = 0
    Attack_Two_Name = ''
    Attack_Two_Cost = ''
    RetreatCost = 0
    Pokemon_Type = ''
    Weakness = ''
    Resistance = ''
    Stage = 0
    Owner = ''
    Energies = []
  

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
            self.Energies = obj['Energies']
       
    def isBasic(self):
        if self.Card_Type == 'Pokemon':
            return self.Stage == 0
        else:
            return False
    def setOwner(self, owner):
        self.Owner = owner