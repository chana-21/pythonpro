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


class Unprintable_Card(Card):
    def __str__(self):
        return "<unprintable>"


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


if __name__ == '__main__':
    card1 = Card("A", "c")
    card2 = Unprintable_Card("A", "d")
    card3 = Positionable_Card("A", "h")

    print(card1)  # Ac
    print(card2)  # <unprintable>
    print(card3)  # Ah
    card3.flip()
    print(card3)  # XX
