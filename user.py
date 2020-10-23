"""
This file contains the functions related to character information.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020
"""


import random
import map
import message
import doctest


def CHARACTERNAME():
    """
    Return the index of character name element in a character information list.

    :precondition: None
    :postcondition: Return the index where the character name is stored in the character_info list
    :return: An integer, the index of the character name in a character information list
    """
    return 0


def HEALTH():
    """
    Return the index of health point element in a character information list.

    :precondition: None
    :postcondition: Return the index where the health point is stored in the character_info list
    :return: An integer, the index of the health point in a character information list
    """
    return 1


def POSITION():
    """
    Return the index of the position element in a character information list.

    :precondition: None
    :postcondition: Return the index where the position element is stored in the character_info list
    :return: An integer, the index of the position in a character information list
    """
    return 2


def MAX_HEALTH():
    """
    Return the maximum health point of a character.

    :precondition: None
    :postcondition: Return the maximum health point of a character
    :return: An integer, the the maximum health point of a character
    """
    return 10


def get_character_name(character_info):
    """
    Get the character name from a character information list.

    :param character_info: A list that contains a character information
    :precondition: The character_info must contains a list contains character information
    :postcondition: Return the correct character name
    :return: A string, represents the character name

    >>> character_info = ["James", 10, [1, 2]]
    >>> get_character_name(character_info)
    'James'
    """
    return character_info[CHARACTERNAME()]


def get_character_position(character_info):
    """
    Return the character coordination

    :param character_info: A list that contains a character information
    :precondition: The character_info must contains a list contains character information
    :postcondition: Return the correct character coordination
    :return: A list contains the character coordination

    >>> character_info = ["DJ", 10, [1, 2]]
    >>> get_character_position(character_info)
    [1, 2]
    """
    return character_info[POSITION()]


def create_character():
    """
    Prompt the user to create the character profile which contains name, health point and position

    :precondition: None
    :postcondition: Return a list contains character information
    :return: A list contains character information
    """
    character_info = []
    character_name = input("\033[1;34mPlease input your character name:\033[0m").strip()
    if not character_name:  # when the character only enter space(s)
        print("please enter at list one character.")
        create_character()
    character_info.insert(CHARACTERNAME(), character_name)  # put character name in the character_info list
    character_info.insert(HEALTH(), 10)  # put character HP in the character_info list, whose initial value is 10
    character_info.insert(POSITION(), [2, 2])  # put character position in the list, the initial position is [2, 2]

    message.welcome(character_info)  # display welcome messages

    return character_info


def heal(character_info):
    """
    Increase 2 helath point for the character until character health is 10.

    :param character_info: A list that contains character information
    :precondition: The character_info must contains correct character information
    :postcondition: Update the character health point correctly
    :return: None
    """
    # Add 2 health point first
    character_info[HEALTH()] += 2

    if character_info[HEALTH()] > MAX_HEALTH():
        # The character health point cannot be greater than 10
        character_info[HEALTH()] = MAX_HEALTH()


def hurt(character_info, amount):
    """
    Decrease the character health point and check if the character is dead.

    :param character_info: A list that contains character information
    :param amount: The amount of health should be decreased
    :precondition: The character_info must contains correct character information, 
      the amount must be a positive integer
    :postcondition: Change character health point and return the charactor status
    :return: True or False

    >>> character_info = ["James", 5, [1, 2]]
    >>> hurt(character_info, 2)
    False
    >>> character_info = ["James", 5, [1, 2]]
    >>> hurt(character_info, 10)
    True
    """
    # Decrase specific amount of health point
    character_info[HEALTH()] -= amount

    # Return False if character is dead
    return character_info[HEALTH()] <= 0


def move(character_info, direction, game_map):
  return


def get_character_choice(tip):
  return


def main():
    """Drive the program."""
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()