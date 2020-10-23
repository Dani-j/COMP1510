"""
(Description:)

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


def attack(character_choice, monster_choice, character_info, monster_info):
    """


    :param character_choice:
    :param monster_choice:
    :param character_info:
    :param monster_info:
    :precondition:
    :postcondition:
    :return:
    """
    if character_choice < monster_choice:
        message.character_hurted(monster_info, monster_choice)
        if user.hurt(character_info, monster_choice):
            message.character_die(monster_info)
            return CHARACTER_DIE()
    elif character_choice > monster_choice:
        message.monster_hurted(monster_info, character_choice)
        if monster.hurt(monster_info, character_choice):
            message.monster_die(monster_info)
            return MONSTER_DIE()
    else:
        message.monster_hurted(monster_info, character_choice)
        return DRAW_GAME()


def start(character_info, monster_info, action):
    """


    :param character_info:
    :param monster_info:
    :param action:
    :precondition:
    :postcondition:
    :return:
    """
    battle_result = DRAW_GAME()
    if "kill" == action:
        while character_info[user.HEALTH()] > 0 and monster_info[monster.HEALTH()] > 0:
            character_choice = fight_ready()
            monster_choice = fight_ready()
            battle_result = attack(character_choice, monster_choice, character_info, monster_info)
        if 0 < character_info[user.HEALTH()]:
            message.character_health(character_info)
        return battle_result
    else:
        if FLEE_FAIL() == random.randint(1, 1):
            hurt_amout = random.randint(1, 4)
            user.hurt(character_info, hurt_amout)
            message.character_hurted(monster_info, hurt_amout)
            if 0 < character_info[user.HEALTH()]:
                message.character_health(character_info)
            return ESCAPED()


def main():
    """Drive the program."""
    doctest.testmod()


if __name__ == '__main__':
    main()

