"""
This file contains the functions related to battle operations and results.

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020
"""


import random
import user
import monster
import message


def FLEE_FAIL():
  """
  A constant integer that represents the charactor was attacked while fleeing.

  :precondition: None
  :postcondition: Always return 1
  :return: A integer that represents the charactor was attacked while fleeing
  """
  return 1

def ESCAPED():
  """
  A constant integer that represents the charactor has eacaped from a battle.

  :precondition: None
  :postcondition: Always return 99
  :return: A integer that represents the charactor has eacaped from a battle
  """
  return 99


def DRAW_GAME():
  """
  A constant integer that represents a draw game.

  :precondition: None
  :postcondition: Always return 0
  :return: A integer that represents a draw game
  """
  return 0


def CHARACTER_DIE():
  """
  A constant integer that represents the character has died.

  :precondition: None
  :postcondition: Always return 1
  :return: A integer that represents the character has died
  """
  return 1


def MONSTER_DIE():
  """
  A constant integer that represents a monster has died.

  :precondition: None
  :postcondition: Always return 2
  :return: A integer that represents a monster has died
  """
  return 2


def fight_ready():
  """
  Generate a random integer to prepare for the battle.

  :precondition: None
  :postcondition: Return a random integer
  :return: A random integer
  """
  return random.randint(1, 2)


def attack(character_choice, monster_choice, character_info, monster_info):
  """
  Hurt the one whose choice number is less and return the battle result.

  The battle result is represented by an integer in [0, 1, 2], 0 means a draw, 1 means the character
    died, 2 means the monster died

  :param character_choice: a positive integer in [1, 2], showing how stong the character's attack is
  :param monster_choice: a positive integer in [1, 2], showing how stong the monster's attack is
  :param character_info: a list containing character information
  :param monster_info: a list containing monster information
  :precondition: character_choice and monster_choice must a positive integer in [1, 2]; character_info must 
    be a list containing character information; monster_info must be a list containing character information
  :postcondition: return the battle result represented by an integer in [0, 1, 2]
  :return: an integer in [0, 1, 2], which is the battle result
  """
  if character_choice < monster_choice:  # compare numbers, the bigger the number, the stronger the attack
    message.character_hurted(monster_info, monster_choice)  #  tell the user the character was hurt by which monster, and by how much

    if user.hurt(character_info, monster_choice):  # True when the character died (i.e. character health <= 0)
      message.character_die(monster_info) 

      return CHARACTER_DIE()  # the battle result is that the character was died
  elif character_choice > monster_choice: 
    message.monster_hurted(monster_info, character_choice) 

    if monster.hurt(monster_info, character_choice):  # True when the monster is dead (i.e. monster health <= 0)
      message.monster_die(monster_info)
      
      return MONSTER_DIE()  # the battle result is that the monster died 
  else:  # when both attacks are equally strong (i.e. numbers are same)
    message.monster_hurted(monster_info, character_choice) 
    
    return DRAW_GAME()  # the battle result is a draw


def start(character_info, monster_info, action):
  """
  Exicute Kill or flee action, and return the battle or flee result.

  The return value, which is an integer, reprents the battle or flee result, integer 
    in [0, 1, 2] is result of battle, integer that is equals to 99 means the character
    fled

  :param character_info: a list containing character information
  :param monster_info: a list containing monster information
  :param action: a string that is equals to "kill" or anything else
  :precondition: the character_info must contains a list containing character information, 
    the monster_info must contains a list containing monster information, and action must be a string
  :postcondition: return a integer in [0, 1, 2, 99] representing the fighting result or flee result
  :return: a integer in [0, 1, 2, 99] representing the battle result or flee result
  """
  battle_result = DRAW_GAME()  # the initial battle result is 0
  if "kill" == action: 
    while character_info[user.HEALTH()] > 0 and monster_info[monster.HEALTH()] > 0:
      # keep fighting until one of character and monster died
      character_choice = fight_ready()  # random number showing how strong the character's attack is
      monster_choice = fight_ready() 
      battle_result = attack(character_choice, monster_choice, character_info, monster_info) 
      #return battle result after one round of fighting

    if 0 < character_info[user.HEALTH()]:  
      # update character health points when the character is still alive
      message.character_health(character_info)

    return battle_result
  else:  # when the user chose to flee
    if FLEE_FAIL() == random.randint(1, 1):  # the chance of got attacked when flee is 1/1
      hurt_amout = random.randint(1, 4)  # the amount of hurt by the monster is random in range [1, 4]
      user.hurt(character_info, hurt_amout) # decrease character health point
      message.character_hurted(monster_info, hurt_amout) # send the user who attacted the character, and how much
      
      if 0 < character_info[user.HEALTH()]: 
        # send the user the current health points if the user if still alive (i.e. health point > 0)
        message.character_health(character_info)
      
      return ESCAPED()  # return positive numbr that means the character fled