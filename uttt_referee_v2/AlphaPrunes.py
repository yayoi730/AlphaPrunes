import numpy as np
from random import random

import pygame

board = np.zeros((9, 9))


def main():
    readMoves('first_four_moves.txt')
    


def makeAMove():
    readMoves()
    findNextMove()
    addMove()


def readMoves(file):
    f = open(file, "r")
    lines = file.readlines()
    for line in lines:
        lastMove = line
        if line.isspace():
            break
        else:
            # populates matrices
            moves = line.split()
            if moves[0] == "X":
                board[int(moves[1]), int(moves[2])] = 1  # X = 1
            else:
                board[int(moves[1]), int(moves[2])] = 2  # O = 2
    return lastMove


def findNextMove():
    lastMove = readMoves("move.txt")
    takenList = []
    for i in range(0, 8):
        if board[lastMove[2]][i] == 1 or board[lastMove[2]][i] == 2:
            takenList.append(board[lastMove[2]][i])
    move = [lastMove[2], random.choice([i for i in range(0, 8) if i not in takenList])]
    return move


def addMove(globalBoard, localBoard):
    board[globalBoard][localBoard] = 1
    f = open("move_file.txt", "a")
    f.write("X " + globalBoard + " " + localBoard)
    f.close()

if __name__ == "__main__":
    main()
