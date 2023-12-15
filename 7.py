#lang python
import collections
file = 'input/input7.txt'
f = [i.strip().split() for i in open(file).readlines()]

def run(part):
	cards = collections.defaultdict(list)
	strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	strength.reverse()
	for hand in f:
		freq_map = collections.defaultdict(int)

		for i in range(len(hand[0])):
			freq_map[hand[0][i]] += 1

		if part == 2:
			strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
			strength.reverse()
			jokers = freq_map['J']
			del freq_map['J']
			if freq_map:
				biggest = max(freq_map, key=freq_map.get)
				freq_map[biggest] += jokers
			else:
				freq_map['A'] = jokers

		match(sorted(freq_map.values())):
			case [5]:
				cards[6].append(hand)
			case [1, 4]:
				cards[5].append(hand)
			case [2, 3]:
				cards[4].append(hand)
			case [1, 1, 3]:
				cards[3].append(hand)
			case [1, 2, 2]:
				cards[2].append(hand)
			case [1, 1, 1, 2]:
				cards[1].append(hand)
			case _:
				cards[0].append(hand)

	total = []
	for i in range(6, -1, -1):
		card = cards[i]
		if card:
			card = sorted(card, key=lambda word: [strength.index(c) for c in word[0]], reverse = True)
			for i in card:
				total.insert(0, i[1])

	newtot = 0
	for i in range(len(total)):
		newtot += int(total[i]) * (i+1)
	return newtot
print("silver: ", run(1))
print("gold: ",run(2))