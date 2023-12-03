#lang python
import re

symbols = []
example_fname = 'input/example3.txt'
input_fname = 'input/input3.txt'
current = input_fname

# part 1:
with open(current) as f:
	i = 0
	for line in f:
		line = line.strip()
		for c in range(len(line)):
			if not line[c].isnumeric() and not line[c] == '.':
				symbols.append((i, c))
		i += 1

total = 0
totry = [(-1, -1), (-1, 1), (1, 1), (1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]
with open(current) as f:
	row = 0
	for line in f:
		line = line.strip()
		c = 0
		while c < len(line):
			flag = False
			oldc = c
			while c < len(line) and line[c].isnumeric() and c < len(line):
				for versuch in totry:
					newtry = (row + versuch[0], c + versuch[1])
					if newtry in symbols:
						flag = True
				c += 1
			if flag:
				total += int(line[oldc:c])
			c += 1
		row += 1
print(f"part1: {total}")


# part 2:
with open(current) as f:
	i = 0
	for line in f:
		line = line.strip()
		for c in range(len(line)):
			if line[c] == '*':
				symbols.append((i, c))
		i += 1

import collections
total = 0
totry = [(-1, -1), (-1, 1), (1, 1), (1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]
with open(current) as f:
	symbol_keys = collections.defaultdict(list)
	row = 0
	for line in f:
		line = line.strip()
		c = 0
		while c < len(line):
			flag = False
			oldc = c
			while c < len(line) and line[c].isnumeric():
				for versuch in totry:
					newtry = (row + versuch[0], c + versuch[1])
					if newtry in symbols:
						flag = newtry
						break
				c += 1
			if flag:
				symbol_keys[flag].append(int(line[oldc:c]))
			c += 1
		row += 1

gear_ratios = sum([v[0]*v[1] for k,v in symbol_keys.items() if len(v) == 2])
print(f"part2: {gear_ratios}")
