"""Alto Sax Fingering"""
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Alto Saxophone
from sys import(stdin, stdout)
c = {2, 3, 4, 7, 8, 9, 10}
d = {2, 3, 4, 7, 8, 9}
e = {2, 3, 4, 7, 8}
f = {2, 3, 4, 7}
g = {2, 3, 4}
a = {2, 3}
b = {2}
C = {3}
D = {1, 2, 3, 4, 7, 8, 9}
E = {1, 2, 3, 4, 7, 8}
F = {1, 2, 3, 4, 7}
G = {1, 2, 3, 4}
A = {1, 2, 3}
B = {1, 2}

DATA = []           #each entry in data[] will be a different song
SONG = []

for line in stdin:
    SONG = line.replace('\n', '').split(" ")
    DATA.append(SONG)

for j in range(len(DATA)):
    SONG = str(DATA[j])
    SONG = SONG[2:len(SONG)-2]

    # A dictionary with the keys being notes and the values sets of fingers that must be pressed
    finger_dict = dict(zip('cdefgabCDEFGAB', [c, d, e, f, g, a, b, C, D, E, F, G, A, B]))
    # A list of lists (bins) to keep track of how many times each finger is pressed.
    finger_bins = []
    for i in range(0, 10):
        finger_bins.append(0)
    CHECK = 0
    # Count finger presses for the first note
    if len(SONG) > 0:
        firstnote = SONG[0]
    else:
        CHECK = 1

    for i in finger_dict[firstnote]:
        finger_bins[i - 1] += 1

    # Now we need to count the rest of the key presses.   Since the fingerings are listed as sets
    # we can use set difference to figure out which keys were pressed.
    # Then increment the appropriate bins.
    for i in range(len(SONG) - 1):
        note = SONG[i]  # current note
        nextnote = SONG[i + 1]  # next note played
        # set of fingers pressed in transition
        fingers_pressed = finger_dict[nextnote] - finger_dict[note]
        # This loop counts how many times each note was pressed add increments the bins.
        for fin in fingers_pressed:
            finger_bins[fin - 1] += 1

    if CHECK == 1:
        for i in range(10):
            stdout.write('{} '.format(int(0)))
    else:
        for i in finger_bins:
            stdout.write('{} '.format(i))
    stdout.write('\n')
