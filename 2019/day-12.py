# sample
# pos = [
# 	[-1, 0, 2],
# 	[2, -10, -7],
# 	[4, -8, 8],
# 	[3, 5, -1],
# ]

from itertools import combinations

def sign(x):
	if x > 0: return 1
	if x < 0: return -1
	return 0

def apply_gravity():
	for m1, m2 in combinations(range(len(pos)), 2):
		if m1 == m2: continue
		p1 = pos[m1]
		p2 = pos[m2]
		dv = [ sign(x2-x1) for x1,x2 in zip(pos[m1], pos[m2]) ]
		vel[m1] = [ v+d for v,d in zip(vel[m1], dv) ]
		vel[m2] = [ v-d for v,d in zip(vel[m2], dv) ]

def apply_velocity():
	for m in range(len(pos)):
		pos[m] = [ x+v for x,v in zip(pos[m], vel[m]) ]


# Part One

pos = [
	[6, -2, -7],
	[-6, -7, -4],
	[-9, 11, 0],
	[-3, -4, 6],
]

vel = [ [ 0 for _ in p ] for p in pos ]

for _ in range(1000):
	apply_gravity()
	apply_velocity()

pot = [ sum(abs(c) for c in p) for p in pos ]
kin = [ sum(abs(c) for c in v) for v in vel ]

print(sum(p*k for p,k in zip(pot, kin)))


# Part Two

initial = [
	[6, -2, -7],
	[-6, -7, -4],
	[-9, 11, 0],
	[-3, -4, 6],
]

from copy import deepcopy
from math import gcd

def lcm(a, b):
	return a*b // gcd(a, b)

steps = 1
for dim in range(len(initial[0])):
	n=0
	pos = [ [p[dim]] for p in initial ]
	vel = [ [ 0 for _ in p ] for p in pos ]
	ref = (deepcopy(pos), deepcopy(vel))
	print(pos, flush=True)
	while True:
		n += 1
		apply_gravity()
		apply_velocity()
		if (pos, vel) == ref:
			print(n, 'steps')
			break
	steps = lcm(steps, n)
print(steps)
