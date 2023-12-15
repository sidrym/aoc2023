#lang python
import collections
file = 'input/input5.txt'
example = 'input/example5.txt'
f = [i.strip() for i in open(file).readlines()]
seeds = [int(i) for i in f.pop(0).split()[1:]]
f.pop(0)

while f:
	ranges = []
	key = f.pop(0).split()[0]
	while f and f[0] != '':
		readin = [int(i) for i in f.pop(0).split()]
		dest, source, rang = readin
		ranges += [(range(source, source+rang), source, dest, rang)]
	if f:
		f.pop(0)
	for i in range(len(seeds)):
		flag = False
		for rang in ranges:
			if flag:
				break
			r, source, dest, rang = rang
			if seeds[i] in r:
				seeds[i] = seeds[i]-source+dest
				flag = True

print("silver", min(seeds))


#lang python
import collections
f = [i.strip() for i in open(file).readlines()]
seeds = [int(i) for i in f.pop(0).split()[1:]]
newseeds = []
while seeds:
	hi = seeds.pop(0)
	rang = seeds.pop(0)
	newseeds.append((hi, hi+rang))
seeds = newseeds

f.pop(0)
while f:
	ranges = []
	key = f.pop(0).split()[0]
	while f and f[0] != '':
		ranges.append([int(i) for i in f.pop(0).split()])
	if f:
		f.pop(0)
	new = []

	while seeds:
		start, end = seeds.pop()
		for x,y,z in ranges:
			overlap_start = max(start, y)
			overlap_end = min(end, y + z)
			if overlap_start < overlap_end:
				new.append((overlap_start - y + x, overlap_end - y + x))
				if overlap_start > start:
					seeds.append((start, overlap_start))
				if end > overlap_end:
					seeds.append((overlap_end, end))
				break
		else:
			new.append((start, end))
	seeds = new
print("gold", min(seeds)[0])
