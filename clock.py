""" ASCII Clock """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019

from sys import (stdin, stdout)

def clock(tm):
    """ Takes a time as input and prints it in desired format """
    if tm == 'end':
        return stdout.write('end')

    # each digit is assigned to a variable
    n_1 = int(tm[0])
    n_2 = int(tm[1])
    n_3 = int(tm[3])
    n_4 = int(tm[4])

    # the following are the lines needed to build characters
    l = '+---+'  # line
    sd = '|   |'  # sides
    sp = '+   +'  # side plusses
    d = '  o  '  # dot
    lp = '|    '  # left pipe
    rp = '    |'  # right pipe
    rpl = '    +'  # right plus
    e = '     '  # empty

    # each number can be represented by the lines defined above
    colon = [e, e, d, e, d, e, e]
    zero = [l, sd, sd, sp, sd, sd, l]
    one = [rpl, rp, rp, rpl, rp, rp, rpl]
    two = [l, rp, rp, l, lp, lp, l]
    three = [l, rp, rp, l, rp, rp, l]
    four = [sp, sd, sd, l, rp, rp, rpl]
    five = [l, lp, lp, l, rp, rp, l]
    six = [l, lp, lp, l, sd, sd, l]
    seven = [l, rp, rp, rpl, rp, rp, rpl]
    eight = [l, sd, sd, l, sd, sd, l]
    nine = [l, sd, sd, l, rp, rp, l]

    # number definitions
    chars = [zero, one, two, three, four, five, six, seven, eight, nine]

    for i in range(7):
        stdout.write('{} {}{}{} {}\n'.format(chars[n_1][i], chars[n_2][i],
                                             colon[i], chars[n_3][i], chars[n_4][i]))

DATA = []
for line in stdin:
    DATA = line.replace('\n', '')
    clock(DATA)
    stdout.write('\n')
