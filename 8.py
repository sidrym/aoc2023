#lang python
import collections
file = 'input/input8.txt'
example = 'input/example8.txt'
f = [i.strip() for i in open(file).readlines()]
key = f.pop(0)

f.pop(0)
first = f[0][0:3]
table = collections.defaultdict()
nodes = []
for line in f:
	newkey = line[0:3]
	left = line[7:10]
	right = line[12:15]
	table[newkey] = (left, right)
	if newkey[-1] == 'A':
		nodes.append(newkey)

current = 'AAA'
counter = 0
while current != 'ZZZ':
	for c in key:
		counter += 1
		if c == 'R':
			current = table[current][1]
		else:
			current = table[current][0]
		if current == 'ZZZ':
			break

print("silver", counter)

f = [i.strip() for i in open(file).readlines()]
key = f.pop(0)

f.pop(0)
first = f[0][0:3]
table = collections.defaultdict()
nodes = []
for line in f:
	newkey = line[0:3]
	left = line[7:10]
	right = line[12:15]
	table[newkey] = (left, right)
	if newkey[-1] == 'A':
		nodes.append(newkey)
counter = 0

answers = []
for i in range(len(nodes)):
	counter = 0
	while True:
		for c in key:
			counter += 1
			direction = 0
			if c == 'R':
				direction = 1
			nodes[i] = table[nodes[i]][direction]
			if nodes[i][2] == 'Z':
				answers.append(counter)
				counter = -1
		if counter == -1:
			break

import math
print("gold", math.lcm(*answers))

