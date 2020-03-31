""" Project: S&P500 """
# Author: Erika Ambrioso, eambrioso2017@my.fit.edu
# Course: CSE2050, Fall 2019

from sys import(stdin, stdout)
from datetime import *

def format_date(date):
    """ formats the date how we'd like to print it """
    dt = datetime.strptime(date, "%Y-%m-%d")
    # print('proper date format: ', dt.strftime('%a, %d %b %Y'))
    output = dt.strftime('%a, %d %b %Y')
    return output

def find_streak(gains_list, date_list):
    """ Returns the longest growth streak """
    streak = ['', '',  0]
    for i in range(len(gains_list)):
        if gains_list[i] > 0:
            location = i
            streak[0] = date_list[location]
    # calcualte the difference in days of the start and end date
        if gains_list[i] > 0:
            streak[2] += 1
            streak[1] = date_list[i+1]
    return streak

# Read in the data
DATA = []
for line in stdin:
    DATA.append(line.replace('\n', ''))
# Parse the data
data_list = [DATA[i].split(',') for i in range(len(DATA))]
date_list = [data_list[i][0] for i in range(1, len(DATA))]
close_list = [float(data_list[i][5]) for i in range(1, len(DATA))]      #ASK about the 2

# Create a list of percent gains for each daily pair.
# Find the maximum and minimum of each list.
gains_list = []
for i in range(1, len(close_list)):
    gains_list.append(100.0 * (close_list[i] - close_list[i - 1]) / close_list[i - 1])

# Use list of gains to find the longest growth strength:  streak_length
max_gain = max(gains_list)
max_loss = min(gains_list)
# find the index of the max gain and loss from the gains list
for i in range(len(gains_list)):
    if gains_list[i] == max_gain:
        max_gain_loc = i + 1
    if gains_list[i] == max_loss:
        max_loss_loc = i + 1

DATE1 = format_date(date_list[max_gain_loc])
DATE2 = format_date(date_list[max_loss_loc])
STREAK = find_streak(gains_list, date_list)
streak_length = STREAK[2]
date3 = format_date(STREAK[0])
date4 = format_date(STREAK[1])

stdout.write('Max gain: {0:5.2f}% on '.format(max_gain))
stdout.write('{}\n'.format(DATE1))
stdout.write('Max loss: {0:5.2f}% on '.format(max_loss))
stdout.write('{}\n'.format(DATE2))
stdout.write('Longest growth streak: {} days ({} to {})'.format(streak_length, date3, date4))
