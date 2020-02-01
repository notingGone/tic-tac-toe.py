#!/usr/bin/env python3

"""This script plays a little game of tic-tac-toe in your console."""

import os
from subprocess import call


def clear_screen():
    """Clear the screen with OS appropriate system call."""
    call('clear' if os.name == 'posix' else 'cls')


def print_grid(moves_arr):
    """Print a 3x3 ascii grid with moves filled in from provided array.

    Argument:
    l -- Cumulative list of length 10 containing all moves with the
         index mapped to the board as a 10-key layout.  Index 0 should
         be a non-space character for index offset purposes.
         Any cell on the board that has not been played should contain
         a single space character (' ').  Otherwise, it should contain
         a corresponding 'X' or 'O'.
    """
    grid = [
        '     |     |     ',
        '     |     |     ',
        '  {}  |  {}  |  {}  '.format(moves_arr[7], moves_arr[8], moves_arr[9]),
        '     |     |     ',
        '     |     |     ',
        '-----------------',
        '     |     |     ',
        '     |     |     ',
        '  {}  |  {}  |  {}  '.format(moves_arr[4], moves_arr[5], moves_arr[6]),
        '     |     |     ',
        '     |     |     ',
        '-----------------',
        '     |     |     ',
        '     |     |     ',
        '  {}  |  {}  |  {}  '.format(moves_arr[1], moves_arr[2], moves_arr[3]),
        '     |     |     ',
        '     |     |     '
    ]
    clear_screen()
    print('\n'.join(grid))


def get_valid_move(board_list):
    """Get and return a valid, unplayed cell number.

    Argument:
    board_list -- Cumulative list of length 10 containing all moves.
                  Used to check if move has already been played.
    """
    while True:
        move = input('Your move: ')
        try:
            move = int(move)
        except ValueError:
            print('That is not a valid number')
            continue
        if  move not in range(1, 10):
            print('There are only cells 1 through 9')
            continue
        if board_list[move] != ' ':
            print('That square has already been played')
            continue
        return move


def has_winner(board_array):
    """Check winning cell combinations and return True if winner is found.

    Argument:
    board_list -- Cumulative list of length 10 containing all moves.
    """
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # H'zontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
        [1, 5, 9], [3, 5, 7]              # Diagonal
    ]

    for cells in winning_lines:
        if (board_array[cells[0]]
                == board_array[cells[1]]
                == board_array[cells[2]]
                != ' '):
            return True
    return False


def toggle_player():
    """Generator. Alternately return 'X' or 'O' when iterated upon.

    e.g.
        toggler = toggle_player()
        current_player = next(toggler) # -> 'X'
        current_player = next(toggler) # -> 'O'
    """
    while True:
        yield 'X'
        yield 'O'


def game():
    """Play tic-tac-toe."""
    board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print_grid(board)
    winner = False
    get_player = toggle_player()

    while ' ' in board and not winner:
        current_player = next(get_player)
        print(f"{current_player}'s turn. ", end='')
        current_move = get_valid_move(board)
        board[current_move] = current_player
        winner = has_winner(board)
        print_grid(board)

    if winner:
        print(f'You won! Congradulations to {current_player}!')
    else:
        print("Cat's game...")


game()
