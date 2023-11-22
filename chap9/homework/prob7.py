class Critter:
    def __init__(self, name):
        self.name = name
        self.__mood_level = 100

    def talk(self):
        print("\nHi, I'm", self.name)
        if self.__mood_level >= 75:
            print("I feel so Great! ヽ(✿ﾟ▽ﾟ)ノ")
            self.__mood_level -= 10
        elif self.__mood_level >= 50:
            print("I feel good. ╰(￣ω￣ｏ)")
            self.__mood_level -= 10
        elif self.__mood_level >= 25:
            print("I feel so so. (´。＿。｀)")
            self.__mood_level -= 10
        elif self.__mood_level >= 0:
            print("I feel mad. (σ｀д′)σ")
            if (self.__mood_level - 10) < 0:
                self.__mood_level = 0
            else:
                self.__mood_level -= 10

    def feed(self):
        print("\t\tWhat kind of food do you feed your critter?")
        print("\t\t0 - ")

    def play(self):
        pass

    def setMood(self, level):
        pass

    def getMood(self):
        print("Your critter mood level is ", self.__mood_level)


def print_option():
    print("\n\t\tGritter Caretaker\n")
    print("\t\t0 - Quit")
    print("\t\t1 - Listen to your critter")
    print("\t\t2 - Feed your critter")
    print("\t\t3 - Play with your critter\n")


if __name__ == '__main__':
    name = input("What do you want to name your critter?: ")
    crit = Critter(name)

    while True:
        print_option()
        choice = int(input("Choice: "))

        if choice == 0:
            break
        elif choice == 1:
            crit.talk()
        elif choice == 2:
            pass



