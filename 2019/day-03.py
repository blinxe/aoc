with open('input-03.txt') as f:
	input = [l[:-1].split(',') for l in f]

# Part One
def getPoints(w):
	pts = {}
	x = y = 0
	total = 0
	for m in w:
		dirs = {
			'R': (1, 0),
			'L': (-1, 0),
			'U': (0, 1),
			'D': (0, -1),
		}

		dx, dy = dirs[m[0]]
		dist = int(m[1:])

		for _ in range(dist):
			x += dx
			y += dy
			total += 1
			pts[(x, y)] = total
	return pts

p1 = getPoints(input[0])
p2 = getPoints(input[1])

p1pos = set(p1)
inter = p1pos.intersection(p2)
dist = map(lambda p: abs(p[0]) + abs(p[1]), inter)
print(min(dist))

# Part Two
sumsteps = [p1[i]+p2[i] for i in inter]
print(min(sumsteps))
