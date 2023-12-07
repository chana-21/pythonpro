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


class Dealer(Hand):
    """ A Dealer of playing cards. """

    def __init__(self):
        super().__init__()
        self.name = "dealer"

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
        print("Welcome to the worlds simplest game!")
        self.player_num = None
        self.players = []
        self.stay_players = []

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

    def outcome(self, player):
        if player.get_value() == 21:
            print(player.name, "wins.")
            exit()

        elif player.get_value() > 21:
            print(player.name, "busts.")
            print(player.name, "loses.")
        else:
            self.stay_players.append(player)

    def start_game(self):
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

            self.outcome(player)

        # dealer turn
        dealer.hiding()
        hands.clear()
        hands.append(dealer)
        print(dealer.name, " : ", dealer, "\t<", dealer.get_value(), ">", sep='')
        while dealer.get_value() < 17:
            deck1.deal(hands, per_hand=1)
            print(dealer.name, " : ", dealer, "\t<", dealer.get_value(), ">", sep='')

        self.outcome(dealer)

        tmp = 0
        name = ""
        for player in self.stay_players:
            if player.get_value() > tmp:
                tmp = player.get_value()
                name = player.name

        print(name, "wins")


if __name__ == '__main__':
    BJ_start = BlackJackGame()
    BJ_start.start_game()
