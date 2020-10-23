"""
This file contains the functions related to character information.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020
"""


import map
import message
import doctest


def CHARACTERNAME():
  """
  Return the index of character name element in a character information list.

  :precondition: None
  :postcondition: Return the index where the character name is stored in the character_info list
  :return: An integer, the index of the character name in the character information list
  """
  return 0


def HEALTH():
  """
  Return the index of health points in the character information list.

  :precondition: none
  :postcondition: return 1, the index where the health points is stored in the character_info list
  :return: an integer, the index of the health points in a character information list
  """
  return 1


def POSITION():
  """
  Return the index of the position element in a character information list.

  :precondition: none
  :postcondition: return the index where the position element is stored in the character_info list
  :return: an integer, the index of the position in a character information list
  """
  return 2


def MAX_HEALTH():
  """
  Return the maximum health points of a character.

  :precondition: none
  :postcondition: return the maximum health points of a character
  :return: an integer, the the maximum health points of a character
  """
  return 10


def get_character_name(character_info):
  """
  Get the character name from a character information list.

  :param character_info: a list that contains character information
  :precondition: the character_info must contain a list of character information
  :postcondition: return the correct character name
  :return: a string, represents the character name

  >>> character_info = ["James", 10, [1, 2]]
  >>> get_character_name(character_info)
  'James'
  """
  return character_info[CHARACTERNAME()]


def get_character_position(character_info):
  """
  Return the character coordinates.

  :param character_info: a list that contains character information
  :precondition: the character_info must contain a list of character information
  :postcondition: return the correct character coordinates
  :return: a list contains the character coordinates

  >>> character_info = ["DJ", 10, [1, 2]]
  >>> get_character_position(character_info)
  [1, 2]
  """
  return character_info[POSITION()]


def create_character():
  """
  Prompt the user to create the character profile which contains name, health point and position.

  :precondition: none
  :postcondition: return a list containing character information
  :return: a list containing character information
  """
  character_info = []
  character_name = input("\033[1;34mNow, tell me what's your name:\033[0m").strip()
  if "quit" == character_name:
    return None
  # put character name in the character_info list
  character_info.insert(CHARACTERNAME(), character_name)  
  # put character healh points in the character_info list, whose initial value is 10
  character_info.insert(HEALTH(), 10)  
  # put character position in the list, the initial position is [2, 2]
  character_info.insert(POSITION(), [2, 2])  
  
  message.welcome(character_info)  # display welcome messages
  map.print_map(character_info[POSITION()])  # display the map

  return character_info


def heal(character_info):
  """
  Increase 2 helath points for the character (maximum defined by MAX_HEALTH).

  :param character_info: a list that contains character information
  :precondition: the character_info must contain correct character information
  :postcondition: update the character health points correctly
  :return: none

  >>> character_info = ["James", 7, [1, 2]]
  >>> heal(character_info)
  >>> character_info[HEALTH()]
  9
  >>> heal(character_info)
  >>> character_info[HEALTH()]
  10
  >>> heal(character_info)
  >>> character_info[HEALTH()]
  10
  """
  # Add 2 health point first
  character_info[HEALTH()] += 2

  if character_info[HEALTH()] > MAX_HEALTH():
    # The character health points cannot be greater than MAX_HEALTH()
    character_info[HEALTH()] = MAX_HEALTH()


def hurt(character_info, amount):
  """
  Decrease the character health point and check if the character is dead.

  :param character_info: a list that contains character information
  :param amount: the amount of health should be decreased
  :precondition: the character_info must contain correct character information,
    the amount must be a positive integer
  :postcondition: change character health point and return the charactor status
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
  """
  Try to change the character's position and check if the direction is right.

  :param character_info: a list that contains character information
  :param direction: a string represent the direction chosen by the user
  :param game_map: a map list that has 25 positions, which are lists
  :precondition: the character_info must contains correct character information;
    The direction must be "left", "right", "up" or down;
    The game_map must be a list that is a 5 x 5 matrix
  :postcondition: change character position if possible and return the result
  :return: A boolean values shows if the direction is valid

  >>> character_info = ["James", 5, [0, 0]]
  >>> game_map = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
  >>> move(character_info, "right", game_map)
  True
  >>> move(character_info, "up", game_map)
  False
  """
  # Get the previous position from the character_info
  position = get_character_position(character_info)[:]

  # Move
  if "left" == direction:
    position[map.LONGITUDE()] -= 1
  elif "right" == direction:
    position[map.LONGITUDE()] += 1
  elif "up" == direction:
    position[map.LATITUDE()] -= 1
  elif "down" == direction:
    position[map.LATITUDE()] += 1
  else:
    return False

  # If the new position is valid, update the character_info and return
  if map.valid_move(game_map, tuple(position)):
    character_info[POSITION()] = position
    return True

  # Return false if the new position is not valid
  return False


def get_character_choice(tip):
  """
  Get the command of the user from stdio

  :param tip: A string, the message to be shown to prompt the the user to input
  :precondition: The parameter tip must be a string
  :postcondition: Return the user command if the command is not "quit"
  :return: None if the user typed "quit", or else return what the user typed
  """
  command = input(tip).strip().lower()
  if "quit" == command:
    return None
  else:
    return command


def main():
  """Test the module"""
  doctest.testmod(verbose=True)


if __name__ == '__main__':
  main()
