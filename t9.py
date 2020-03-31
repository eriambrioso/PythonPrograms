""" Trie Trie Again """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019
from sys import (stdin, stdout)
from itertools import *

def find_max(dictionary):
    max_word = dictionary[0]
    for i in range(len(dictionary)):
        if int(dictionary[i][1]) > int(max_word[1]):
           max_word = dictionary[i]

    return max_word

def search_in(combos, dictionary):
    output = []
    for k in range(len(dictionary)):
        for i in range(len(combos)):
            for j in range(len(combos[i])):
                combos[i][j] = ''.join(combos[i][j])
                if combos[i][j] in dictionary[k][0]:
                    output.append(combos[i][j])

    output = set(output)
    final = []
    for J in range(len(dictionary)):
        for thing in output:
            if thing in dictionary[J][0] and thing != dictionary[J][0]:
                value = dictionary[J][1]
                final.append([thing, value])
    size = len(final)
    for i in range(size):
        yikes = find_max(final)
        final.remove(yikes)
        stdout.write('{}\n'.format(yikes[0]))


def decode(dictionary, sequences):
    nums = ['two', 'three', 'four', 'five', 'six',
            'seven', 'eight', 'nine']
    two = ['a', 'b', 'c']
    three = ['d', 'e', 'f']
    four = ['g', 'h', 'i']
    five = ['j', 'k', 'l']
    six = ['m', 'n', 'o']
    seven = ['p', 'q', 'r', 's']
    eight = ['t', 'u', 'v']
    nine = ['w', 'x', 'y', 'z']
    possible_words = []
    for i in range(len(sequences)):  # iterate for each sequenes inputed
        possible_words = []
        for digit in sequences[i]:  # iterate on each number in the sequences
            if digit == '2':
                possible_words.append(two)
            if digit == '3':
                possible_words.append(three)
            if digit == '4':
                possible_words.append(four)
            if digit == '5':
                possible_words.append(five)
            if digit == '6':
                possible_words.append(six)
            if digit == '7':
                possible_words.append(seven)
            if digit == '8':
                possible_words.append(eight)
            if digit == '9':
                possible_words.append(nine)

        # create the possible combos
        combos =[]
        for j in range(len(possible_words)+1):
            for subset in permutations(possible_words, j+1):
                if subset[0] == possible_words[0]:
                    combos.append((list(product(*subset))))
        search_in(combos, dictionary)

def main():
    """ Main function to read input and print output """
    N = int(stdin.readline())  # The number of words
    dictionary = []
    data = []
    for i in range(N):
        data = stdin.readline().replace('\n', '').replace('\r', '')
        dictionary.append(data.split(' '))
    M = int(stdin.readline())  # number of sequences
    sequences = []
    for j in range(M):
        sequences.append(stdin.readline().replace('\n', '').replace('\r', ''))

    decode(dictionary, sequences)

main()
