from start_game import play_tic_tac_toe


def display_instruct():
    print("\tWelcome to the graeatest intellectual challenge of all time: Tic-Tac-Toe.")
    print("\tThis will be a showdown betwwen your human brain and my silicon processor.\n")

    print("You will make your move known by entering a number, 0 - 8. The number")
    print("will correspond to the board position as illustrated:")
    print("\t\t0 | 1 | 2")
    print("\t\t---------")
    print("\t\t3 | 4 | 5")
    print("\t\t---------")
    print("\t\t6 | 7 | 8")
    print("\tPrepare yourself, human. The ultimate battle is about to begin.\n")


def difficulty_level():
    print("[1]\tEasy")
    print("[2]\tHard")
    while True:
        diff = int(input("Select the difficulty level <1/2> : "))
        if diff == 1 or diff == 2:
            break

    return diff


def sequence():
    while True:
        ask_yes_no = input("Do you require the first move? <y/n>:")
        # first move : X
        # rast move : O
        if ask_yes_no == "y" or ask_yes_no == "Y":
            return "X", "O"
        elif ask_yes_no == "n" or ask_yes_no == "N":
            return "O", "X"


if __name__ == '__main__':
    display_instruct()
    diff = difficulty_level()
    human, computer = sequence()

    play_tic_tac_toe(human, computer, diff)
