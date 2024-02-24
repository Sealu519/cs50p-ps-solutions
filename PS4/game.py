# I’m thinking of a number between 1 and 100…
#
# What is it?
# It’s 50! But what if it were more random?
#
# In a file called game.py, implement a program that:
#
# Prompts the user for a level. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and , inclusive, using the random module. Prompts the user to guess that
# integer. If the guess is not a positive integer, the program should prompt the user again. If the guess is smaller
# than that integer, the program should output Too small! and prompt the user again. If the guess is larger than that
# integer, the program should output Too large! and prompt the user again. If the guess is the same as that integer,
# the program should output Just right! and exit.

import random


def main():
    level = get_level()
    guess(level)


def get_level():
    while True:
        try:
            n = input("Level: ").strip()
            if n.isnumeric() and int(n) > 0:
                return int(n)
            else:
                raise ValueError
        except ValueError:
            pass


def guess(level):
    answer = random.randint(1, level)
    while True:
        try:
            x = input("Guess: ").strip()
            if x.isnumeric() and int(x) > 0:
                if int(x) > answer:
                    print("Too large!")
                    pass
                elif int(x) < answer:
                    print("Too small!")
                    pass
                elif int(x) == answer:
                    print("Just right!")
                    break
            else:
                raise ValueError
        except ValueError:
            pass


main()
