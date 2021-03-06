with open('input-06.txt') as f:
	input = f.read().split()

orbits = { b[1]: b[0] for b in [i.split(')') for i in input] }

def ancestors(b):
	while b != 'COM':
		b = orbits[b]
		yield b

# Part One
print('checksum:', sum(sum(1 for _ in ancestors(b)) for b in orbits))

# Part Two
# distYou, common = next((i, b) for i, b in enumerate(ancestors('YOU')) if b in ancestors('SAN'))
# distSan = next(i for i, b in enumerate(ancestors('SAN')) if b==common)
ancSan = list(ancestors('SAN')) # going through it many times -> prevent dict lookups
distYou, common = next((i, b) for i, b in enumerate(ancestors('YOU')) if b in ancSan)
distSan = ancSan.index(common)
print('jumps:', distYou+distSan)
