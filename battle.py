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
  A constant integer that represents the charactor was attacked while fleeing

  :precondition: None
  :postcondition: Always return 1
  :return: A integer that represents the charactor was attacked while fleeing
  """
  return 1

def ESCAPED():
  """
  A constant integer that represents the charactor has eacaped from a battle

  :precondition: None
  :postcondition: Always return 99
  :return: A integer that represents the charactor has eacaped from a battle
  """
  return 99


def DRAW_GAME():
  """
  A constant integer that represents a draw game

  :precondition: None
  :postcondition: Always return 0
  :return: A integer that represents a draw game
  """
  return 0


def CHARACTER_DIE():
  """
  A constant integer that represents the character has died

  :precondition: None
  :postcondition: Always return 1
  :return: A integer that represents the character has died
  """
  return 1


def MONSTER_DIE():
  """
  A constant integer that represents a monster has died

  :precondition: None
  :postcondition: Always return 1
  :return: A integer that represents a monster has died
  """
  return 2


def fight_ready():
  """
  Generate a random integer to prepare for the battle

  :precondition: None
  :postcondition: Return a random integer
  :return: A random integer
  """
  return random.randint(1, 2)





def start(character_info, monster_info, action):
  """
  

  :param character_info: a list containing character information
  :param monster_info: a list containing monster information
  :param action: a string that is equals to "kill" or anything else
  :precondition: character_info
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
  """Test the module"""
  doctest.testmod()


if __name__ == '__main__':
  main()

