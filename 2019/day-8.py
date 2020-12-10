with open('input-8.txt') as f:
	input = [int(c) for c in f.read()]

W = 25
H = 6
layers = [ input[i:i+W*H] for i in range(0, len(input), W*H) ]

# Part One
# zeroes, ones, twos
zot = [ (l.count(0), l.count(1), l.count(2)) for l in layers ]
m = min(zot, key=lambda x: x[0])
print(m[1]*m[2])

# Part Two
from functools import reduce
pic = [ reduce(lambda f,b: b if f==2 else f, pixels)
	for pixels in zip(*layers) ]

pic = ['#' if p==1 else ' ' for p in pic]
rows = [ pic[i:i+W] for i in range(0, W*H, W) ]
for row in rows:
	print(*row, sep='')
