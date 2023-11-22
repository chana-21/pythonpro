import random

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")

element = random.choice(words)
element_list = list(element)

guess_list = ["_"] * len(element_list)

print("Guess the Word!!!")
print("In this game, the program selects a word at computer_move, and the player's objective is to guess the chosen word.\n")

print("Length of the selected word:", len(element_list))

attempts = len(element_list)

while True:
	print("Remaining attempts:", attempts)
	print("Current guessed word: ", end="")
	for i in guess_list:
		print(i, end=" ")
	letter = input('\nGuess a letter: ')
	
	a = False
	for index, value in enumerate(element_list):
		if value == letter and not value == guess_list[index]:
			guess_list[index] = letter
			a = True

	if a == False:
		print("Incorrect guess.")
		attempts -= 1

	if attempts <= 0:
		print("You've used up all attempts. The correct word was", element)
		break
	elif guess_list == element_list:
		print("Congratulations! You guessed the word:", element)
		break

