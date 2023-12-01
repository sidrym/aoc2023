#lang python

with open("input1.txt") as f:
	result = 0
	for line in f:
		temp = []
		for i in range(len(line)):
			if line[i].isnumeric():
				temp.append(line[i])
		result += int(temp[0]+temp[-1])
	print(f"part 1: {result}")


nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("input1.txt") as f:
	result = 0
	for line in f:
		temp = []
		for i in range(len(line)):
			if line[i].isnumeric():
				temp.append(line[i])
			else:
				for j in range(3, 5):
					if line[i:i+j] in nums:
						temp.append(str(nums.index(line[i:i+j])+1))
		result += int(temp[0]+temp[-1])

	print(f"part 2: {result}")
