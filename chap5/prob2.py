import random

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")

element = random.choice(words)
element_list = list(element)
random.shuffle(element_list)

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")
print("Jumbled word: ", end="")
for i in element_list:
	print(i, end='')
print()

guess_word = input('Your guess: ')

if element == guess_word:
	print("correct.")
else:
	print("Sorry, that's not correct. The word was:", element)
