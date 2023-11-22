class Critter:
    def __init__(self, name):
        self.name = name
        self.__mood_level = 100

    def talk(self):
        print("\nHi, I'm", self.name)
        if self.__mood_level >= 75:
            print("I feel so Great! ヽ(✿ﾟ▽ﾟ)ノ")
        elif self.__mood_level >= 50:
            print("I feel good. ╰(￣ω￣ｏ)")
        elif self.__mood_level >= 25:
            print("I feel so so. (´。＿。｀)")
        elif self.__mood_level >= 0:
            print("I feel mad. (σ｀д′)σ")

        return -20

    def feed(self):
        food = [0, 20, 15, 10, 5]

        while True:
            print("\n\t\tWhat kind of food do you feed your critter?\n")
            print("\t\t0 - Quit")
            print("\t\t1 - leaf\t(Mood +20)")
            print("\t\t2 - carrot\t(Mood +15)")
            print("\t\t3 - bread\t(Mood +10)")
            print("\t\t4 - cereal\t(Mood +5)\n")

            level = input("Food select: ")
            if level.isdigit() and (0 <= int(level) <= 4):
                if not int(level) == 0:
                    print("\nYammy~")
                return food[int(level)]

    def play(self):
        print("\n\tWheee!")
        return 25

    def setMood(self, level):
        if level == 0:
            return

        if level < 0:
            print("\n\tmood -", end='')
        else:
            print("\n\tmood +", end='')
        print(abs(level))

        self.__mood_level += level

        if self.__mood_level > 100:
            self.__mood_level = 100
        elif self.__mood_level < 0:
            self.__mood_level = 0

    def getMood(self):
        print("\n\tYour critter mood level is ", self.__mood_level, "/ 100")


if __name__ == '__main__':
    name = input("What do you want to name your critter?: ")
    crit = Critter(name)

    while True:
        print("\n\t\tGritter Caretaker\n")
        print("\t\t0 - Quit")
        print("\t\t1 - Listen to your critter")
        print("\t\t2 - Feed your critter")
        print("\t\t3 - Play with your critter\n")
        choice = input("Choice: ")

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice == 0:
            break
        elif choice == 1:
            level = crit.talk()
            crit.setMood(level)
            crit.getMood()
        elif choice == 2:
            level = crit.feed()
            crit.setMood(level)
            crit.getMood()
        elif choice == 3:
            level = crit.play()
            crit.setMood(level)
            crit.getMood()



