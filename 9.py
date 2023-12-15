#lang python
# day 9
file = 'input/input9.txt'
example = 'input/example9.txt'
f = [i.strip() for i in open(file).readlines()]
import numpy as np

def predict_next_term(sequence):
	ll = [sequence]
	# bubble up
	while any([x!=0 for x in ll[-1]]):
		newlist = []
		for i in range(1, len(ll[-1])):
			newlist.append(ll[-1][i] - ll[-1][i-1])
		ll.append(newlist)

	# bubble down
	ll[-1].append(0)
	ll.reverse()
	for i in range(1, len(ll)):
		ll[i].append(ll[i][-1] + ll[i-1][-1])

	return(ll[-1][-1])

part1 = 0
part2 = 0
for line in f:
	line = list(map(int, line.strip().split()))
	part1 += predict_next_term(line)
	line.reverse()
	part2 += predict_next_term(line)
print(f'silver: {part1}')
print(f'gold: {part2}')

