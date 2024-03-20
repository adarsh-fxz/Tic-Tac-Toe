"""
Unbeatable Noughts and Crosses game or Tic-Toc-Toe.
This program allows the user to play a game of Noughts and Crosses against the computer.
"""

import random
import os.path
import json
random.seed()

def draw_board(board):
    """
    Displays the current state of the game board.

    Parameter:
    - board: 2D list representing the game board.
    """

    # develop code to draw the board
    print(' -----------')
    for row in board:
        print(f'| {row[0]} | {row[1]} | {row[2]} |')
        print(' -----------')

def welcome(board):
    """
    Prints a welcome message and displays the initial game board.

    Parameter:
    - board: 2D list representing the game board.
    """

    # prints the welcome message
    print('\nWelcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below:')

    # display the board by calling draw_board(board)
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')

def initialise_board(board):
    """
    Sets all elements of the game board to a space ' '.

    Parameter:
    - board: 2D list representing the game board.

    Returns:
    - board: Updated game board.
    """

    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        board[i] = ([' ']*3)
    return board

def get_player_move(board):
    """
    Gets the player's move by asking for input.

    Parameter:
    - board: 2D list representing the game board.

    Returns:
    - row (int): Row index of the player's move.
    - col (int): Column index of the player's move.
    """

    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            print('Choose your square:')
            user_input = int(input('1 2 3\n4 5 6\n7 8 9 : '))
            if (user_input < 1 or user_input > 9):
                print('Invalid input. Please enter a number between 1 and 9.')
                continue

            row = (user_input - 1) // 3
            col = (user_input - 1) % 3
            if board[row][col] != ' ':
                print('Invalid input. Please choose an empty square.')
                continue
            break

        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.')

    return row, col

def choose_computer_move(board):
    """
    Chooses a random move for the computer on the game board.

    Parameter:
    - board: 2D list representing the game board.

    Returns:
    - row (int): Row index of the computer's move.
    - col (int): Column index of the computer's move.
    """

    # develop code to let the computer chose a cell to put a nought in
    # and return row and col

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            break
    return row, col

def check_for_win(board, mark):
    """
    Checks if a player (or computer) has won the game.

    Parameters:
    - board (list): 2D list representing the game board.
    - mark (str): Player's mark ('X' or 'O').

    Returns:
    - bool: True if the player has won, False otherwise.
    """

    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
        if board[0][0] == board[1][1] == board[2][2] == mark:
            return True
        if board[0][2] == board[1][1] == board[2][0] == mark:
            return True

    return False

def check_for_draw(board):
    """
    Checks if the game is a draw (all cells occupied).

    Parameter:
    - board: 2D list representing the game board.

    Returns:
    - bool: True if the game is a draw, False otherwise.
    """

    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    """
    Plays a round of the game, alternating between player and computer moves.

    Parameter:
    - board: 2D list representing the game board.

    Returns:
    - int: Score of the game (-1 for computer win, 0 for draw, 1 for player win).
    """

    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop

    initialise_board(board)
    draw_board(board)

    while True:
        row , col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X' ):
            return 1

        if check_for_draw(board):
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1

        if check_for_draw(board):
            return 0

def menu():
    """
    Gets user input for menu options.

    Returns:
    - choice (str): User's choice ('1', '2', '3', or 'q').
    """

    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program

    print('\nEnter one of the following options:')
    print('1 - Play the game')
    print('2 - Save your score in the leaderboard')
    print('3 - Load and display the leaderboard')
    print('q - End the program')
    choice = input('\nEnter your choice: ')
    if choice not in ['1', '2', '3', 'q']:
        print('Invalid input. Please enter 1, 2, 3 or q.')
        return menu()

    return choice

def load_scores():
    """
    Loads the leaderboard scores from the file 'leaderboard.txt'.

    Returns:
    - leaders (dict): Dictionary with player names as keys and scores as values.
    """

    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders

    leaders = {}
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r', encoding='utf-8') as file:
            leaders = json.load(file)
    return leaders

def save_score(score):
    """
    Saves the player's score to the leaderboard file 'leaderboard.txt'.

    Parameters:
    - score (int): The player's score.

    Prompts the player for their name, updates the leaderboard, and saves it to the file.
    """

    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    name = input('Enter your name: ')
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w', encoding='utf-8') as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    """
    Displays the leaderboard scores from the provided dictionary.

    Parameters:
    - leaders (dict): Dictionary with player names as keys and scores as values.
    """

    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader

    print('\nLeaderboard:')
    for name, score in leaders.items():
        print(f'{name}: {score}')
