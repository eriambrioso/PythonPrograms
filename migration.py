""" Manatee Migration """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019

from sys import(stdin, stdout)
from decimal import(Decimal)

def calculate_dist(num, cap, rate):
    """ Calculates the total distance recursively"""
    if num == 0:
        return cap*rate
    return (cap*rate)/(2*num-1) + calculate_dist(num-1, cap, rate)

DATA = []
ROW = ()
for line in stdin:
    ROW = line.replace('\n',  '').split()
    for i in range(len(ROW)):
        Decimal(ROW[i])
    DATA.append(ROW)

for i in range(len(DATA)):
    N = int(DATA[i][0])     # N is the number of full cans initially
    C = Decimal(DATA[i][1])     # C is the capacity of the boat's engine
    R = Decimal(DATA[i][2])    # R is the rate gas is consumed/100km

    R = 100/R
    #print(R)
    TOTAL = Decimal(calculate_dist(N-1, C, R))

    stdout.write('{}\n'.format(round(TOTAL, 5)))
