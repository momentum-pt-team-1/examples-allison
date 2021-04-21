import random
# player1, player2

# serve
# 1st serve -> if out, second serve
# 2nd serve -> if out, receiver gets the point


def serve(player):
    outcomes = ["in", "in", "in", "in", "in", "in", "in", "out", "out", "out"]
    outcome = random.choice(outcomes)
    print(f"{player}'s serve is {outcome}")
    return outcome

def serve_until_out(player):
    '''player keeps serving until ball goes out'''
    serve_outcome = None
    while serve_outcome != "out":
        serve_outcome = serve(player)

def game(player1, player2):
    serve_until_out(player1)
    serve_until_out(player2)
    
game("Venus", "Serena")
    

