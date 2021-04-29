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

    def calculate_hand_value(self):
        # TODO handle A having two potential values
        total_value = 0
        for card in self.hand:
            if card.rank in ["J", "Q", "K"]:
                total_value += 10
            elif card.rank == "A":
                total_value += 11
            else:
                total_value += card.rank
        if total_value > 21:
            if "A" in self.hand:
                total_value -= 10
        return total_value



class Game:
    def __init__(self, player_name, dealer_name):
        self.deck = Deck(ranks, suits)
        self.deck.shuffle()
        self.player = Player(player_name, False)
        self.dealer = Player(dealer_name, True)
        for i in range(2):
            self.deal_one_card(self.player)
            self.deal_one_card(self.dealer)

    def deal_one_card(self, person):
        person.hand.append(self.deck.cards.pop())

    def ask_hit_or_stay(player):
        '''Determine whether player wants to hit or stay'''
        # if player.is_dealer == True:
        pass
            
       # return hit or stay
     

game = Game("Rusty Ryan", "Tracy")

print(game.player)
for card in game.player.hand:
    print(card)
print(f'The total value of this hand is {game.player.calculate_hand_value()}')
print(game.dealer)
for card in game.dealer.hand:
    print(card)

print(f'The total value of this hand is {game.dealer.calculate_hand_value()}')
