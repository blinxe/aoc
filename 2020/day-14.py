from collections import defaultdict
import re

with open('input-14.txt') as f:
	input = f.read().splitlines()


# Part One

def applymask(mask, n):
	ones = ''.join('1' if c=='X' else c for c in mask)
	zeroes = ''.join('0' if c=='X' else c for c in mask)
	ones = int(ones, 2)
	zeroes = int(zeroes, 2)
	return n & ones | zeroes

mem = defaultdict(lambda: 0)
for l in input:
	if l.startswith('mask = '):
		mask = l.split()[-1]
	else:
		m = re.match('mem\[(.*)\] = (.*)', l)
		mem[int(m[1])] = applymask(mask, int(m[2]))

print(sum(mem.values()))


# Part Two

def countmaskcombos(mask):
	combos = ''.join([ '1' if c=='X' else '0' for c in mask ])
	combos = int(combos, 2)
	return combos

masks = [ m.split()[-1] for m in input if m.startswith('mask = ') ][::-1]
mi = 0

print(masks)

def suppressmask(m, M): # M supercedes m i.e. 0XX1,X0X0 -> 00X1
	return ''.join([ mc if Mc=='X' else Mc for (mc, Mc) in zip(m, M) ])

effective = [masks[0]] + [ suppressmask(mc, Mc) for (mc, Mc) in zip(masks[1:], masks) ]
print(effective)

s = 0
combos = 2**effective[mi].count('X')
for l in input[:0:-1]:
	if l.startswith('mask = '):
		mi += 1
		combos = 2**effective[mi].count('X')
	else:
		m = re.match('mem\[(.*)\] = (.*)', l)
		s += combos * int(m[2])
print(s)
