""" Collating Sequence """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE 2050, Fall 2019

from sys import (stdin, stdout)

DATA = []
for line in stdin:
    DATA.append(line.replace('\n', ''))

alpha = []
size = len(DATA) - 1
for index in range(size):
        word1 = DATA[index]
        word2 = DATA[index+1]
        #print('word1 and word2', word1, word2)
        min_size = min(len(word1), len(word2))
        #loops for each letter
        for cur in range(min_size):
            # stops at first difference and adds it to alpha in not already in
            if word1[cur] != word2[cur]:
              #  print(word1[cur],word2[cur])
                if [word1[cur],word2[cur]] not in alpha:
                    alpha.append([word1[cur],word2[cur]])
                break

stdout.write('{}'.format("".join(alpha)))
