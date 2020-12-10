with open('input-10.txt') as f:
	input = [int(s) for s in f.read().split()]

adapters = sorted(input)
device = adapters[-1] + 3
full = [0] + adapters + [device]

# Part One
diff = [ full[i]-full[i-1] for i in range(1, len(full)) ]
d1 = diff.count(1)
d3 = diff.count(3)
print(d1, d3, d1*d3)

# Part Two
okNext = { a: [n for n in range(a+1, a+4) if n in full] for a in full }
okChainNb = { device: 1 }
for adapter in full[-2::-1]:
	okChainNb[adapter] = sum(okChainNb[a] for a in okNext[adapter])
print(okChainNb[0])
