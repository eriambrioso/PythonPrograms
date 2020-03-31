""" Seagrass Bundles """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019

from sys import(stdin, stdout)

DATA = []
DATA = stdin.readline().split(" ")
N = int(DATA[0])
K = int(DATA[1])
# Create empty bins for each dock
DOCKS = []
for i in range(N):
    DOCKS.append(int(0))

for line in stdin:
    DATA = line.split(" ")
    s = int(DATA[0])
    e = int(DATA[1])

    # Add to the bins within the range s:e
    for j in range(s-1, e):
        DOCKS[j] = DOCKS[j] + 1

    # Find max and min and subtract the difference
    DIFF = max(DOCKS) - min(DOCKS)
stdout.write('{}\n'.format(DIFF))
