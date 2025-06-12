import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [ HEADS, TAILS]

def flip_coin():
    return random.choice(COIN_VALUES)

print(flip_coin())

def play_martingale(*, starting_funds: int, min_bet:int, max_bet: int)-> int:
    step_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        print("======")
        step_to_loose +=1
        current_funds -= current_bet
        print(f"{current_funds=}, {current_bet=}")
        flipped_coin_value = flip_coin()
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            print(f"{win=}")
            current_funds +=win
            current_bet = min_bet
        else:
            print("loose")
            current_bet *=2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds        
    
    return step_to_loose                
print(play_martingale(starting_funds=100, min_bet=1, max_bet=100))

#heads
#======
#current_funds=99, current_bet=1
#win=2
#======
#current_funds=100, current_bet=1
#loose
#======
#current_funds=98, current_bet=2
#loose
#======
#current_funds=94, current_bet=4
#loose
#======
#current_funds=86, current_bet=8
#loose
#======
#current_funds=70, current_bet=16
#loose
#======
#current_funds=38, current_bet=32
#loose
#======
#current_funds=0, current_bet=38
#loose
#8

def simulate_martingale_for_n_players(*, starting_funds: int, min_bet:int, max_bet:int, n_games:int)-> float:
    total_steps_to_loose = 0 
    for i in range(n_games):
        step_to_loose = play_martingale(starting_funds=starting_funds, min_bet=min_bet, max_bet=max_bet)
        total_steps_to_loose += step_to_loose
        return total_steps_to_loose / n_games
    
    print(simulate_martingale_for_n_players(
        n_games=10,
        starting_funds=1000,
        min_bet=1,
        max_bet=100
    ))

    #106770