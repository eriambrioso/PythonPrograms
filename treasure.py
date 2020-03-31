# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Treaure Hunt

from sys import(stdin,stdout)
import itertools as it

map1 = []
row = []
for line in stdin:
    row = line.replace('\n','').split(" ")
    for i in range(len(row)):
        int(row[i])
    map1.append(row)

routes = it.product(range(3), repeat=len(map1))

# Removes all routes that collect the same treasure at successive islands
goodroutes=[]
for i in routes:
    check=[]
    for j in range(len(i)-1):
        if i[j] != i[j+1]:
            check.append(True)
        else: 
            check.append(False)          
    if False not in check:
        goodroutes.append(i)

# Creates a list of all the sums for the routes in goodroutes.
sumlist =[]                    
for i in range(len(goodroutes)):
    sum = 0
    for j in range(len(goodroutes[0])):
        sum += int(map1[j][goodroutes[i][j]])
    sumlist.append(sum)

# Prints the list of sums and then the maximum value in that list.

print('{}'.format(max(sumlist))) 

