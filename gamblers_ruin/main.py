# https://www.stat.auckland.ac.nz/~fewster/325/notes/ch1.pdf

from random import *

starting_cash = 30  # our starting cash
goal_cash = 100  # we stop when we get this amount of money
lost_state = 0  # we stop when we have no money
cash_per_round = 5  # win or lose by this amount
iteration = 100  # how many times do we want to play


def gamblers_ruin():
    current_cash = starting_cash

    while current_cash <= goal_cash or current_cash >= lost_state:
        # print(f'current_cash = {current_cash}')
        if flip_a_coin():
            current_cash += cash_per_round
        if not flip_a_coin():
            current_cash -= cash_per_round

        if current_cash <= lost_state:
            print('You Lost M8')
            return 'lost'
        if current_cash >= goal_cash:
            print(f'Congrats you got {current_cash}')
            return 'won'


def flip_a_coin():
    r = random()
    if r > 0.5:
        return True
    elif r < 0.5:
        return False
    else:
        # if for some reason we get 0.5? 0 or 1
        # try again
        flip_a_coin()


def summary(lst: list):
    return {i: lst.count(i) for i in lst}


def run(iteration):
    actual_winning = list()
    for _ in range(iteration):
        did_you_win = gamblers_ruin()
        actual_winning.append(did_you_win)

    print(summary(actual_winning))


if __name__ == '__main__':
    run(iteration=iteration)
