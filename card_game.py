# Build a card game based on War

# What I already know
# Deck with 2 suits and 10 cards
# Objective is to get the most cards
# Turn: each player (A & B) flips a card
# If A's card is larger, A gets all cards
# If B's card is larger, B gets all cards
# If it's a tie, flip over two new cards?
# Game ends when one player runs out of cards and the other wins

def make_deck():
    '''Create & return a deck of cards, 2 suits, 10 cards each'''
    # for suits, use tuples, e.g. (1, ♥️)
    deck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    return deck

def shuffle_cards():
    '''Rearrange cards in random order and return deck'''
    pass

def deal_cards():
    '''Deal the cards one at a time to each player until gone'''
    pass

def take_turn():
    '''players flip cards over, compare cards, player with larger card gets all cards
    If tie, flip another card and re-evaluate'''
    pass

def play_game():
    '''Execute the game process from creating deck to one player winning'''
    deck = make_deck()
    print(deck)

play_game()