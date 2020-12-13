import math

with open('input-13.txt') as f:
	input = f.read().splitlines()
buses = [ int(b) for b in input[1].split(',') if b != 'x' ]

# Part One
ready = int(input[0])
closest = [ (b, b*math.ceil(ready/b)) for b in buses ]
best = min(closest, key=lambda b: b[1]-ready)
print(best[0] * (best[1]-ready))

# Part Two
shift = { int(b):e for e,b in enumerate(input[1].split(',')) if b != 'x' }
def nextok(b, time, step):
	while (time+shift[b]) % b != 0:
		time += step
	return time

t = 0
step = 1
for b in buses:
	t = nextok(b, t, step) # next (first for primes) ok timestamp for buses up to b
	step *= b # time gap (minimal for primes) to next ok timestamp for buses up to b
print(t)
