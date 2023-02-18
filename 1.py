from pprint import pprint

text_name = 'pushkin123.txt'
stat = {}
# stat = {'a':{'t': 2, 'u': 4}, 'b':{'t': 2, 'u': 4}}
prev_char = ' '
with open(text_name, mode='r', encoding='utf8') as file:
    for line in file:
        for char in line:
            if prev_char in stat:
                if char in stat[prev_char]:
                    stat[prev_char][char] += 1
                else:
                    stat[prev_char][char] = 1
            else:
                stat[prev_char] = {char: 1}
            prev_char = char

# pprint(stat)
totals = {}
stat_for_generation = {}
for prev_char, char_stat in stat.items():
    totals[prev_char] = 0
    stat_for_generation[prev_char] = []
    for chars, count in char_stat.items():
        totals[prev_char] += count
        stat_for_generation[prev_char].append([count, chars])
    stat_for_generation[prev_char].sort()
    stat_for_generation[prev_char].reverse()
