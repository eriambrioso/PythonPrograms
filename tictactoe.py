# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019
# Project: Tic Tac Toe

from sys import(stdin,stdout)

#read the input 
data = []
for i in range(3):                  
    data.append(stdin.readline())

str1 = data[0]
str2 = data[1]
str3 = data[2]

bd = str1[:3]+str2[:3]+str3[:3]    

#create rows and cols to represent each possible win
row1 = bd[:3]
row2 = bd[3:6]
row3 = bd[6:]
col1 = bd[0]+bd[3]+bd[6]
col2 = bd[1]+bd[4]+bd[7]
col3 = bd[2]+bd[5]+bd[8]
diag1 = bd[0]+bd[4]+bd[8]
diag2 = bd[2]+bd[4]+bd[6]

# The string of letters use by the monkeys in the game.

checklist = [row1, row2, row3, col1, col2, col3, diag1, diag2]
singlewinners = []
doublewinners = []

# check how many single or double winners there are
#must keep track of the winners to only count distinct wins

for i in checklist:
    if len(set(i))==1:
        if set(i) not in singlewinners:         #only add unique winners
            singlewinners.append(set(i))
    elif len(set(i))==2:
        if set(i) not in doublewinners:
            doublewinners.append(set(i))

print("double winners: ", doublewinners)
stdout.write('{}\n'.format(len(singlewinners)))
stdout.write('{}'.format(len(doublewinners)))

