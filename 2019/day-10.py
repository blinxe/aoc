with open('input-10.txt') as f:
	input = f.read().splitlines()

import itertools
import math

W = len(input[0])
H = len(input)

# Part One

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
base = max(see, key=lambda a: see[a])
print(base, see[base])


# Part Two
mandist = [ (a, abs(a[0]-base[0]) + abs(a[1]-base[1])) for a in asteroids() ]
mandist.sort(key = lambda a: a[1])

def getangle(base, a):
	x = a[0] - base[0]
	y = a[1] - base[1]
	angle = 180.0 + math.atan2(-x, y)*180/math.pi
	if angle >= 360.0:
		angle -= 360.0
	return angle

angles = [ (a[0], getangle(base, a[0]), a[1]) for a in mandist[1:] ]
angles.sort(key = lambda a: a[1])

nth = 0
while angles:
	remain = []
	i = 0
	while i<len(angles):
		nth += 1
		if nth == 200:
			print(angles[i][0])
		a = angles[i][1]
		i += 1
		while i<len(angles) and angles[i][1] == a:
			remain.append(angles[i])
			i += 1
	angles = remain
