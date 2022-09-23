import numpy as np
from random import random

import pygame

board = np.zeros((9, 9))

def initBoard():
    readMoves('first_four_moves.txt')


def makeAMove():
    readMoves()
    findNextMove()
    addMove()
def readMoves(file):
    f = open(file, "r")
    lines = file.readlines()
    for line in lines:
        last_move = line
        if line.isspace():
            break
        else:
            # populates matrices
            moves = line.split()
            if moves[0] == "X":
                board[int(moves[1]),int(moves[2])] = 1 # X = 1
            else:
                board[int(moves[1]), int(moves[2])] = 2 # O = 2
    return last_move

def findNextMove():
    lastMove = readMoves("move.txt")
    takenList = []
    for i in range(0,8):
        if board[lastmove[2]][i] = 1 or board[lastMove[2]][i] = 2:
            takenList.append(board[lastmove[2]][i])
    move = [lastmove[2],random.choice([i for i in range(0,8) if i not in takenList])]
    board[move[0]][move[1]] = 1
    return move
def addMove():
