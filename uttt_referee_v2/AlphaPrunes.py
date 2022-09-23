import numpy as np
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

def addMove():
