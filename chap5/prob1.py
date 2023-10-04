inventory = ("sword", "aromor", "shield", "healing potion")
print("Your items:")
for i in inventory:
	print(i)

print("\nPress the enter Key to continue.", end='')
while True:
	enter = input()
	if enter == "":
		break
print("You have", len(inventory), "items in your possession.\n")


print("Press the enter Key to continue.", end='')
while True:
	enter = input()
	if enter == "":
		break
if "healing potion" in inventory:
	print("You will live to fight another day.\n")

index = int(input('Enter the index number for an item in inventory:'))
print("At index", index, "is", inventory[index], "\n")

first_slice = int(input('Enter the index number to begin a slice:'))
last_slice = int(input('Enter the index number to end the slice:'))

print("inventory[", first_slice, ":", last_slice, "]\t\t", inventory[first_slice:last_slice])

print("\nPress the enter Key to continue.", end='')
while True:
	enter = input()
	if enter == "":
		break
chest = ("gold", "gems")
print("You find a chest. It contains:\n", chest)

print("You add the contents of the ches to your inventory.")
print("Your inventory is now:")
inventory += chest
print(inventory)
