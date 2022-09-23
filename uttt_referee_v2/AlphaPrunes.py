import os
from os.path import exists

import numpy as np
import random

import pygame

board = np.zeros((9, 9))


def main():
    while not exists("AlphaPrunes.go"):
        pass
    print("here1")
    print(os.listdir())
    move = findNextMove(readMoves('first_four_moves'))
    addMove(int(move[0]), int(move[1]))


def readMoves(file):
    f = open(file)
    lines = f.readlines()
    for line in lines:
        lastMove = line
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
    return lastMove


def findNextMove(lastMove):
    print(board)
    lastMove = int(lastMove[2])
    takenList = []
    for i in range(0, 8):
        if board[lastMove][i] == 1 or board[lastMove][i] == 2:
            takenList.append(board[lastMove][i])
    move = [lastMove, random.choice([i for i in range(0, 8) if i not in takenList])]
    print(move)   
    return move


def addMove(globalBoard, localBoard):
    board[globalBoard][localBoard] = 1
    print(board)
    f = open("move_file", "a")
    f.write("X " + globalBoard + " " + localBoard)
    f.close()


if __name__ == "__main__":
    main()
