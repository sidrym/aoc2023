#lang python
file = 'input/bigboy.txt'
hits = [len(set(line[0]).intersection(line[1])) \
		for line in [[i.split() for i in line.split(": ")[1].split('|')] \
		for line in open(file).readlines()]]

silver, gold = 0, 0
cardsleft = [1 for i in range(len(hits) + 1)]

for row, hit in enumerate(hits, 1):
	silver += 2**(hit-1) if hit > 0 else 0
	gold += cardsleft[row]
	for i in range(row+1, row+hit+1):
		cardsleft[i] += cardsleft[row]

print("silver:", silver
)print("gold:", gold)
