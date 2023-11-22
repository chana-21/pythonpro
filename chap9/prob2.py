class Critter:
   def __init__(self):
      print("A new critter has been born!")

   def talk(self):
      print("Hi. I'm an instance of class Critter.\n")


# main
crit1 = Critter()
crit2 = Critter()
print("\n")
crit1.talk()
crit2.talk()
