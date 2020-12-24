with open('input-24.txt') as f:
	input = f.read().splitlines()

DIR = {
	'e': (1, 0),
	'w': (-1, 0),
	'ne': (0, 1),
	'nw': (-1, 1),
	'se': (1, -1),
	'sw': (0, -1),
}

lines = []
for l in input:
	line = []
	i = 0
	while i < len(l):
		if l[i] in DIR:
			line.append(l[i])
			i += 1
		else:
			line.append(l[i]+l[i+1])
			i += 2
	lines.append(line)


# Part One

blacks = set()

for l in lines:
	tx,ty = 0,0
	for d in l:
		dx,dy = DIR[d]
		tx += dx
		ty += dy
	if (tx,ty) in blacks:
		blacks.remove((tx,ty))
	else:
		blacks.add((tx, ty))

print(len(blacks))
print()


# Part Two

def getneighbors(t):
	tx,ty = t
	return set((tx+d[0], ty+d[1]) for d in DIR.values())

for _ in range(100):
	white_neighbors = set()
	for t in blacks:
		white_neighbors |= getneighbors(t)
	white_neighbors -= blacks

	new_blacks = set(t for t in white_neighbors if len(getneighbors(t) & blacks) == 2)
	remaining_blacks = set(t for t in blacks if len(getneighbors(t) & blacks) in [1, 2])
	blacks = new_blacks | remaining_blacks

print(len(blacks))
