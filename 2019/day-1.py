with open('input-1.txt') as f:
	input = f.read().split()
input = map(int, input)

# Part One
fuel = list(map(lambda x: x//3-2, input))
print(sum(fuel))

# Part Two
def rocketeq(fuel):
	more = fuel
	while more > 0:
		more = more//3-2
		if more > 0:
			fuel += more
	return fuel

more = map(rocketeq, fuel)
print(sum(more))
