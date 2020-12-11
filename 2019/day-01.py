with open('input-01.txt') as f:
	input = f.read().split()
input = map(int, input)

# Part One
fuel = [ x//3-2 for x in input ]
print(sum(fuel))

# Part Two
def rocketeq(fuel):
	more = fuel
	while more > 0:
		more = more//3-2
		if more > 0:
			fuel += more
	return fuel

print(sum(rocketeq(f) for f in fuel))
