#lang python
file = 'input/input11.txt'
example = 'input/example11.txt'
f = [list(i.strip()) for i in open(file).readlines()]

def expansion(f, n):
	# rows
	i = 0
	while i < len(f):
		if '#' not in f[i]:
			f.insert(i, ['*'] * len(f[0] * n))
			i += 2
		else:
			i += 1

	# cols
	j = 0
	while j < len(f[0]):
		if '#' not in [f[i][j] for i in range(len(f))]:
			for i in range(len(f)):
				f[i].insert(j, '.')
			j += 2
		else:
			j += 1
	return f


def get_coords(f):
	coords = []
	for i in range(len(f)):
		for j in range(len(f[0])):
			if f[i][j] == '#':
				coords.append((i,j))
	return coords

def solve(f, n):
	f = expansion(f, n)
	coords = get_coords(f)

	counter = 0
	for i in range(len(coords)):
		for j in range(i, len(coords)):
			if i != j:
				counter += abs(coords[i][0] - coords[j][0]) + abs(coords[i][1]-coords[j][1])
	return counter

print("silver: ", solve(f, 2))
#print("gold: ", solve(f, 1000000))
