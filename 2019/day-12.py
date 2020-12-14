pos = [
	[6, -2, -7],
	[-6, -7, -4],
	[-9, 11, 0],
	[-3, -4, 6],
]

vel = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
]


# Part One

from itertools import combinations

def sign(x):
	if x > 0: return 1
	if x < 0: return -1
	return 0

def apply_gravity():
	for m1, m2 in combinations(range(4), 2):
		if m1 == m2: continue
		p1 = pos[m1]
		p2 = pos[m2]
		dv = [ sign(x2-x1) for x1,x2 in zip(pos[m1], pos[m2]) ]
		vel[m1] = [ v+d for v,d in zip(vel[m1], dv) ]
		vel[m2] = [ v-d for v,d in zip(vel[m2], dv) ]

def apply_velocity():
	for m in range(4):
		pos[m] = [ x+v for x,v in zip(pos[m], vel[m]) ]

for _ in range(1000):
	apply_gravity()
	apply_velocity()
	print(pos)
	print(vel)


pot = [ abs(p[0]) + abs(p[1]) + abs(p[2]) for p in pos ]
kin = [ abs(v[0]) + abs(v[1]) + abs(v[2]) for v in vel ]

total = sum(p*k for p,k in zip(pot, kin))
print(total)
