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

    while True:
        ask_yes_no = input("Do you require the first move? <y/n>:")

        if ask_yes_no == "y" or ask_yes_no == "Y":
            return "X", "O"
        elif ask_yes_no == "n" or ask_yes_no == "N":
            return "O", "X"
        else:
            print("please enter <y/n>")


def new_board():
    board = [[" " for x in range(3)] for y in range(3)]
    return board


def display_board(board):
    for r in range(3):
        print("\t\t", board[r][0], " | ", board[r][1], " | ", board[r][2], sep="")
        if r != 2:
            print("\t\t---------")


def human_move(board, human):
    move = int(input("Where will you move? <0 - 8>:"))


def computer_move(board, human, computer):
    pass


def play_tic_tac_toe(human, computer):
    turn = "X"
    board = new_board()
    display_board(board)

    if turn == human:
        move = human_move(board, human)
        board[move] = human

    else:
        move = computer_move(board, human, computer)
        board[move] = computer




if __name__ == '__main__':
    # pieces==True : human first, pieces==False : computer first
    human, computer = display_instruct()
    play_tic_tac_toe(human, computer)
    board = new_board()
    display_board(board)
    print(human, computer)
