#!/usr/bin/python3
''' Python3 program to solve N Queen '''
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)
N = sys.argv[1]
try:
    N = int(N)

except:
    print('N must be a number')
    exit(1)

if N < 4:
    print('N must be at least 4')
    exit(1)

k = 1


def printSolution(board):
<<<<<<< HEAD
""" A utility function to print solution """
=======
    """ A utility function to print solution """
>>>>>>> edf7d1035eaf240a5f9ea7e096db12608fb50a56
    queens = []
    global k
    k = k + 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j]:
            return False
        i = i + 1
        j = j - 1
    return True
def solveNQUtil(board, col):
<<<<<<< HEAD

