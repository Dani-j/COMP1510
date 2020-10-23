"""
This file contains the functions related to character information.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020D
"""


import user
import monster


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
  Tell the users that they input wrong direction.

  :param character_info: a list containing character information
  :precondition: the character_info must contains a list containing character information
  :postcondition: display a message telling the user typed a wrong direction
  :return: a string message
  """
  print("\033[1;31mSorry, %s. You cannot go that way.\033[0m" % user.get_character_name(character_info))
    

def character_hurted(monster_info, amount):
  """
  Tell the user that the character was hurt, how much and by whom.

  :param monster_info: a list containing monster information
  :param amount: a number showing how much the character was hurt
  :precondition: the monster_info must contains a list containing monster information,
    the number must be an positive integer that is bigger than 0
  :postcondition: Display a message telling the character was hurt, how much and by whom
  :return: a string message
  """
  print(f"\033[1;31mThe {monster_info[monster.MONSTER_NAME()]} bite you, and you lose {amount} HP\033[0m")


def monster_hurted(monster_info, amount):
  """
  Display the specific monster that is hurt by the character, and how much.

  :param monster_info: a list containing monster information
  :param amount:  number showing how much the monster was hurt
  :precondition: the monster_info must contains a list containing monster information,
    the number must be an positive integer that is bigger than 0
  :postcondition: Display a message telling which monster was hurt by the character and how much
  :return: a string message
  """
  print(f"\033[1;32mYou slashed the {monster_info[monster.MONSTER_NAME()]}, and it lose {amount} HP\033[0m")

 

def monster_appear(monster_info):
  """
  Telling the user which specific monster the character meet.

  :param monster_info: a list containing monster information
  :precondition: the monster_info must contains a list containing monster information
  :postcondition: Display a message telling which monster the character meet
  :return: a string message
  """
  print(f"\033[1;31mA {monster_info[monster.MONSTER_NAME()]} is looking at you maliciously\033[0m")
  
   


def character_die(monster_info):
  """
  Tell the user the character was killed

  :param monster_info: a list containing monster information
  :precondition: the monster_info must contains a list containing monster information
  :postcondition: print two messages showing the character is killed, and game is over
  :return: two string messages
  """
  print(f"\033[1;31mThe {monster_info[monster.MONSTER_NAME()]} killed you")
  print("GAME OVER\033[0m")
   


def monster_die(monster_info):
  """
  Tell the user the monster was killed

  :param monster_info: a list containing monster information
  :precondition: the monster_info must contains a list containing monster information
  :postcondition: print a message showing the monster is killed
  :return: a string message 
  """
  print(f"\033[1;32mThe {monster_info[monster.MONSTER_NAME()]} has been killed\033[0m")



def character_health(character_info):
  return
