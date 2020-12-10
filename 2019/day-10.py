with open('input-10.txt') as f:
	input = f.read().splitlines()

import itertools
import math

W = len(input[0])
H = len(input)

def asteroids():
	for x, y in itertools.product(range(W), range(H)):
		if input[y][x] == '#':
			yield (x, y)

def cansee(base, target):
	dx = target[0]-base[0]
	dy = target[1]-base[1]
	gcd = math.gcd(dx, dy)
	if gcd == 1:
		return True
	dx = dx//gcd
	dy = dy//gcd

	x = base[0]+dx
	y = base[1]+dy

	while x!=target[0] or y!=target[1]:
		if input[y][x] == '#':
			return False
		x += dx
		y += dy
	return True

def spot(base):
	n = 0
	for a in asteroids():
		if a == base:
			continue
		if cansee(base, a):
			n += 1
	return n

see = { a: spot(a) for a in asteroids() }
print(see[max(see, key=lambda a: see[a])])
