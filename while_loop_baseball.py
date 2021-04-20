import random


def at_bat(outs):
    # check the outcome of the is_out function
    print("At bat")
    if is_out() == True:
        outs += 1
    print(outs, " outs")
    return outs
    

def is_out():
    '''This function randomly determines whether the batter is out or makes it on base'''
    options = ["on_base", "out"]
    outcome = random.choice(options)
    if outcome == "on_base":
        print("Batter made it on base.")
        return False
    else:
        print("Batter is out")
        return True

def play_inning(team1, team2):
    # need each team to bat
    for team in [team1, team2]:
        print(team, " is currently batting")
        outs = 0 
        while outs < 3:
            outs = at_bat(outs)

def game(team1, team2):
    # 9 innings 
    # each team bats each inning
    for inning in range(1, 10):
        print("inning", inning)
        play_inning(team1, team2)
    
    print("Game Over")

game("Bulls", "Mudcats")


