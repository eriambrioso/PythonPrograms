""" Transition matrix """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019
# Project: Page Rank

from sys import (stdin, stdout, argv)

def num_connections(value, list):
    """ returns the number of times that a value is in a list """
    count = 0
    for element in list:
        for thing in element:
            if int(thing) == value:
                count+=1
    return count

def build_matrix(size, prob, graph):
    n = size #number of nodes
    matrix = {}
    for i in range(size):
        row = []
        for j in range(size):
            # determine what type it is..how many
            connects = num_connections(j, graph[i])     # how many times the connection is repeated
            e = 0
            for k in range(len(graph[i])):
                e += len(graph[i][k])
            if connects == 0:        # no connection
                row.append(prob/n)
            elif connects == 1:        # one connection
                row.append(1 - (prob*(n-e)/n))
                #row.append(0)
            else:                                       # one or more connections
                sum =(n-connects)*prob
                row.append(((1-sum)/(n-e+connects)) *(e/n))
            matrix[i] = row
    stdout.write('{} {}\n'.format(size, size))
    print(matrix)
    return matrix

    #connect = (1-(sum of no connects))/(n-e)*(w/n)
"""
    print(float.fromhex('0x1.47ae147ae147bp-6'))
    #print(float.hex(.02))
    print(float.fromhex('0x1.d70a3d70a3d71p-1'))
    print(float.fromhex('0x1.e147ae147ae15p-2'))
    print(float.fromhex('0x1.851eb851eb852p-2'))
    print(float.fromhex('0x1.9999999999999p-3'))

"""

def main():
    """ Main function to call the other functions and read input """
    graph = {}
    prob = float(argv[2])
    size = int(stdin.readline())

    for i in range(size):
        graph[i] = []
    for line in stdin:
        input = []
        line = line.replace('\r', '').replace('\n', '').split()
        for element in line:
            if int(element) != int(line[0]):
                input.append(element)

        graph[int(line[0])].append(input)

    return build_matrix(size, prob, graph)

main()
