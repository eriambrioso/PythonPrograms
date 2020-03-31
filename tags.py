""" RFID Tags """
# Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019

from itertools import(product)
from sys import(stdin, stdout)

DATA = []
ROW = []
result = []
for line in stdin:
    ROW = line.replace('\n', '').split()
    DATA.append(ROW)

N = int(DATA[0][0])      # number of lines of strings
S = int(DATA[0][1])      # start count
E = int(DATA[0][2])      # end count

count = 0                # this will be used to help us print the desired range later
char_str = []
final = []         # final will hold the possible codes

for i in range(N):
    char_str.append(str(DATA[i+1]))
    char_str[i] = char_str[i][2:len(char_str[i])-2]

code_list = product(*char_str)
for i in code_list:
    if len(set(i)) == len(i):   # We must get rid of any codes with duplicate letters
        final.append(i)

# Print the desired range (E:S)
for c in final:
    count += 1
    if count >= S and count <= E:
        stdout.write('{}\n'.format(''.join(c)))
