with open('input-22.txt') as f:
	input = f.read().splitlines()

sep = input.index('')
player1 = [ int(n) for n in input[1:sep] ]
player2 = [ int(n) for n in input[sep+2:] ]


# Part One

p1 = player1.copy()
p2 = player2.copy()
turns = 0
while p1 and p2:
	turns += 1
	d1 = p1.pop(0)
	d2 = p2.pop(0)
	if d1 > d2:
		p1 += [ d1, d2 ]
	else:
		p2 += [ d2, d1 ]

if p1: winner = p1
else: winner = p2

total = 0
for i,n in enumerate(winner[::-1], start=1):
	total += i*n

print(total)


# Part Two


def recurse(p1, p2):
	previous_rounds = set()

	while p1 and p2:
		tp1 = tuple(p1)
		tp2 = tuple(p2)
		if (tp1, tp2) in previous_rounds:
			return 1
		previous_rounds.add((tp1, tp2))

		d1 = p1.pop(0)
		d2 = p2.pop(0)
		if len(p1) >= d1 and len(p2) >= d2:
			w = recurse(p1[:d1].copy(), p2[:d2].copy())
		else:
			w = 1 if d1 > d2 else 2

		if w == 1:
			p1 += [ d1, d2 ]
		else:
			p2 += [ d2, d1 ]

	if p1: return 1
	return 2


p1 = player1.copy()
p2 = player2.copy()
winner = recurse(p1, p2)
print(winner)
if winner == 1:
	winner = p1
else:
	winner = p2

total = 0
for i,n in enumerate(winner[::-1], start=1):
	total += i*n

print(total)
