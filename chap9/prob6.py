class Critter:
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    def talk(self):
        print("\nHi, I'm", self.__name)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name == "":
            print("Critter's name can't be empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")


if __name__ == '__main__':
    crit = Critter("Poochie")

    crit.talk()

    print("\nMy critter's name is:", crit.get_name())

    print("\nAttempting to change my critter's name.")
    crit.set_name("")

    print("\nAttempting to change my critter's name again.")
    crit.set_name("Randolph")

    crit.talk()
