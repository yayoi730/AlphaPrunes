import os
from os.path import exists
import time

import numpy as np
import random

import pygame

board = np.zeros((9, 9)) # stores the moves that have been played


def main():
    print("hello")
    while not exists("end_game"):
        time.sleep(5)
        while not exists("AlphaPrunes.go"):
            pass
        last_move = readMoves('first_four_moves')
        move = findNextMove(last_move)
        addMove(move, last_move)

def readMoves(file):
    # reads in txt file and populates the board with the move information
    # returns the last move made in a list ex: ['X'. '1' '2']
    f = open(file)
    lines = f.readlines()
    for line in lines:
        last_move = line
        if line.isspace():
            break
        else:
            # populates matrices
            moves = line.split()
            if moves[0] == "X":
                board[int(moves[1])][int(moves[2])] = 1  # X = 1
            else:
                board[int(moves[1])][int(moves[2])] = 2  # O = 2
    f.close()
    return last_move


def findNextMove(lastMove):
    # function that determines the next move the player will make
    lastMove = int(lastMove[2])
    takenList = []
    for i in range(0, 8):
        if board[lastMove][i] == 1 or board[lastMove][i] == 2:
            takenList.append(board[lastMove][i])
    move = [lastMove, random.choice([i for i in range(0, 8) if i not in takenList])]
    return move


def addMove(move, lastmove):
    # function that takes in the next move (int) and adds it to move_file
    f = open("move_file", "r+")
    f.truncate(0)
    if lastmove[0] == "X":
        board[int(move[0])][int(move[1])] = 2
        f.write("0 " + str(move[0]) + " " + str(move[1]))
    else:
        board[int(move[0])][int(move[1])] = 1
        f.write("X " + str(move[0]) + " " + str(move[1]))
    f.close()
    display()

def display():
    # function that can be called to display the current state of the board
    # arranged in ultimate tic-tac-toe style (X = 1 and O = 2)
    print("Current Board:")
    print(str(board[0][0:3]) + " | " + str(board[1][0:3]) + " | " + str(board[2][0:3]))
    print(str(board[0][3:6]) + " | " + str(board[1][3:6]) + " | " + str(board[2][3:6]))
    print(str(board[0][6:9]) + " | " + str(board[1][6:9]) + " | " + str(board[2][6:9]))
    print("------------------------------------")
    print(str(board[3][0:3]) + " | " + str(board[4][0:3]) + " | " + str(board[5][0:3]))
    print(str(board[3][3:6]) + " | " + str(board[4][3:6]) + " | " + str(board[5][3:6]))
    print(str(board[3][6:9]) + " | " + str(board[4][6:9]) + " | " + str(board[5][6:9]))
    print("------------------------------------")
    print(str(board[6][0:3]) + " | " + str(board[7][0:3]) + " | " + str(board[8][0:3]))
    print(str(board[6][3:6]) + " | " + str(board[7][3:6]) + " | " + str(board[8][3:6]))
    print(str(board[6][6:9]) + " | " + str(board[7][6:9]) + " | " + str(board[8][6:9]))


if __name__ == "__main__":
    main()
