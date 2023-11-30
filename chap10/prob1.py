class Player:
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        print("The alien gasps and says, 'Oh, this is it. This is the big one.")
        print("Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...")

        enemy.die()


class Alien:
    def die(self):
        print("Good-bye, cruel universe.")


hero = Player()
invader = Alien()

print("\t\tDeath of an Alien\n")
hero.blast(invader)
