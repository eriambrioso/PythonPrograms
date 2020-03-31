# Author: Quentin Johnson, qjohnson2017@my.fit.edu
# Course: CSE 2050, Fall 2019
# Project: RFID Tags
from sys import(stdin, stdout, stderr)
from itertools import (product)
INPUT = []
INPUT = stdin.readline().split()

N = INPUT[0]
S = INPUT[1]
E = INPUT[2]

N = int(N)
S = int(S)
E = int(E)

CHARS = []
CODELIST = []
CODES = []

i = 0
for line in stdin:
    tup = line.replace('\n', '')
    CHARS.append(tup)

CODELIST = product(*CHARS)
for i in CODELIST:
    if len(set(i)) == len(i):
        CODES.append(i)

COUNT = 0
for i in CODES:
    COUNT += 1
    if COUNT >= S and COUNT <= E:
        stdout.write('{}\n'.format(''.join(i)))
