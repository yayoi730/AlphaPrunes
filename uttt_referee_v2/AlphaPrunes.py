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
def readMoves():
    f = open("move.txt", "r")
    lines = f.readlines()
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
