class Card:
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        reply = self.rank + self.suit
        return reply


class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            reply = super().__str__()
        else:
            reply = "XX"
        return reply

    def flip(self):
        self.is_face_up = not self.is_face_up


class BJ_Card(Positionable_Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit)
        self.value = 0
        self.init_rank()

    def init_rank(self):
        if self.rank.isdigit():
            self.value = int(self.rank)
        elif self.rank == 'A':
            self.value = 1
        else:
            self.value = 10

    def get_rank(self):
        return self.value


class Chip:
    amount = 1

    def __int__(self):
        self.type = 'dollar'

    def batting(self, hands, dealer):
        print("\n")
        for player in hands:
            while True:
                print(player.name, ", How much will you bat($)? : ", sep='', end='')
                bat = input()
                if not bat.isdigit():
                    continue
                elif int(bat) < self.amount:
                    print("minimum bat is", self.amount, "dollar.")
                elif int(bat) > player.chips:
                    print("Over bat Your total dollar. total $ =", player.chips)
                elif int(bat) > dealer.chips:
                    print("Over bat dealer chips. dealer total $ =", dealer.chips)
                else:
                    break
            player.chip_bat(bat)

    def player_win(self, winner, players, dealer):
        dealer.chips -= winner.bat
        winner.chips += winner.bat
        for player in players:
            player.chips -= player.bat
            dealer.chips += player.bat

    def dealer_win(self, players, dealer):
        for player in players:
            player.chips -= player.bat
            dealer.chips += player.bat

class Hand:
    """ A hand of playing cards. """

    def __init__(self):
        self.cards = []
        self.value = 0

    def __str__(self):
        reply = ""
        for card in self.cards:
            reply += str(card) + "\t\t"

        return reply

    def add(self, card):
        self.cards.append(card)
        self.value += (card.get_rank())

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def get_value(self):
        return self.value



class Deck(Hand):
    """ A deck of playing cards. """

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(BJ_Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:  # if len(self.cards) >  0
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")


class Player(Hand):
    """ A Player of playing cards. """

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.chips = 10
        self.bat = 0

    def chip_bat(self, bat):
        self.bat = int(bat)

class Dealer(Hand):
    """ A Dealer of playing cards. """

    def __init__(self):
        super().__init__()
        self.name = "dealer"
        self.chips = 100

    def add(self, card):
        self.cards.append(card)
        # If the rank of the dealer's card is 'A'
        # set to 11
        if card.get_rank() == 1:
            self.value += 11
        else:
            self.value += (card.get_rank())

    def hiding(self):
        self.cards[0].flip()


class BlackJackGame:
    def __init__(self):
        print("\t\t\tWelcome to the worlds simplest game!\n")
        self.player_num = None
        self.players = []
        self.stay_players = []
        self.lose_players = []

        self.init_players()

    def init_players(self):
        while True:
            self.player_num = input("How many players? <1 - 7>: ")
            if self.player_num.isdigit():
                self.player_num = int(self.player_num)
                if 0 < self.player_num < 8:
                    break

        for _ in range(self.player_num):
            name = input("Enter player name: ")
            self.players.append(Player(name))
            self.lose_players.append(Player(name))

    def outcome(self, player):
        if player.get_value() == 21:
            print(player.name, "wins.")
            return "win"

        elif player.get_value() > 21:
            print(player.name, "busts.")
            print(player.name, "loses.")
        else:
            self.stay_players.append(player)

    def question1(self):
        dealer = Dealer()

        hands = []
        for i in self.players:
            hands.append(i)
        hands.append(dealer)

        deck1 = Deck()
        deck1.populate()
        deck1.shuffle()

        deck1.deal(hands, per_hand=2)

        for i in self.players:
            print(i.name, " : ", i, sep='')

        dealer.hiding()
        print(dealer.name, ":", dealer)

    def question2(self):
        dealer = Dealer()

        hands = []
        for i in self.players:
            hands.append(i)
        hands.append(dealer)

        deck1 = Deck()
        deck1.populate()
        deck1.shuffle()

        deck1.deal(hands, per_hand=2)

        for i in self.players:
            print(i.name, " : ", i, "\t<", i.get_value(), ">", sep='')

        dealer.hiding()
        print(dealer.name, ":", dealer)

    def question3(self):
        dealer = Dealer()

        hands = []  # to add
        for player in self.players:
            hands.append(player)
        hands.append(dealer)

        deck1 = Deck()
        deck1.populate()
        deck1.shuffle()

        # deal the first card
        deck1.deal(hands, per_hand=2)
        print("\n", end='')
        for player in self.players:
            print(player.name, " : ", player, "\t<", player.get_value(), ">", sep='')

        dealer.hiding()
        print(dealer.name, ":", dealer)

        #  players turn
        for player in self.players:
            while player.get_value() < 21:
                while True:
                    print("\n", player.name, ", do you wand a hit? <Y/N>: ", sep='', end='')
                    answer = input()
                    answer = answer.upper()
                    if answer == 'Y' or answer == 'N':
                        break

                if answer == 'Y':
                    hands.clear()
                    hands.append(player)
                    deck1.deal(hands, per_hand=1)
                    print(player.name, " : ", player, "\t<", player.get_value(), ">", sep='')

                else:
                    break

            winner = self.outcome(player)
            if winner == 'win':
                exit()

        # dealer turn
        dealer.hiding()
        hands.clear()
        hands.append(dealer)
        print(dealer.name, " : ", dealer, "\t<", dealer.get_value(), ">", sep='')
        while dealer.get_value() < 17:
            deck1.deal(hands, per_hand=1)
            print(dealer.name, " : ", dealer, "\t<", dealer.get_value(), ">", sep='')

        winner = self.outcome(dealer)
        if winner == 'win':
            exit()

        tmp = 0
        name = ""
        for player in self.stay_players:
            if player.get_value() > tmp:
                tmp = player.get_value()
                name = player.name

        print(name, "wins.")

    def question4(self):
        dealer = Dealer()
        chip = Chip()

        hands = []  # to add
        for player in self.players:
            hands.append(player)

        chip.batting(hands, dealer)
        hands.append(dealer)

        deck1 = Deck()
        deck1.populate()
        deck1.shuffle()

        # deal the first card
        deck1.deal(hands, per_hand=2)
        print("\n", end='')
        for player in self.players:
            print(player.name, " : ", player, "\t<", player.get_value(), "> total $ = ", player.chips, ", bat($)=", player.bat, sep='')

        dealer.hiding()
        print(dealer.name, ":", dealer)

        #  players turn
        for player in self.players:
            while player.get_value() < 21:
                while True:
                    print("\n", player.name, ", do you wand a hit? <Y/N>: ", sep='', end='')
                    answer = input()
                    answer = answer.upper()
                    if answer == 'Y' or answer == 'N':
                        break

                if answer == 'Y':
                    hands.clear()
                    hands.append(player)
                    deck1.deal(hands, per_hand=1)
                    print(player.name, " : ", player, "\t<", player.get_value(), ">", sep='')

                else:
                    break

            winner = self.outcome(player)
            if winner == 'win':
                self.lose_players.remove(player)
                chip.player_win(player, self.lose_players, dealer)
                print(player.name, "total $ =", player.chips)
                exit()

        # dealer turn
        dealer.hiding()
        hands.clear()
        hands.append(dealer)
        print(dealer.name, " : ", dealer, "\t<", dealer.get_value(), ">", sep='')
        while dealer.get_value() < 17:
            deck1.deal(hands, per_hand=1)
            print(dealer.name, " : ", dealer, "\t<", dealer.get_value(), ">", sep='')

        winner = self.outcome(dealer)
        if winner == 'win':
            chip.dealer_win(self.lose_players, dealer)
            print(dealer.name, "total $ =", dealer.chips)
            exit()

        tmp = 0
        name = ""
        for player in self.stay_players:
            if player.get_value() > tmp:
                tmp = player.get_value()
                winner = player

        if winner.name == "dealer":
            chip.dealer_win(self.lose_players, dealer)
        else:
            chip.player_win(winner, self.lose_players, dealer)

        print(winner.name, "wins.")
        print(winner.name, "total $ =", winner.chips)


if __name__ == '__main__':
    number = input("Enter the Question number (1), (2), (3), (4) >> ")

    BJ_start = BlackJackGame()

    if number == '1':
        BJ_start.question1()
    elif number == '2':
        BJ_start.question2()
    elif number == '3':
        BJ_start.question3()
    elif number == '4':
        BJ_start.question4()
