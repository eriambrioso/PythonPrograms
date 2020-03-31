""" How Clever is That? """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019

from sys import(stdin, stdout)

def open_count(grid):
    count = 0
    for j in range(5):
        for i in range(5):
            if grid [i][j] == 0:
                count += 1
    return count

def run_game(grid):
    """ Runs the scenerio of the manatees eating on the grid"""
    x1 = 0          # x1/y1 = Hugh Manatee
    y1 = 0
    x2 = 4          # xw/y2 = Herb Manatee
    y2 = 4

    while open_count(grid) >= 1:
        # cannot go on squares with a 1
        # cannot go on the same square
        # will always go to a square with a 0 if they can

        if x1 == x2 and y1 == y2:
            return 1

    return 0

K = int(stdin.readline())
COUNT = 0
# the intial grid
GRID = [[1, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0,],           # 0 means there is seagrass at that position
        [0, 0, 0, 0, 0,],           # 1 means there is no seagrass
        [0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 1,]]

GAP = []
for i in range(K):
    GAP = stdin.readline().split(" ")
    X = int(GAP[0])
    Y = int(GAP[1])

    GRID[X][Y] = 1

if run_game(GRID) == 1:
    COUNT += 1
