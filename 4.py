#lang python
import collections, re
example_fname = 'input/example4.txt'
input_fname = 'input/input4.txt'

USE_EXAMPLE = False

file = example_fname if USE_EXAMPLE else input_fname
f = [line.strip() for line in open(file).readlines()]
total = 0
for line in f:
	line = line.split(": ")[1].split('|')
	card = [int(i) for i in line[0].strip().split(' ') if i != '']
	card2 = [int(i) for i in line[1].strip().split(' ') if i != '']
	answer = 0
	for i in card:
		if i in card2:
			if answer == 0:
				answer = 1
			else:
				answer *= 2

	total += answer
print("part1: ", total)

cardsleft = collections.defaultdict(int)
for i in range(1, len(f)+1):
	cardsleft[i] = 1
grand_total = 0

for row, line in enumerate(f):
	row += 1
	line = line.split(": ")[1].split('|')
	card = [int(i) for i in line[0].strip().split(' ') if i != '']
	card2 = [int(i) for i in line[1].strip().split(' ') if i != '']
	hits = 0
	for i in card:
		if i in card2:
			hits += 1
	for copies in range(cardsleft[row]):
		for i in range(row+1, row+hits+1):
			cardsleft[i] += 1

print("part2: ", sum(cardsleft.values()))
