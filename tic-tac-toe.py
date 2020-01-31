#!/usr/bin/env python3
# coding: utf-8

import os
from subprocess import call

def clear_screen():
    call('clear' if os.name == 'posix' else 'cls')

def print_grid(a):
    grid = [
        "     |     |     ",
        "     |     |     ",
       f"  {a[7]}  |  {a[8]}  |  {a[9]}  ",
        "     |     |     ",
        "     |     |     ",
        "-----------------",
        "     |     |     ",
        "     |     |     ",
       f"  {a[4]}  |  {a[5]}  |  {a[6]}  ",
        "     |     |     ",
        "     |     |     ",
        "-----------------",
        "     |     |     ",
        "     |     |     ",
       f"  {a[1]}  |  {a[2]}  |  {a[3]}  ",
        "     |     |     ",
        "     |     |     "
    ]
    clear_screen()
    print('\n'.join(grid))

def get_valid_move(board_array):
    while True:
        move = input(f"Your move: ")
        try:
            move = int(move)
        except ValueError:
            print("That is not a valid number")
            continue
        if not move in range(1,10):
            print("There are only cells 1 through 9")
            continue
        if (board_array[move] != ' '):
            print("That square has already been played")
            continue
        return move

def has_winner(board_array):
    winning_lines = [ [1, 2, 3], [4, 5, 6], [7, 8, 9],  #h'zontal
                      [1, 4, 7], [2, 5, 8], [3, 6, 9],  #vertical
                      [1, 5, 9], [3, 5, 7]  ]           #diagonal
    for cells in winning_lines:
        if board_array[cells[0]] == board_array[cells[1]] == board_array[cells[2]] != ' ':
            return True
    return False

def toggle_player():
    while True:
        yield 'X'
        yield 'O'

def game():
    board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print_grid(board)
    winner = False
    get_player = toggle_player()
    while ' ' in board and winner == False:
        current_player = next(get_player)
        print(f"{current_player}'s turn. ", end='')
        current_move = get_valid_move(board)
        board[current_move] = current_player
        winner = has_winner(board)
        print_grid(board)
    if winner:
        print(f"You won! Congradulations to {current_player}!")
    else:
        print("Cat's game...")
    return True
game()
