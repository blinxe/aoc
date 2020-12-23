# input = '952316487'
input = '389125467'

cups = [ int(c) for c in input ]


def shuffle(cups):
	global index
	insert = cups[index]-1
	if insert == 0:
		insert = 9

	if index+4 <= len(cups):
		pick = cups[index+1:index+4]
		cups = cups[:index+1] + cups[index+4:]
	else:
		pick = cups[index+1:]
		n = 3 - len(pick)
		pick += cups[:n]
		cups = cups[n:index+1]
		index -= n

	while insert in pick:
		insert -= 1
		if insert == 0:
			insert = 9

	insert = cups.index(insert) + 1
	cups = cups[:insert] + pick + cups[insert:]
	if insert <= index:
		index += 3
	index = (index+1) % len(cups)
	return cups


# Part One

index = 0
for _ in range(100):
	cups = shuffle(cups)

print(cups)
one = cups.index(1)
print(''.join(str(i) for i in cups[one+1:] + cups[:one]))


# Part Two

cups = [ int(c) for c in input ] + list(range(10, 1_000_001))

index = 0
for i in range(10_000_000):
	if (i % 1_000) == 0: print(i, flush=True)
	cups = shuffle(cups)

print(cups)
one = cups.index(1)
print(cups[one+1], cups[one+2])
