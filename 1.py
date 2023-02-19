from pprint import pprint
from random import randint

text_name = 'pushkin123.txt'
stat = {}
# stat = {'a':{'t': 2, 'u': 4}, 'b':{'t': 2, 'u': 4}}
sequence = '    '
with open(text_name, mode='r', encoding='utf8') as file:
    for line in file:
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char

pprint(stat)
totals = {}
stat_for_generation = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generation[sequence] = []
    for chars, count in char_stat.items():
        totals[sequence] += count
        stat_for_generation[sequence].append([count, chars])
    stat_for_generation[sequence].sort()
    stat_for_generation[sequence].reverse()

# pprint(stat_for_generation)
number_of_chars = 500
counter = 0
sequence = '    '
while counter <= number_of_chars:
    char_stat = stat_for_generation[sequence]
    pos = 0
    dice = randint(1, totals[sequence])
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    sequence = sequence[1:] + char
    counter += 1
