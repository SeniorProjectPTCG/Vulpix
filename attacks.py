def whimsyTackle(attacker, defender, damage){
	x = randint(0,1)
	if (attacker.Pokemon_Type == defender.Weakness):
		damage *= 2
	if x == 1:
		defender.Hp -= damage
	else:
		print("tails, attack does no damage")
}
#Not sure how to do amnesia yet
#Not sure how to do Facade yet
def recklessCharge(attacker, defender, damage){
	if (attacker.Pokemon_Type == defender.Weakness):
		damage *= 2
	defender.Hp -= damage
	attacker.Hp -= 10
}
#Not sure how to do agility yet
#Not sure how to do Sqallow dive yet
def coreBeam(attacker, defender, damage){
	if (attacker.Pokemon_Type == defender.Weakness):
		damage *= 2
	#Not sure how to decide which discard pile to append to
}