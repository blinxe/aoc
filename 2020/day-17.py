import itertools
import functools

with open('input-17.txt') as f:
	input = f.read().splitlines()

init = set((x,y) for y,row in enumerate(input) for x,c in enumerate(row) if c=='#')


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def getneighbors(coord):
	unit_vectors = itertools.product((0, -1, 1), repeat=NDIM)
	next(unit_vectors)
	return set(tuple(c+u for c,u in zip(coord, uv)) for uv in unit_vectors)
getneighbors = memoize(getneighbors)

def step(active):
	neighbors = set()
	for a in active:
		neighbors |= getneighbors(a)
	keep = set(a for a in active if len(getneighbors(a)&active) in [2, 3])
	add = set(n for n in neighbors-active if len(getneighbors(n)&active)==3)
	return keep | add


# Part One

NDIM = 3
active = set((i[0], i[1], 0) for i in init)
for _ in range(6):
	active = step(active)
print(len(active), flush=True)


# Part Two

NDIM = 4
active = set((i[0], i[1], 0, 0) for i in init)
for _ in range(6):
	active = step(active)
print(len(active))
