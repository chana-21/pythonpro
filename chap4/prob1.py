import random

print("I sense your energy. Your true emtions are coming across my screen.")
print("You are...")

mood = random.randrange(0,4)

if mood == 0:
	print("----------")
	print("|        |")
	print("| 0   0  |")
	print("|   <    |")
	print("| .    . |")
	print("|  ....  |")
	print("----------")

elif mood == 1:
	print("----------")
	print("|        |")
	print("| 0   0  |")
	print("|   <    |")
	print("| .....  |")
	print("|        |")
	print("----------")

elif mood == 2:
	print("----------")
	print("|        |")
	print("| 0   0  |")
	print("|   <    |")
	print("|  ....  |")
	print("| .    . |")
	print("----------")

else:
	print("Illegal mood value!")

