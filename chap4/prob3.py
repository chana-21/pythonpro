import random

num = random.randrange(1,101)
guess = 0
count = 0

print("\tWelcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

while not guess == num:
	guess = int(input('Take a guess:'))
	count += 1
	if guess < num:
		print("Higher...")
	elif guess > num:
		print("Lower...")
print("You guessed it! The number was", num)
print("And it only took you", count, "tries!")

