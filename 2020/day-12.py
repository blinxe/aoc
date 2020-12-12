with open('input-12.txt') as f:
	input = [ (l[0], int(l[1:])) for l in f.read().splitlines() ]


# Part One

dir = {
	0:   'E',
	90:  'S',
	180: 'W',
	270: 'N',
}

def move(st, m):
	d = m[0]
	n = m[1]

	if d == 'N': st[1] += n
	elif d == 'S': st[1] -= n
	elif d == 'E': st[0] += n
	elif d == 'W': st[0] -= n
	elif d == 'L': st[2] = (st[2]+3*n) % 360
	elif d == 'R': st[2] = (st[2]+n) % 360
	elif d == 'F': move(st, (dir[st[2]], n))

# x, y, dir
state = [0, 0, 0]

for i in input:
	move(state, i)

print(state)
print(abs(state[0]) + abs(state[1]))


# Part Two

def move(st, m):
	d = m[0]
	n = m[1]

	if d == 'N': st[1] += n
	elif d == 'S': st[1] -= n
	elif d == 'E': st[0] += n
	elif d == 'W': st[0] -= n

	elif d == 'L':
		for l in range(n//90):
			dx = -(st[1]-st[3])
			dy = st[0]-st[2]
			st[0] = st[2] + dx
			st[1] = st[3] + dy

	elif d == 'R':
		for r in range(n//90):
			dx = st[1]-st[3]
			dy = -(st[0]-st[2])
			st[0] = st[2] + dx
			st[1] = st[3] + dy

	elif d == 'F':
		dx = n * (st[0]-st[2])
		dy = n * (st[1]-st[3])
		st[0] += dx
		st[1] += dy
		st[2] += dx
		st[3] += dy

# [ wp-x, wp-y, ship-x, ship-y ]
state = [10, 1, 0, 0]

for i in input:
	move(state, i)

print(state)
print(abs(state[2]) + abs(state[3]))
