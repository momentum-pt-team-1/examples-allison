import random

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suits = ["🔥", "💧", "🌪", "🌈"]


class Deck:
    def __init__(self, ranks, suits):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Player:
    # dealer will be a type of player
    def __init__(self, name, is_dealer):
        self.name = name
        self.is_dealer = is_dealer
        self.hand = []

    def __str__(self):
        if self.is_dealer == True:
            return 'Dealer'
        else:
            return f"{self.name}"


class Game:
    def __init__(self, player_name, dealer_name):
        self.deck = Deck(ranks, suits)
        self.deck.shuffle()
        self.player = Player(player_name, False)
        self.dealer = Player(dealer_name, True)
        self.player.hand.append(self.deck.cards.pop())
        self.dealer.hand.append(self.deck.cards.pop())
        self.player.hand.append(self.deck.cards.pop())
        self.dealer.hand.append(self.deck.cards.pop())

game = Game("Rusty Ryan", "Tracy")

print(game.player)
for card in game.player.hand:
    print(card)
print(game.dealer)
for card in game.dealer.hand:
    print(card)
