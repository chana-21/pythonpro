import random

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

        # first move : X
        # rast move : O
        if ask_yes_no == "y" or ask_yes_no == "Y":
            return "X", "O"
        elif ask_yes_no == "n" or ask_yes_no == "N":
            return "O", "X"
        else:
            print("please enter <y/n>")


def initial_board():
    board = [[" " for x in range(3)] for y in range(3)]
    return board


def display_board(board):
    for r in range(3):
        print("\t\t", board[r][0], " | ", board[r][1], " | ", board[r][2], sep="")
        if r != 2:
            print("\t\t---------")


def player(board):
    first, last = 0, 0
    for i in board:
        for j in i:
            if j == "X":
                first += 1
            elif j == "O":
                last += 1

    if first == last:
        return "X"
    else:
        return "O"


def human_move(board, human, cases):
    while(True):
        move = int(input("Where will you move? <0 - 8>:"))
        for i in cases:
            if move == i:
                print()

    row = int(move / 3)
    col = int(move - (row * 3))
    board[row][col] = human
    return board


def computer_move(board, computer):
    move = random.randint(0, 8)
    row = int(move / 3)
    col = int(move - (row * 3))
    board[row][col] = computer
    return board

def actions(board):
    cases = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                cases.append((i * 3) + j)

    return cases


def play_tic_tac_toe(human, computer):
    board = initial_board()
    turn = player(board)
    display_board(board)
    while(True):
        cases = actions(board)
        if turn == human:
            board = human_move(board, human, cases)

        else:
            board = computer_move(board, computer, cases)

        display_board(board)
        turn = player(board)



if __name__ == '__main__':
    human, computer = display_instruct()
    play_tic_tac_toe(human, computer)
    board = initial_board()
    print(human, computer)
