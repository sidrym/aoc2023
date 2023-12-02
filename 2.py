#lang python
import collections

with open("input/input2.txt") as f:
	game = {"red": 12, "green": 13, "blue": 14}
	total = 0
	i = 0
	for line in f:
		i += 1
		line = line.strip().split(" ", 2)[2].replace(':', '').split('; ')
		error = 0
		while line:
			group = line.pop(0).split(', ')
			while group:
				newgroup = group.pop().split()
				amount = int(newgroup[0])
				color = newgroup[1]
				if game[color] < amount:
					error = 1
		if not error:
			total += i
	print(f"part 1: {total}")

with open("input/input2.txt") as f:
	total = 0
	for line in f:
		line = line.strip().split(" ", 2)[2].replace(':', '').split('; ')
		mindict = collections.defaultdict(lambda: float('-inf'))
		while line:
			group = line.pop(0).split(', ')
			while group:
				newgroup = group.pop().split()
				amount = int(newgroup[0])
				color = newgroup[1]
				mindict[color] = max(mindict[color], amount)
		result = 1
		for i in mindict.values():
			result *= i
		total += result
	print(f"part 2: {total}")
