ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suits = ["♣️", "♦️", "♥️", "♠️"]


class Deck:
    def __init__(self, ranks, suits):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                print(card)
                self.cards.append(card)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Player:
    # dealer will be a type of player
    pass


deck = Deck(ranks, suits)
breakpoint()