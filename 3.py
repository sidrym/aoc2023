#lang python
import collections, re

example_fname = 'input/example3.txt'
input_fname = 'input/input3.txt'
current = input_fname

symbols = []
totry = [(-1, -1), (-1, 1), (1, 1), (1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]

f = [line.strip() for line in open(current).readlines()]

# read symbols
for row, line in enumerate(f):
	for c in range(len(line)):
		if not line[c].isnumeric() and not line[c] == '.':
			symbols.append((row, c))

# part 1:
total = 0
for row, line in enumerate(f):
	c = 0
	while c < len(line):
		flag = False
		oldc = c
		while c < len(line) and line[c].isnumeric():
			for versuch in totry:
				newtry = (row + versuch[0], c + versuch[1])
				if newtry in symbols:
					flag = True
			c += 1
		if flag:
			total += int(line[oldc:c])
		c += 1
print(f"part1: {total}")

# part 2:
symbol_keys = collections.defaultdict(list)
for row, line in enumerate(f):
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

gear_ratios = sum([v[0]*v[1] for k,v in symbol_keys.items() if len(v) == 2])
print(f"part2: {gear_ratios}")
