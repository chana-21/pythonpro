import random

hero_hp = random.randrange(50,101)
monster_hp = random.randrange(50,101)
count = 0
print("hero HP:", hero_hp, ", monster HP:", monster_hp)

while hero_hp > 0 and monster_hp > 0:
	hero_attack = random.randrange(-10,21)
	monster_attack = random.randrange(-10,21)

	if hero_attack > 0:
		monster_hp -= hero_attack
		hero_check = "success"
	else:
		hero_check = "fail"

	if monster_attack > 0:
		hero_hp -= monster_attack
		monster_check = "success"
	else:
		monster_check = "fail"

	print("hero(HP:", hero_hp, ", attack:", hero_attack, ")", hero_check, "<-> monster(HP:", monster_hp, ", attack:", monster_attack, ")", monster_check)
	count += 1

print("--------------------------------------------")
print("Total phase:", count)
if hero_hp <= 0:
	print("Monster Win!!!!")
elif monster_hp <= 0:
	print("Hero Win!!!")
