import os
import shelve
import random


def read_prob(file_path):
    f = shelve.open(file_path)
    n = str(random.randint(1, 5))

    print("\t\t", f[str(0)]['title'], sep="", end="\n\n")

    return f[n]


def start_game(prob):
    corr_num = prob['correct']
    print(prob['category'], end="\n\n")
    print(prob['question'], end="\n\n")

    for i, answer in enumerate(prob['answer']):
        print(i + 1, "-", answer)

    num = int(input("\nWhat's your answer? : "))
    if num == corr_num:
        print("Correct! answer :\n", corr_num, "\"", prob['answer'][corr_num - 1], "\"")
    else:
        print("Wrong.answer :\n", corr_num, "\"", prob['answer'][corr_num - 1], "\"")

    print("\nexplanation :")
    print(prob['explanation'])


if __name__ == '__main__':
    path = os.getcwd()
    file_path = os.path.join(path, "problem_db")

    print("\t\tWelcome to Trivia Challenge!\n")
    prob = read_prob(file_path)

    start_game(prob)







