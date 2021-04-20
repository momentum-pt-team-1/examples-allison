import random
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
    # TODO for suits, use tuples, e.g. (1, ♥️)
    deck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    return deck

def shuffle_cards(deck):
    '''Rearrange cards in random order and return deck'''
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    '''Deal the cards one at a time to each player until gone'''
    player1_hand = []
    player2_hand = []
    while len(deck) > 0:
    # until the deck is empty    
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())
    return (player1_hand, player2_hand)

def take_turn(player1_hand, player2_hand):
    '''players flip cards over, compare cards, player with larger card gets all cards
    If tie, flip another card and re-evaluate'''
    # both players flip one card on to table
    table = []
    round_over = False
    while not round_over:
        player1_card = player1_hand.pop()
        player2_card = player2_hand.pop()
        table.append(player1_card)
        table.append(player2_card)
        # if player1 card > player2 card: player 1 collects all cards
        if player1_card > player2_card:
            print("Player 1 takes the cards")
            player1_hand.append(table)
            round_over = True
        # elif player2 card > player1 card: player2  collects all cards
        elif player2_card > player1_card:
            print("Player 2 takes the cards")
            player2_hand.append(table)
            round_over = True
        else:
            print("Tie, flip cards again")
        
    

def play_game():
    '''Execute the game process from creating deck to one player winning'''
    # create a deck
    deck = make_deck()
    # print out that deck
    print(deck)
    # shuffle our deck
    shuffled_deck = shuffle_cards(deck)
    # show the shuffled deck
    print(shuffled_deck)
    # deal the cards
    player1_hand, player2_hand = deal_cards(deck)
    print("Player 1:", player1_hand)
    print("Player 2:", player2_hand)
    # repeat flip_and_compare until one player runs out of cards
    while len(player1_hand) > 0 and len(player2_hand) > 0:
        take_turn(player1_hand, player2_hand)

play_game()