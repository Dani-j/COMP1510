"""
This file contains the functions related to the map.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020
"""

import doctest


def LONGITUDE():
  """
  Return the index of longitude element in a position list.

  :precondition: None
  :postcondition: Return the constant index of longitude
  :return: An integer, the constant index of longitude
  """
  return 0


def LATITUDE():
  """
  Return the index of latituede element in a position list.

  :precondition: None
  :postcondition: Return the constant index of latituede
  :return: An integer, the constant index of latituede
  """
  return 1


def create_map():
  """
  Create a map consists of a position list matrix.

  :precondition: None
  :postcondition: Generate a map list that is a 5 x 5 grid
  :return: A list that contain position information

  >>> create_map()
  [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4]]
  """
  # Define the map matrix variable
  map = []
  # Use a nested loop to fill the map matrix
  for latitude in range(0, 5):
    for longitude in range(0, 5):
      position = [longitude, latitude]
      map.append(position)
  return map


def valid_move(map, position):
  """
  Check if the movement is valid.

  :param map: A list that contain position information
  :param position: A list that containing latitude and longitude
  :precondition: The parameter map is a list representing a map matrix,
    the parameter position is a list containing the next position of the character
  :postcondition: Check if the next position is inside of the map and return the result
  :return: A boolean values showing if the next move is possible

  >>> map = [[1,2], [2,3]]
  >>> position = [1,2]
  >>> valid_move(map, position)
  True
  >>> position = [5,6]
  >>> valid_move(map, position)
  False
  """
  return position in map


def print_map(position):
  """
  Display the map and the current position of the character.

  :param position: A list containing 2 elements -- [latitude, longitude]
  :precondition: position must be a list containing 2 elements
  :postcondition: None
  :return: None
  """
  for latitude in range(0, 5):
    for longitude in range(0, 5):
      if position == [longitude, latitude]:
        print("\033[1;35mo \033[0m", end="")  # display the character??
      else:
          print("* ", end="")
    print("")


def main():
  """Test the module"""
  doctest.testmod(verbose=True)


if __name__ == '__main__':
  main()
