""" Spot on """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019
from sys import(stdin, stdout)

def generate_path(start, end, board):
    """ Checks if you can get from the start point to the desired
        finish point. returns 0 if can't be done """
    position = start
    if position == end:  # base case
        return 1

    if len(board) > position[0] + 1:  # if you can move up
        if board[position[0] + 1][position[1]] != '*':
            position[0] += 1
            generate_path(position, end, board[position[0]-1][position[1]].replace('M', '*').replace('.', '*'))
            return 1
    if len(board) > position[1] + 1:  # if you can move right
        if board[position[0]][position[1] + 1] != '*':
            position[1] += 1
            generate_path(position, end, board[position[0]][position[1]-1].replace('.', '*').replace('M', ''))
            return 1
    if position[0] > 0 and position[0] < len(board):  # if you can move down
        if board[position[0] - 1][position[1]] != '*':
            position[0] -= 1
            generate_path(position, end, board[position[0]+1][position[1]].replace('.', '*').replace('M', ''))
            return 1
    if position[1] > 0 and position[1] < len(board):  # if you can move left
        if board[position[0]][position[1] - 1] != '*':
            position[1] -= 1
            generate_path(position, end, board[position[0]][position[1]+1].replace('.', '*').replace('M', ''))
            return 1
    return 0

def move(tupper, dirr):  # tupper is top, right, front
    """ accepts the tupple describing the die's current position, and the direction you'd
        like to move the die. Returns the new position of the die"""
    # print(dirr)
    if dirr == 'north':
        output = [tupper[2], tupper[1], 7 - tupper[0]]
        return output
    if dirr == 'south':
        output = [7 - tupper[2], tupper[1], tupper[0]]
        return output
    if dirr == 'east':
        output = [tupper[1], 7 - tupper[0], tupper[2]]
        return output
    if dirr == 'west':
        output = [7 - tupper[1], tupper[0], tupper[2]]
        return output
    return 0

def get_bottom(tupper):
    """ RETURNS the bottom number of the die"""
    bot = 7 - tupper[0]
    return bot

# READ IN DATA
DATA = []
for line in stdin:
    DATA.append(line.replace('\n', '').replace('\r', ''))

BOARD = DATA[1:]
START = []
END = []
# find position of start and end
for i in range(len(BOARD)):
    for j in range(len(BOARD[i])):
        if BOARD[i][j] == 'M':
            START = [i, j]
        if BOARD[i][j] == '1' or BOARD[i][j] == '2' or BOARD[i][j] == '3' or BOARD[i][j] == '4' or BOARD[i][j] == '5' or \
                BOARD[i][j] == '6':
            END = [i, j]

if generate_path(START, END, BOARD) > 0:
    stdout.write('Yes')
else:
    stdout.write('No')
