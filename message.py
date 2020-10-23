"""
This file contains the functions related to character information.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020D
"""


import user
import monster


"""
Python font colored string：
"\033[1;{font_color}m{message_string}\033[0m"

-------------------------------------------
font_color | Color Description
-------------------------------------------
30         |      Black
31         |      Red
32         |      Green
33         |      Yellow
34         |      Blue
35         |      Magenta
36         |      Cyan
37         |      Grey
-------------------------------------------

From: https://www.cnblogs.com/daofaziran/p/9015284.html
"""


def opening():
  """
  Display opening message.

  :precondition: none
  :postcondition: dispaly an opening string message
  :return: none
  """
  print("\033[1;35mOnce upon a time, there is a Kingdom of far far away.")
  print("One day, the princess of the kingdom was taken away by the devil.")
  print("The king looked for warriors to rescue the princess.")
  print("As a true warrior, you decide to go to rescue the princess immediately.\033[0m")
  print("")


def welcome(character_info):
  """
  Display welcome message.

  :param character_info: a list containing character information
  :precondition: the character_info must contain a list containing character information
  :postcondition: return four welcome string messages in special color, the first
    message containing character name
  :return: four welcome messages
  """
  print("\033[1;35mWelcome to the Kingdom of Far Far Away, %s." % user.get_character_name(character_info))
  print("You're now standing in the center of a dark forest.")  
  print("Type 'up', 'down', 'left' or 'right' and press 'Enter' to move.")
  print("If you are scared, type 'Quit' and press 'Enter'.")
  print("Watch out for your footsteps, it may attract unknown monsters.\033[0m")
  print("")
  print("However, you hear nothing except your own heartbeat.")


def wrong_direction(character_info):
  """
  Tell the user that they input wrong direction.

  :param character_info: a list containing character information
  :precondition: the character_info must contain a list containing character information
  :postcondition: display a string message telling the user typed a wrong direction
  :return: a string message
  """
  print("\033[1;31mSorry, %s. You cannot go that way.\033[0m" % user.get_character_name(character_info))


def character_hurted(monster_info, amount):
  """
  Tell the user that the character was hurt, by how much and by whom.

  :param monster_info: a list containing monster information
  :param amount: a number showing how much the character was hurt
  :precondition: the monster_info must contain a list containing monster information,
    the number must be an positive integer that is bigger than 0
  :postcondition: display a string message telling the user the character was hurt, by how much and by whom
  :return: a string message
  """
  print(f"\033[1;31mThe {monster_info[monster.MONSTER_NAME()]} bite you, and you lose {amount} HP\033[0m")


def monster_hurted(monster_info, amount):
  """
  Display the specific monster that is hurt by the character, and by how much.

  :param monster_info: a list containing monster information
  :param amount: a number showing how much the monster was hurt
  :precondition: the monster_info must contain a list containing monster information,
    the number must be an positive integer that is bigger than 0
  :postcondition: Display a string message telling the user which monster was hurt by the character and by how much
  :return: a string message
  """
  print(f"\033[1;32mYou slashed the {monster_info[monster.MONSTER_NAME()]}, and it lose {amount} HP\033[0m")


def monster_appear(monster_info):
  """
  Telling the user which specific monster the character meet.

  :param monster_info: a list containing monster information
  :precondition: the monster_info must contain a list containing monster information
  :postcondition: Display a string message telling the user which monster the character meet
  :return: a string message
  """
  print(f"\033[1;31mA {monster_info[monster.MONSTER_NAME()]} is looking at you maliciously\033[0m")



def character_die(monster_info):
  """
  Tell the user the character was killed

  :param monster_info: a list containing monster information
  :precondition: the monster_info must contain a list containing monster information
  :postcondition: print two string messages showing the character was killed, and game is over
  :return: two string messages
  """
  print(f"\033[1;31mThe {monster_info[monster.MONSTER_NAME()]} killed you")
  print("GAME OVER\033[0m")



def monster_die(monster_info):
  """
  Tell the user the monster was killed

  :param monster_info: a list containing monster information
  :precondition: the monster_info must contain a list containing monster information
  :postcondition: print a string message showing the monster was killed
  :return: a string message
  """
  print(f"\033[1;32mThe {monster_info[monster.MONSTER_NAME()]} has been killed\033[0m")



def character_health(character_info):
  """
  Display the character HP

  :param character_info: a list containing character information
  :precondition: the character_info must contains a list containing character information
  :postcondition: print a string message showing the character HP
  :return: a string message
  """
  print("\033[1;32mYour HP is {0} now\033[0m".format(character_info[user.HEALTH()]))