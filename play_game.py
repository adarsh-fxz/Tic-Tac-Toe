"""
This module contains the main function to run the "Unbeatable Noughts and Crosses" game.
The main function is responsible for running the game and handling the user's choices from the menu.
"""

from noughtsandcrosses import welcome, menu, play_game, save_score, load_scores
from noughtsandcrosses import display_leaderboard

def main():
    """
    Main function to run the "Unbeatable Noughts and Crosses" game.
    """
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:', total_score)
        elif choice == '2':
            save_score(total_score)
        elif choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        elif choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return

# Program execution begins here
if __name__ == '__main__':
    main()
