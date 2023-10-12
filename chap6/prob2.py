scores = [("Moe", 1000), ("Larry", 1500), ("Curly", 3000)]
choice = None
while True:
	print("\n\tHigh Scores Keeper\n")
	print("\t0 - Quit")
	print("\t1 - List Scores")
	print("\t2 - Add a Score")
	choice = int(input("\nChoice: "))

	if choice == 1:
		scores.sort(key=lambda x: x[1], reverse=True)	

		print("\nHigh Scores Keeper\n")
		print("NAME\tSCORE")
		for i in scores:
			name, score = i
			print(name, "\t", score)
	

	elif choice == 2:
		player_name = input("\nWhat is the player's name?:")
		player_score = int(input("What score did the player get?:"))
		entry = (player_name, player_score)
		scores.append(entry)
	

	elif choice == 0:
		break
	

	else :pass 

