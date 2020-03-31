"""Never mind"""
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Never Mind

from sys import(stdin, stdout)
DATA = []
DATA = stdin.readline().split(" ")

LENGTH = int(DATA[0])
CODE = DATA[1]
guess = DATA[2]

# The set of letters in the code.  This is used to elimimate repetitions.
let = set(CODE)

# Initialize variables for the counting
r = 0
s = 0

# We initialize the dictionary.
let_dict = dict(zip(let, [0 for i in range(len(let))]))

# We set up the letter counts for let_dict.
for c in CODE:
    let_dict[c] += 1

# We initialize a dictionary to keep track of what letters have been guessed.
guessed_let = dict(zip(let, [0 for i in range(len(let))]))

# We loop through the guessed letters and find out which ones are in the code and
# in the correct position.
for i in range(LENGTH):
    if guess[i] in CODE: # Is guess in code?
        if CODE[i] == guess[i]: # Is position correct.
            guessed_let[CODE[i]] += 1 # We used the letter.
            r += 1

# Now we look to see if any of the other letters are correct but in the wrong position.
for i in range(LENGTH):
    # Check that the guessed letter is in the code, in the wrong position, and not yet counted.
    if guess[i] in CODE and CODE[i] != guess[i] and guessed_let[guess[i]] < let_dict[guess[i]]:
        guessed_let[guess[i]] += 1 # We show that used this letter.
        s += 1 # Increment the count of correct letters in the wrong position

# Output the counts.
stdout.write('{} {}'.format(r, s))
