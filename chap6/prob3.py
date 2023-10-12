geek = {"404" : "clueless.", "Uninstalled" : "being fired."}

while True:
	print("\n\tGeek Translator\n")
	print("\t0 - Quit")
	print("\t1 - Look Up a Geek Term")
	print("\t2 - Add a Geek Term")
	print("\t3 - Redefine a Geek Term")
	print("\t4 - Delete a Geek Term\n")

	choice = int(input("Choice: "))

	if choice == 1:
		translate = input("\nWhat term do you want me to translate?: ")
		if translate in geek:
			print("\n", translate, " means ", geek[translate], sep='')
		else:
			print("\nThis translate is not define")

	elif choice == 2:
		key = input("What do you want to add a Geek term?: ")
		value = input("What does this term mean?: ")

		geek[key] = value

	elif choice == 3:
		key = input("What do you want to Redefine a Geek term?: ")
		
		if key in geek:
			value = input("Waht does this term mean?: ")
			geek[key] = value
		else:
			print("This term is not define in Geek Term")

	elif choice == 4:
		key = input("Which Term do you want to delete?: ")

		if key in geek:
			del geek[key]
			print(key, "is Delete in Geek Term")
		else:
			print("This term is not define in Geek Term")

	elif choice == 0:
		break
	
	else: pass
