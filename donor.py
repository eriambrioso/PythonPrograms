""" Donor Party """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019
from sys import(stdin, stdout)

def find_max(input):
    """ returns the donation from any given donor"""
    max = int(input[0][0])
    for i in range(len(input)):
        if max < int(input[i][0]):
            max = int(input[i][0])

    return str(max)

def collect(input):
    """ finds possible donation options based on order and time
        and selects the highest possibility """
    donors = []
    donation = 0
    max = find_max(input)
    for i in range(len(input)):
        """ find all donors with the max donations"""
        if input[i][0] == max:
            donors.append(input[i])
    if len(donors) == 1:
        donation += int(donors[0][0])
    else:
        """ chose the one with the shorter wait timeout"""
        for i in range(len(donors)):
            if donors[i][1] == find_min(donors):
                donation += int(donors[i][0])
    return donation

def main():
    """ Driver function that accepts inputs and prints the output"""
    data = []
    row = []
    for line in stdin:
        row = line.replace('\n', '').split()
        data.append(row)

    donation = collect(data[1:])
    #stdout.write('{}'.format(donation))
    max = 0
    for i in range(len(data[1:])):
        max += int(data[i+1][0])
    stdout.write('{}'.format(max))
main()