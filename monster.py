"""
This file contains the functions related to monster information.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020
"""


import random
import doctest


def MONSTER_NAME():
  """
  Return the index of monster name in the monster information list.

  :precondition: none
  :postcondition: return 0, the constant index where the moster name is stored
    in the moster information list
  :return: an integer, the constant index of monster name
  """
  return 0


def HEALTH():
  """
  Return the index of monster health points in the monster information list.

  :precondition: none
  :postcondition: return 1, the constant index where the monster health points 
    is stored in the monster information list
  :return: an integer, the constant index of monster health points
  """
  return 1


def MONSTER_EXISTS():
  """
  Return 1 when monster exists.

  :precondition: none
  :postcondition: return 1, a constant integer showing if the monster exists
  :return: an integer, determine a monster exists
  """
  return 1


def MAX_HEALTH():
  """
  Return the maximum health points of a monster.

  :precondition: none
  :postcondition: return 5, the maximum health points of a monster
  :return: an integer, the maximum health points of a monster
  """
  return 5


def create_monster():
  """
  Create a monster with random name randomly.

  :precondition: none
  :postcondition: return a random monster name or return none
  :return: monster name or none
  """
  if MONSTER_EXISTS() != random.randint(1, 25): 
    # If x != 1, a monster won't appear
    return None

  names = ("Dragon", "Zombie", "Python", "Werewolf", "Ghost", "Vampire")
  monster = [random.choice(names), MAX_HEALTH()]  
  # randomly generate a monster, and assign the maximun health to the monster
  return monster


def hurt(monster_info, amount):
  """
  Decrease the monster health points and check if monster health points is smaller than 0.

  :param monster_info: a list storing the monster information
  :param amount: the amount of health points that is decreased by the character's attack
  :precondition: monster_info is a list containing the monster information, amount is 
    an integer meaning the amount of health points that should be decreased
  :postcondition: return a booleen value showing the status of monster health points
  :return: Ture or False, showing if the moster health points <= 0

  >>> monster_info = ["python", 10]
  >>> amount = 2
  >>> hurt(monster_info, amount)
  True
  >>> monster_info = ["python", 1]
  >>> amount = 2
  >>> hurt(monster_info, amount)
  False
  """
  # return False if monster is dead
  monster_info[HEALTH()] -= amount
  return monster_info[HEALTH()] <= 0


def main():
  """Test the module."""
  doctest.testmod()


if __name__ == '__main__':
  main()