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

    def feed(self, foods):
        while True:
            print("\n\t\tWhat kind of food do you feed your critter?\n")
            print("\t\t0 - Quit")
            for i, food in enumerate(foods, start=1):
                print(f"\t\t{i} - {food.name}\t(Mood +{food.level})")

            choice = input("\nFood select: ")
            if choice.isdigit() and (0 <= int(choice) <= len(foods)):
                choice_idx = int(choice)
                if choice_idx == 0:
                    return 0
                selected_food = foods[choice_idx - 1]
                print("\nYummy~")
                return selected_food.getLevel()

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
        return self.__mood_level


class Food:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def getLevel(self):
        return self.level

    def setCritterLevel(self, critter):
        critter.setMood(self.level)


if __name__ == '__main__':
    name = input("What do you want to name your critter?: ")
    crit = Critter(name)

    # Creating food objects
    leaf = Food("Leaf", 20)
    carrot = Food("Carrot", 15)
    bread = Food("Bread", 10)
    cereal = Food("Cereal", 5)

    foods = [leaf, carrot, bread, cereal]

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
        elif choice == 2:
            level = crit.feed(foods)
            crit.setMood(level)
        elif choice == 3:
            level = crit.play()
            crit.setMood(level)

        mood_level = crit.getMood()
        print("\n\tYour critter mood level is ", mood_level, "/ 100")

