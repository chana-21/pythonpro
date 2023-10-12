import random

def print_hangman(attempts):

    hangman = ["------", "|    |", "|", "|", "|", "|", "|", "|", "----------"]

    if attempts <= 2:
        hangman[5] = "|   /"

    if attempts == 1:
        hangman[5] = "|   / \\"

    if attempts <= 3:
        hangman[4] = "|    |"

    if attempts <= 4:
        hangman[3] = "|  --+--"

    if attempts <= 5:
        hangman[2] = "|    O"

    if attempts == 0:
        hangman[2] = "|"
        hangman[3] = "|    O"
        hangman[4] = "|  --+--"
        hangman[5] = "|    |"
        hangman[6] = "|   / \\"

    for i in hangman:
        print("\t", i)


def hangman_game():
    words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
    element = random.choice(words)
    element_list = list(element)
    guess_list = ["_"] * len(element_list)
    attempts_list = []
    attempts = 6

    while attempts > 0 and not element_list == guess_list:
        is_exists_letter = False

        print("_____________________________________________________\n")
        print_hangman(attempts)

        print("\n\tYou've used the following letters :\n\t", attempts_list, sep='')

        print("\n\tCurrent guessed word :\n\t", end="")
        for i in guess_list:
            print(i, end=" ")

        print("\n\tattempts :", attempts)

        letter = input("\n\tEnter your guess : ")

        # case not alphabet or one letter
        if not letter.isalpha() or not len(letter) == 1:
            print("\t\t\tENTER THE CORRECT LETTER!!\n")
            continue

        # change to small letter
        if letter.isupper():
            letter = letter.lower()

        # check if already entered
        for i in attempts_list:
            if i == letter:
                print("\t\t\tThe letter \'", letter, "\' is already entered.")
                is_exists_letter = True

        if is_exists_letter:
            continue

        # check if a word contains a letter
        for index, value in enumerate(element_list):
            if value == letter and not value == guess_list[index]:
                guess_list[index] = letter
                is_exists_letter = True

        if is_exists_letter:
            print("\t\t\tYes! \'", letter, "\' is in the word!\n")

        else:
            print("\t\t\tyou get incorrect.")
            print("\t\t\tThe letter \'", letter, "\' is not in the word")
            attempts -= 1

        attempts_list.append(letter)

    print("_____________________________________________________\n")
    if attempts > 0:
        print("\t------------------------------------------")
        print("\t\t\tYOU WIN!")
        print("\t\tThe word was \"", element, "\"")
        print("\t------------------------------------------")
    else:
        print_hangman(attempts)

        print("\t------------------------------------------")
        print("\t\t\tGAME OVER!")
        print("\t\tThe word was \"", element, "\"")
        print("\t------------------------------------------")


if __name__ == '__main__':
    print("\t------------------------------------------")
    print("\t---    Welcome to The Hangman Game!    ---")
    print("\t---        Press enter to start        ---")
    print("\t------------------------------------------")

    while True:
        enter = input()
        if enter == "":
            break

    hangman_game()

