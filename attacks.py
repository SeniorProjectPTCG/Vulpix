def attackDamage(defender, damage):
	defender.Hp -= damage

def checkWeakeness(attacker, defender, damage):
	if (attacker.Pokemon_Type == defender.Weakness):
		damage *= 2
	return damage

def whimsyTackle(attacker, defender, damage):
	x = randint(0,1) #coin flip
	damage = checkWeakeness(attacker, defender, damage)
	if x == 1:
		attackDamage(defender, damage)
	else:
		print("tails, attack does no damage")

def amnesia(attacker, defender, damage, player, choice):
	damage = checkWeakeness(attacker, defender, damage)
	if player == 'p':
		oppAttackNotAvail = choice
	else:
		playerAttackNotAvail = choice
	attackDamage(defender, damage)

def facade(attacker, defender, damage, player):
	if player == 'p':
		if playerBurned == True or playerPoisoned == True:
			damage += 80
	damage = checkWeakeness(attacker, defender, damage)
	attackDamage(attacker, defender, damage)

def recklessCharge(attacker, defender, damage):
	damage = checkWeakeness(attacker, defender, damage)
	attackDamage(defender, damage)
	attackDamage(attacker, 10)

def agility(attacker, defender, damage, player):
	if player == 'p':
		playerAgility = True
	else:
		oppAgility = True
	damage = checkWeakeness(attacker, defender, damage)
	attackDamage(attacker, damage)

def swallowDive(attacker, defender, damage, player):
	if player == 'p':
		if playerAgility == True:
			damage += 80
		playerAgility = False
	else:
		if oppAgility == True:
			damage += 80
	damage = checkWeakeness(attacker, defender, damage)
	attackDamage(defender, damage)

def coreBeam(attacker, defender, damage, player):
	damage = checkWeakeness(attacker, defender, damage)
	for i in attacker.Energies:
		if i.Name == "Metal Energy":
			x = i
	if player == 'p':
		playerDiscard.append(attacker.Energies.pop(x))
	else:
		oppDiscard.append(attacker.Energies.pop(x))
	attackDamage(defender, damage)

def dustGathering(player):
	if player == 'p':
		playerDrawCard()
	else:
		oppDrawCard()

def teleport(pokemonIndex, player):
	switch(pokemonIndex, player)

def shiningArrow(attacker, defender, location):
	if location == 'active':
		damage = checkWeakeness(attacker, defender, damage)
	attackDamage(defender, damage)

def fangsOfTheSunne(attacker, defender, damage, player):
	if player == 'p':
		playerAttackNotAvail = 2
	else:
		oppAttackNotAvail = 2
	damage = checkWeakeness(attacker, defender, damage)
	attackDamage(defender, damage)

def dangerousBlow(attacker, defender, damage):
	if defender.Stage == 0:
		damage += 60
	damage = checkWeakeness(attacker, defender, damage)
	attackDamage(defender, damage)

def anchorShot(attacker, defender, damage, player):
	if player == 'p':
		oppCantRetreat = True
	else:
		playerCantRetreat = True
	damage = checkWeakeness(attacker, defender, damage)
	attackDamage(defender, damage)

#Not sure how to impliment Weather Teller [Castform]

def waterPulse(attacker, defender, damage, player):
	if player == 'p':
		oppAsleep = True
	else:
		playerAsleep = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)