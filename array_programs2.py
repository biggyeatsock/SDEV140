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
    for counter in range(0, board_size, 1):
        if counter == 0: # This just prints a blank board in format
            for x in range(board_size):
                print(" . |", end='')
            print()
            for i in range(board_size):
                print(f" {i+1} |", end="")
        
        if counter != 0:
            for x in range(0,board_size):
                if guessed_positions[x] != ship_position:
                    print(" 0 |", end="")
                elif guessed_positions[x] == ship_position:
                    print(" X |", end="")
                else:
                    print(" . |", end="")
            print()
            for i in range(board_size):
                print(f" {i+1} |", end="")
    pass

def get_board_size() -> int:
    # Print an appropriate message and get the board size from the user. Prompt
    num = int(input("Enter the size of the board: "))
    return num
    

def get_guess() -> int:
    # Print an appropriate message and get a guess from the user.
    guess = int(input("\nEnter a guess: "))
    return guess
  
def is_hit(guess: int, ship_position: int) -> bool:
    # Return whether the guess hit the target
    if guess == ship_position:
        sunk = True
        return sunk
    pass

def initialize_ship_position(board_size: int) -> int:
    # Get a random start point on the board. randint(start,end)
    numran = random.randint(0,board_size) # This will work, just not right now. THeres another issue at hand.
    return numran
    # pass

def print_hit_message(is_hit: bool) -> None:
    # Print hit or miss message.
    print("\nYou've sunk the ship! You Win!!!")
    pass

def take_turn(board_size: int, guessed_positions: list[int],
              ship_position: int) -> bool:
    # TODO: use existing functions to...
    # Get a guess from the user.
    guess = get_guess()
    # Update guessed positions.
    guessed_positions.append(guess)
    print(ship_position)
    # Display the board.
    display_board(board_size, guessed_positions, ship_position)
    # Determine if hit.
    if guess == ship_position:
        is_hit(guess, ship_position)
    # Print hit message.
        print_hit_message(is_hit)
    # Return whether the battleship was hit.
    else:
        print("Miss!")
    return

def main():
    print("Welcome to Battleship!")
    # TODO: Uncomment these one at a time and complete.
    board_size: int = get_board_size() # board size
    ship_position: int = initialize_ship_position(board_size) # ship location
    guessed_positions: list[int] = [0] # guessed positions
    display_board(board_size, guessed_positions, ship_position)
    print('\n',ship_position) # Just for debugging purposes, this will need to be removed before finally submitting!!!!!!!
    # TODO: Take turns until the battleship is sunk
    
    take_turn(board_size, guessed_positions, ship_position)
        

if __name__ == "__main__":
    main()
