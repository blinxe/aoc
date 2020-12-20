with open('input-20.txt') as f:
	input = f.read().splitlines()

tiles = {}
tdata = []
for l in input:
	if l.startswith('Tile '):
		t = int(l[5:-1])
	elif l == '':
		tiles[t] = tdata
		tdata = []
	else:
		tdata.append(l)
tiles[t] = tdata


# Part One

borders = {
	t: [
		td[0],
		''.join(row[-1] for row in td),
		td[-1],
		''.join(row[0] for row in td),
	]
	for t,td in tiles.items()
}

def getneighbor(ref, side):
	bref = borders[ref][side]
	rbref = bref[::-1]
	for t,b in borders.items():
		if t == ref: continue
		if any(bref==b[i] or rbref==b[i] for i in range(4)):
			return t
	return None

neighbors = {
	t: [ getneighbor(t, side) for side in range(4) ]
	for t in tiles
}

corners = [ t for t,n in neighbors.items() if sum(1 for s in n if s) == 2 ]
import functools
print(functools.reduce(lambda p,c: p*c, corners))


# Part Two
