"""
This file contains the functions related to battle operations and results.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020
"""


import random
import user
import monster
import message
import doctest


def FLEE_FAIL():
    """

    :precondition:
    :postcondition:
    :return:
    """
    return 1

def ESCAPED():
    """

    :precondition:
    :postcondition:
    :return:
    """
    return 99


def DRAW_GAME():
    """

    :precondition:
    :postcondition:
    :return:
    """
    return 0


def CHARACTER_DIE():
    """

    :precondition:
    :postcondition:
    :return:
    """
    return 1


def MONSTER_DIE():
    """

    :precondition:
    :postcondition:
    :return:
    """
    return 2


def fight_ready():
    """

    :precondition:
    :postcondition:
    :return:
    """
    # 猜拳扣血
    return random.randint(1, 2)


def main():
    """Drive the program."""
    doctest.testmod()


if __name__ == '__main__':
    main()

