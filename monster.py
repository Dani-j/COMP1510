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
  Return the index of monster HP in the monster information list.

  :precondition: none
  :postcondition: return the constant index where the moster HP is stored
    in the moster information list
  :return: an integer, the constant index of monster HP
  """
  return 1


def MONSTER_EXISTS():
  """
  Return if monster exists

  :precondition: none
  :postcondition: return the a constant integer showing if the monster exists or not
  :return: an integer, determine if a monster exists
  """
  return 1


def MAX_HEALTH():
  """
  Return the maximum health point of a monster.

  :precondition: None
  :postcondition: Return the maximum health point of a monster
  :return: An integer, the the maximum health point of a monster
  """
  return 5


def create_monster():
  """
  Create a monster with random name randomly

  :precondition: none
  :postcondition: return a random monster name or return nothing
  :return: monster name or none
  """
  if MONSTER_EXISTS() != random.randint(1, 25):  # If x != 1, a monster won't appear
    return None

  names = ("Dragon", "Zombie", "Python", "Werewolf", "Ghost", "Vampire")
  monster = [random.choice(names), MAX_HEALTH()]  # randomly generate a monster
  return monster


def hurt(monster_info, amount):
  """
  Decrease the monster HP and check if monster HP is smaller than 0 or not.

  :param monster_info: a list where stored the monster information
  :param amount: the amount of HP that is decreased by the character's attack
  :precondition: monster_info is a list containing the monster information,
    amount is a integer means the amount of HP that would be decreased
  :postcondition: return a booleen value showing the status of monster HP
  :return: Ture or False, showing if the moster HP is smaller than 0 or not

  >>> monster_info = ["python", 10]
  >>> amount = 2
  >>> hurt(monster_info, amount)
  True
  >>> monster_info = ["python", 1]
  >>> amount = 2
  >>> hurt(monster_info, amount)
  False
  """
  # return False if character is dead
  monster_info[HEALTH()] -= amount
  return monster_info[HEALTH()] <= 0


def main():
  """Test the module."""
  doctest.testmod()


if __name__ == '__main__':
  main()