""" Social Hierarchy """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2018

from sys import(stdin, stdout)

DATA = []
INPUT = []
for line in stdin:
    DATA.append(line.replace('\n', '').replace('\r', ''))
INPUT = DATA[0].split(' ')

COUNT = int(INPUT[0])  # The number of manatees in the lagoon
ORDER_COUNT = int(INPUT[1])  # The number that have arranged themselves
FIXED_COUNT = int(INPUT[2])  # Number who demand a position

#  Input Data
ORDER = DATA[1].split(' ') # Second line of input is always the social order
# We create a list to store the current order
ORDER_LIST = [0 for i in range(COUNT)]

#  We place manatees with fixed position in the current order
FIXED_LIST = []

for i in range(FIXED_COUNT):
    fixed = (int(DATA[i+2][0]), int(DATA[i+2][2]))
    FIXED_LIST.append(fixed)

for i in range(FIXED_COUNT):
    num = FIXED_LIST[i][0]
    pos = FIXED_LIST[i][1] - 1
    ORDER_LIST[pos] = num

#  Place all the manatees in a social order in the latest possible position.
for i in range(len(ORDER) - 1, -1, -1):
    if ORDER[i] in ORDER_LIST:  # is the manatee already in place?
        #print('first loop')
        continue
    if i == len(ORDER) - 1:
        #print('second loop', ORDER[i])
        for j in range(len(ORDER_LIST)-1, -1, -1):
            if ORDER_LIST[j] == 0:
                ORDER_LIST[j] = ORDER[i]
                break
        continue

    if ORDER[i] != ORDER_LIST and ORDER[i+1] not in ORDER_LIST:
        #print('third loop', ORDER[i])
        for j in range(len(ORDER_LIST)-1, -1, -1):
            if ORDER_LIST[j] == 0:
                ORDER_LIST[j] = ORDER[i]
                break
    if i < len(ORDER) - 1 and ORDER[i+1] in ORDER_LIST:
        #print('fourth loop', ORDER[i])
        for k in range(i, -1, -1):
            if ORDER_LIST[k] == 0:
                ORDER_LIST[k] = ORDER[i]
                break

# Finally the answer is the first 0 in the order_list
for i in range(len(ORDER_LIST)):
    if ORDER_LIST[i] == 0:
        stdout.write('{}'.format(i+1))
        break
