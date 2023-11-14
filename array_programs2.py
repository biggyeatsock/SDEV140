"""
arrays_program2.py

This Python program is a simple game where the player has to guess the position of a ship on a board. 
The board size is determined at the start of the game. 
The player takes turns guessing the ship's position. 
After each guess, the board is displayed with the positions the player has guessed so far. 
The game continues until the player guesses the ship's position correctly.
"""
import random

def display_board(board_size: int, guessed_positions: list[int],
                  ship_position: int) -> None:
    # Display the board in format:
    #  . | O | O | . | X |
    #  1 | 2 | 3 | 4 | 5 |
    
    # Hint - you may use:
    # print(" X |", end="")
    # print(" O |", end="")
    # print(" . |", end="")
    # print(f" {i} |", end="")
    pass

def get_board_size() -> int:
    # Print an appropriate message and get the board size from the user. Prompt
    pass

def get_guess() -> int:
    # Print an appropriate message and get a guess from the user.
    pass
  
def is_hit(guess: int, ship_position: int) -> bool:
    # Return whether the guess hit the target
    pass

def initialize_ship_position(board_size: int) -> int:
    # Get a random start point on the board. randint(start,end)
    pass

def print_hit_message(is_hit: bool) -> None:
    # Print hit or miss message.
    pass

def take_turn(board_size: int, guessed_positions: list[int],
              ship_position: int) -> bool:
    # TODO: use existing functions to...
    # Get a guess from the user.
    # Update guessed positions.
    # Display the board.
    # Determine if hit.
    # Print hit message.
    # Return whether the battleship was hit.
    return

def main():
    print("Welcome to Battleship!")
    
    # TODO: Uncomment these one at a time and complete.
    # board_size: int = get_board_size()
    # ship_position: int = initialize_ship_position(board_size)
    # guessed_positions: list[int] = []
    # display_board(board_size, guessed_positions, ship_position)

    # TODO: Take turns until the battleship is sunk

if __name__ == "__main__":
    main()
