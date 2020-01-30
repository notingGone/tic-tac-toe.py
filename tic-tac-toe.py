#!/usr/bin/env python
# coding: utf-8

import os
from subprocess import call

def clear_screen():
    _ = call('clear' if os.name == 'posix' else 'cls')

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

def get_valid_move(moves):
    if moves.count("O") == moves.count("X"): player = "X"
    else: player = "O"
    while True:
        move = input(f"{player.upper()}'s turn: ")
        try:
            move = int(move)
        except ValueError:
            print("That is not a valid number")
            continue
        if not move in range(1,10):
            print("There are only cells 1 through 9")
            continue
        if (moves[move] != ' '):
            print("That square has already been played")
            continue
        moves[move] = player
        return

def check_for_winner(moves):
    winners = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], #h'zontal
                [1, 4, 7], [2, 5, 8], [3, 6, 9], #vertical
                [1, 5, 9], [3, 5, 7]             #diagonal
              ]
    for line in winners:
        if moves[line[0]] == moves[line[1]] == moves[line[2]] != ' ':
            return moves[line[0]]
    return False

def game():
    moves = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print_grid(moves)
    winner = False
    while ' ' in moves and winner == False:
        get_valid_move(moves)
        winner = check_for_winner(moves)
        print_grid(moves)
    if winner:
        print(f"Congradulations to {winner}!\nYou won!")
    else:
        print("Cat's game...")

game()
