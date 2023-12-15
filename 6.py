#lang python

file = 'input/input6.txt'
f = [i.strip().split() for i in open(file).readlines()]
time = list(map(int, f[0][1:]))
distance = list(map(int, f[1][1:]))

targets = 1

for i in range(len(time)):
	t = time[i]
	d = distance[i]
	target = 0
	for speed in range(t):
		timeleft = t - speed
		if timeleft * speed > d:
			target += 1

	if target:
		targets *= target

print("silver: ", targets)

time = int("".join(f[0][1:]))
distance = int("".join(f[1][1:]))

targets = 0

for speed in range(time):
	timeleft = time - speed
	if timeleft * speed > distance:
		targets += 1

print("gold: ", targets)