with open('input-5.txt') as f:
	input = f.read().split()

# Part One
def ticketToId(t):
	row = ''.join([ '0' if l=='F' else '1' for l in t[:7] ])
	row = int(row, 2)
	col = ''.join([ '0' if l=='L' else '1' for l in t[7:] ])
	col = int(col, 2)
	return 8*row + col

ids = list(map(lambda t: ticketToId(t), input))
m = max(ids)
print(m)

# Part Two
for r in range(m):
	if r not in ids:
		print(r)
