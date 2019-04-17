import random



alterOfTheSunneInPlayAttacks = False

def setAlterOfTheSunneInPlay(flag):
	global alterOfTheSunneInPlayAttacks
	alterOfTheSunneInPlayAttacks = flag

def attackDamage(defender, damage):
	defender.Hp -= damage

def checkWeakness(attacker, defender, damage):
	damage = checkResist(attacker, defender, damage)
	if (alterOfTheSunneInPlayAttacks == True):
		if (defender.Pokemon_Type == 'F' or defender.Pokemon_Type == 'M'):
			return damage
	elif (attacker.Pokemon_Type == defender.Weakness):
		damage *= 2
	return damage

def checkResist(attacker, defender, damage):
	if defender.Resistance == attacker.Pokemon_Type:
		damage -= 20
		if damage < 0:
			damage = 0
	return damage

def basicAttack(attacker, defender, damage):
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def whimsyTackle(attacker, defender, damage):
        ## Flip a coin. If tails, this attack does nothing. 
	x = random.randint(0,1) #coin flip
	damage = checkWeakness(attacker, defender, damage)
	if x == 1:
		attackDamage(defender, damage)
	else:
		print("tails, attack does no damage")

def amnesia(attacker, defender, damage, player, choice):
        ## Choose 1 of your opponent's Active Pokémon's attacks.
        ## That Pokémon can't use that attack during your opponent's next turn.
	damage = checkWeakness(attacker, defender, damage)
	if player == 'p':
		oppAttackNotAvail = choice
	else:
		playerAttackNotAvail = choice
	attackDamage(defender, damage)

def facade(attacker, defender, damage, player):
        ## If this Pokémon is Burned or Poisoned, this attack does 80 more damage. 
	if player == 'p':
		if playerBurned == True or playerPoisoned == True:
			damage += 80
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(attacker, defender, damage)

def recklessCharge(attacker, defender, damage):
        ## This Pokémon does 10 damage to itself.
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)
	attackDamage(attacker, 10)

def agility(attacker, defender, damage, player):
        ## Flip a coin. If heads, prevent all effects of attacks,
        ## including damage, done to this Pokémon during your opponent's
        ## next turn
	if player == 'p':
		playerAgility = True
	else:
		oppAgility = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(attacker, damage)

def swallowDive(attacker, defender, damage, player):
        ## If this Pokémon used Agility during your last turn,
        ## this attack does 80 more damage. 
	if player == 'p':
		if playerAgility == True:
			damage += 80
		playerAgility = False
	else:
		if oppAgility == True:
			damage += 80
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def coreBeam(self, attacker, defender, damage, player):
        ## Discard an M energy from this card
	damage = checkWeakness(attacker, defender, damage)
	j = 0
	for i in attacker.Energies:
                if i.Name == "Metal Energy":
                        x = j
                j += 1
                
	if player == 'p':
		self.playerDiscard.append(attacker.Energies.pop(x))
	else:
		self.oppDiscard.append(attacker.Energies.pop(x))
	attackDamage(defender, damage)

def dustGathering(self, player):
        ## Draw a card.
	if player == 'p':
		self.playerDrawCard()
	else:
		self.oppDrawCard()

def teleport(pokemonIndex, player):
        ## Switch this Pokémon with 1 of your Benched Pokémon
	switch(pokemonIndex, player)

def shiningArrow(attacker, defender, location): ## NEEDS BENCH ATTACK SUPPORT
        ## This attack does 50 damage to 1 of your opponent's Pokémon.
        ## (Don't apply Weakness and Resistance for Benched Pokémon)
	if location == 'active':
		damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def fangsOfTheSunne(attacker, defender, damage, player):
        ## This Pokémon can't use Fangs of the Sunne during your next turn.
	if player == 'p':
		playerAttackNotAvail = 2
	else:
		oppAttackNotAvail = 2
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def dangerousBlow(attacker, defender, damage):
        ## If your opponent's Active Pokémon is a Basic Pokémon,
        ## this attack does 60 more damage. 
	if defender.Stage == 0:
		damage += 60
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def anchorShot(attacker, defender, damage, player):
        ## The Defending Pokémon can't retreat during your opponent's next turn. 
	if player == 'p':
		oppCantRetreat = True
	else:
		playerCantRetreat = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def weatherTeller(self,attacker, player):
        ## Search your deck for up to 2 Stadium cards, reveal them,
        ## and put them into your hand.
        ## Then, shuffle your deck. 
	if player == 'p':
		for i, e in reversed(list(enumerate(self.playerDeck))):
			if e.Card_Type == "Stadium":
				self.playerHand.append(self.playerDeck.pop(i))
	else:
		for i, e in reversed(list(enumerate(self.oppDeck))):
			if e.Card_Type == "Stadium":
				self.oppHand.append(self.oppDeck.pop(i))

def waterPulse(attacker, defender, damage, player):
        ## You opponent's Active Pokémon is now Asleep.
	if player == 'p':
		oppAsleep = True
	else:
		playerAsleep = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def blownKiss(attacker, defender, damage):
	attackDamage(defender, damage)

def psybeam(attacker, defender, damage, player):
	if player == 'p':
		oppConfused = True
	else:
		playerConfused = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def flickeringFlames(attacker, defender, damage, player):
	if player == 'p':
		oppAsleep = True
	else:
		playerAsleep = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def shatterShot(attacker, defender, damage):
	energyCount = 0
	for i in attacker.Energies:
		if i.Name == 'Psychic Energy':
			energyCount += 1
	damage = damage * energyCount
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def wingsOfTheMoon(attacker, defender, damage, player):
	#####NEED TO MOVE ENERGIES#####
	if player == 'p':
		if len(playerBench) > 0:
			for i in reversed(list(enumerate(attacker.Energies))):
				playerBench[0].Energies.append(attacker.Energies.pop(i))
	else:
		if len(oppBench) > 0:
			for i in reversed(list(enumerate(attacker.Energies))):
				oppBench[0].Energies.append(attacker.Energies.pop(i))
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def supernaturalDance(attacker, defender, player):
	damageCounter = 0
	if player == 'p':
		for i in oppDiscard:
			if i.Card_Type == 'Pokemon':
				damageCounter += 1
	else:
		for i in playerDiscard:
			if i.Card_Type == 'Pokemon':
				damageCounter += 1
	damage = damageCounter * 10
	attackDamage(defender, damage)

def revelationDance(attacker, defender, damage):
	if len(stadium) > 0:
		damage = checkWeakness(attacker, defender, damage)
		attackDamage(defender, damage)

def venoshock(attacker, defender, damage, player):
	if player == 'p':
		if oppPoisoned == True:
			damage += 40
	else:
		if playerPoisoned == True:
			damage += 40
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def flamethrower(attacker, defender, damage, player):
	if player == 'p':
		playerDiscard.append(attacker.Energies.pop(0))
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def filch(player):
	if player == 'p':
		playerDrawCard()
		playerDrawCard()
	else:
		oppDrawCard()
		oppDrawCard()

def copycat(attack, attacker, defender, damage, player, choice, pokemonIndex, location):
	if attack == whimseyTackle:
		whimsyTackle(attacker, defender, damage)
	if attack == amnesia:
		amnesia(attacker, defender, damage, player, choice)
	if attack == facade:
		facade(attacker, defender, damage, player)
	if attack == recklessCharge:
		recklessCharge(attacker, defender, damage)
	if attack == agility:
		agility(attacker, defender, damage, player)
	if attack == swallowDive:
		swallowDive(attacker, defender, damage, player)
	if attack == coreBeam:
		coreBeam(attacker, defender, damage, player)
	if attack == dustGathering:
		dustGathering(player)
	if attack == teleport:
		teleport(pokemonIndex, player)
	if attack == shiningArrow:
		shiningArrow(attacker, defender, location)
	if attack == fangsOfTheSunne:
		fangsOfTheSunne(attacker, defender, damage, player)
	if attack == dangerousBlow:
		dangerousBlow(attacker, defender, damage)
	if attack == anchorShot:
		anchorShot(attacker, defender, damage, player)
	if attack == weatherTeller:
		weatherTeller(attacker, player)
	if attack == waterPulse:
		waterPulse(attacker, defender, damage, player)
	if attack == blownKiss:
		blownKiss(attacker, defender, damage)
	if attack == psybeam:
		psybeam(attacker, defender, damage, player)
	if attack == flickeringFlames:
		flickeringFlames(attacker, defender, damage, player)
	if attack == shatterShot:
		shatterShot(attacker, defender, damage)
	if attack == wingsOfTheMoon:
		wingsOfTheMoon(attacker, defender, damage, player)
	if attack == supernaturalDance:
		supernaturalDance(attacker, defender, player)
	if attack == revelationDance:
		revelationDance(attacker, defender, damage)
	if attack == venoshock:
		venoshock(attacker, defender, damage, player)
	if attack == flamethrower:
		flamethrower(attacker, defender, damage, player)
	if attack == filch:
		filch(player)
	if attack == copycat:
		pass
	else:
		basicAttack(defender, damage)

# card1 = {'Name' : 'Solgaleo',
#         'Card_Type' : 'Pokemon',
#         'Stage' : 2,
#         'Hp' : 160,
#         'Power' : False,
#         'Attack1Damage' : 0,
#         'Attack1Effect' : '',
#         'Attack1Cost' : 'MC',
#         'Attack2Damage' : 170,
#         'Attack2Effect' : '',
#         'Attack2Cost' : 'MMC',
#         'RetreatCost' : 3,
#         'Weakness' : 'R',
#         'Resistance' : 'P',
#         'Pokemon_Type' : 'P'}

# card2 = {'Name' : 'Cosmoem',
#         'Card_Type' : 'Pokemon',
#         'Stage' : 1,
#         'Hp' : 90,
#         'Power' : False,
#         'Attack1Damage' : 0,
#         'Attack1Effect' : 'Switch this Pokémon with 1 of your Benched Pokémon',
#         'Attack1Cost' : 'C',
#         'Attack2Damage' : 0,
#         'Attack2Effect' : 'None',
#         'Attack2Cost' : 'None',
#         'RetreatCost' : 3,
#         'Weakness' : 'P',
#         'Resistance' : '',
#         'Pokemon_Type' : 'P'}

# class Card():
#     Name = ''
#     Card_Type = ''
#     #Basic = False
#     Hp = 0
#     Attack_One_Damage = 0
#     Attack_One_Effect = ''
#     Attack_One_Cost = ''
#     Attack_Two_Damage = 0
#     Attack_Two_Effect = ''
#     Attack_Two_Cost = ''
    
#     RetreatCost = 0
#     Pokemon_Type = ''

#     Weakness = ''
#     Resistance = ''
#     PreEvolution = ''
#     Pokemon = []
#     Stage = 0
#     Effect = ''
#     Owner = ''
#     Energies = []
#     Tools = []

#     def __init__(self, obj):
#         self.Name = obj['Name']
#         self.Card_Type = obj['Card_Type']
#         if self.Card_Type == 'Pokemon':
#             self.Stage = obj['Stage']
#             self.Hp = obj['Hp']
#             self.Power = obj['Power']
#             self.Attack_One_Damage = obj['Attack1Damage']
#             self.Attack_One_Effect = obj['Attack1Effect']
#             self.Attack_One_Cost = obj['Attack1Cost']
#             self.Attack_Two_Damage = obj['Attack2Damage']
#             self.Attack_Two_Effect = obj['Attack2Effect']
#             self.Attack_Two_Cost = obj['Attack2Cost']
#             self.Retreat_Cost = obj['RetreatCost']
#             self.Weakness = obj['Weakness']
#             self.Resistance = obj['Resistance']
#             self.Pokemon_Type = obj['Pokemon_Type']
#         if self.Card_Type == 'Item' or self.Card_Type == 'Supporter' or self.Card_Type == 'Stadium' or self.Card_Type == 'Tool':
#             self.Effect = obj['Effect']
#     def isBasic(self):
#         if self.Card_Type == 'Pokemon':
#             return self.Stage == 0
#         else:
#             return False
#     def setOwner(self, owner):
#         self.Owner = owner

# atk = Card(card1)
# dfd = Card(card2)
# print(dfd.Hp)
# basicAttack(atk, dfd,50)
# print(dfd.Hp)
