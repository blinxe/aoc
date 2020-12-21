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

def getborders(tile):
	td = tiles[tile]
	return [
		td[0],
		''.join(row[-1] for row in td),
		td[-1][::-1],
		''.join(row[0] for row in td)[::-1],
	]

borders = { t: getborders(t) for t in tiles }

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

def flip(tile):
	tiles[tile] = tiles[tile][::-1]
	t,r,d,l = neighbors[tile]
	neighbors[tile] = [d,r,t,l]

def rotate_left(tile, times=1):
	for _ in range(times%4):
		tiles[tile] = [
			''.join([ row[-i-1] for row in tiles[tile] ])
			for i,_ in enumerate(tiles[tile])
		]
		t,r,d,l = neighbors[tile]
		neighbors[tile] = [r,d,l,t]

def align_neighbor(ref, side):
	n = neighbors[ref][side]
	if n is None: return
	bref = getborders(ref)[side]
	rbref = bref[::-1]

	if any(bref == bn for bn in getborders(n)):
		flip(n)

	bn = getborders(n)
	for i in range(4):
		if bn[i] == rbref:
			turns = (4 + i - (side+2)) % 4
			rotate_left(n, turns)

def ptile(t):
	for r in tiles[t]:
		print(r)
	print()

topleft = [ c for c in corners if neighbors[c][0]==neighbors[c][3]==None ][0]

pic = []
curs_row = topleft
while curs_row is not None:
	curs_col = curs_row
	pic_data = [ '' for row in tiles[curs_col][1:-1] ]

	while curs_col != None:
		for i,row in enumerate(tiles[curs_col][1:-1]):
			pic_data[i] += row[1:-1]
		align_neighbor(curs_col, 1)
		curs_col = neighbors[curs_col][1]

	pic += pic_data
	align_neighbor(curs_row, 2)
	curs_row = neighbors[curs_row][2]


# for row in pic:
# 	print(row)

monster = [
	'                  # ',
	'#    ##    ##    ###',
	' #  #  #  #  #  #   ',
]

def look_for_monster(roff, coff):
	for r,row in enumerate(monster):
		for c,sym in enumerate(row):
			if sym=='#' and pic[roff+r][coff+c] != '#':
				return 0
	return 1

found = 0
for i in range(4):
	for r,row in enumerate(pic[:-2]):
		for c,sym in enumerate(row[:-19]):
			found += look_for_monster(r, c)
	if found != 0:
		break
	# rotate
	pic = [
		''.join([ row[i] for row in pic[::-1] ])
		for i,_ in enumerate(pic)
	]

if found == 0:
	# flip
	pic = pic[::-1]
	for i in range(4):
		for r,row in enumerate(pic[:-2]):
			for c,sym in enumerate(row[:-19]):
				found += look_for_monster(r, c)
		if found != 0:
			break
		# rotate
		pic = [
			''.join([ row[i] for row in pic[::-1] ])
			for i,_ in enumerate(pic)
		]

monster_count = sum(row.count('#') for row in monster)
habitat_count = sum(row.count('#') for row in pic)
print(habitat_count - found*monster_count)
