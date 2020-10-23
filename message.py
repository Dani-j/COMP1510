"""
This file contains the functions related to character information.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020D
"""


import user
import monster
import doctest


def welcome(character_info):
    """
    Display welcome message.

    :param character_info: a list containing character information
    :precondition: the character_info must contains a list containing character information
    :postcondition: return four welcome meessages in special color, the first
      message containing character name
    :return: four welcome messages
    """
    print("\033[1;34mWelcome to SUD, %s." % user.get_character_name(character_info))
    print("You're now standing in the center of a dark forest.")
    print("Type 'up', 'down', 'left' or 'right' and press 'Enter' to move.")
    print("If you want to exit, type 'Quit' and press 'Enter'.\033[0m")


def wrong_direction(character_info):
    """

    :param character_info: a list containing character information
    :precondition: the character_info must contains a list containing character information
    :postcondition: display a message telling the user typed a wrong direction
    :return: a string message
    """
    print("\033[1;31mSorry, %s. You cannot go that way.\033[0m" % user.get_character_name(character_info))
    

def character_hurted(monster_info, amount):
   


def monster_hurted(monster_info, amount):
 

def monster_appear(monster_info):
   


def character_die(monster_info):
   


def monster_die(monster_info):
 


def character_health(character_info):
    


def main():
    """Drive the program."""
    doctest.testmod()


if __name__ == '__main__':
    main()
