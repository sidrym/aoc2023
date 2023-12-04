#lang python
import collections
file = 'input/bigboy.txt'
hits = [len(set(line[0]).intersection(line[1])) \
		for line in [[i.split() for i in line.split(": ")[1].split('|')] \
		for line in open(file).readlines()]]

silver, gold = 0, 0
cardsleft = [1 for i in range(len(hits) + 1)]

for row, hit in enumerate(hits, 1):
	# silver:
	answer = 0
	for i in range(hit):
		answer = answer*2 if answer else 1

	silver += answer

	# gold:
	gold += cardsleft[row]
	for i in range(row+1, row+hit+1):
		cardsleft[i] += cardsleft[row]

print("silver:", silver)
print("gold:", gold)
