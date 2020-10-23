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

