"""
(Description:)

Authors: James (Hang) Liu, Dani (Danfeng) Jin
Date: October 23, 2020D
"""


import user
import message
import map
import monster
import battle


def game_process(game_character, game_map):
  # Get the direction from yser input
  direction = user.get_character_choice("\033[1;34mEnter a direction to go:\033[0m")

  if not direction:
    # If it's not a valid direction, return
    return False
  
  if user.move(game_character, direction, game_map):
    # Print the map and the current position of the character
    map.print_map(game_character[user.POSITION()])

    # Try to create a monster
    game_monster = monster.create_monster()
    if not game_monster:
      # Display a hint and return if it failed to create a monster
      user.heal(game_character)
      message.character_health(game_character)
      return False
    else:
      # Display a hint if a monster has been created
      message.monster_appear(game_monster)

      # Wait for user choice (kill or flee away)
      action = user.get_character_choice(
        "\033[1;34mType Kill to attack, type anything else to flee:\033[0m")
      
      if not action or battle.CHARACTER_DIE() == battle.start(game_character, game_monster, action):
        # If user type quit of the character has died, return True to end the loop
        return True
  else:
    # If user cannot go to the direction, show a hint and return
    message.wrong_direction(game_character)
    return False


def run(game_logic):
  """
  Create the map and the character and then start game

  :precondition: None
  :postcondition: Exit if goal has been achieved
  :return: None
  """
  # Display the opening message
  message.opening()

  # Create the game map
  game_map = map.create_map()

  # Create the character
  game_character = user.create_character()
  if not game_character:
    return

  # Start the game loop
  goal_achieved = False;
  while not goal_achieved:
    goal_achieved = game_logic(game_character, game_map)



def main():
  """Test the module"""
  run()


if __name__ == '__main__':
  main()