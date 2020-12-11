import functools

with open('input-03.txt') as f:
	input = [l[:-1] for l in f]

def slope(h, v):
	trees = 0
	off = 0
	for l in input[::v]:
		if l[off] == '#': trees += 1
		off = (off + h) % len(l)
	return trees

# Part One
trees = 0
off = 0
for l in input:
	if l[off] == '#': trees += 1
	off = (off + 3) % len(l)
print(trees)

# Part Two
slopes = [
	(1, 1),
	(3, 1),
	(5, 1),
	(7, 1),
	(1, 2),
]
t = {s: slope(*s) for s in slopes}

res = functools.reduce(lambda acc,s: acc*t[s], t, 1)
print(res)
