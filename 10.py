#lang python
file = 'input/input10.txt'
example = 'input/example10.txt'
f = [i.strip() for i in open(file).readlines()]
import collections
north = (-1, 0)
south = (1, 0)
east = (0, 1)
west = (0, -1)
counterparts = {north:south, east:west, west:east, south:north}

pieces = {'S':[north, south, east, west], '|': [north, south], '-': [east, west],\
		  'L': [north, east], 'J': [north, west], '7': [south, west],'F':[south, east]}

history = []
speedy_dict = collections.defaultdict(tuple)
def is_valid_move(x2, y2, move):
	piece2 = f[x2][y2]
	return counterparts[move] in pieces[piece2]

for i in range(len(f)):
	for j in range(len(f[0])):
		if f[i][j] == 'S':
			history.append((i, j))
			break

def silver():
	while True:
		curr_x, curr_y = history[-1]
		for move in pieces[f[curr_x][curr_y]]:
			new_x, new_y = curr_x + move[0], curr_y + move[1]
			if new_x < 0 or new_x >= len(f) or new_y < 0 or new_y >= len(f[0]) or f[new_x][new_y] not in pieces:
				continue
			if (new_x, new_y) == history[0] and len(history) > 2: 
				return len(history)//2
			if (new_x, new_y) not in history and is_valid_move(new_x, new_y, move):
				history.append((new_x, new_y))
				speedy_dict[(new_x, new_y)] = True
				break



print(f"silver: {silver()}")

# import solution lmao, would be nice to actually figure out how to do this
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

counter = 0
poly = Polygon(history)
for x in range(len(f)):
	for y in range(len(f[0])):
		if poly.contains(Point(x,y)):
			counter += 1

print("gold: ", counter)
