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

def mergemask(mask, at):
	masked = ''.join([ at[i] if mask[i]=='0' else mask[i] for i in range(36) ])
	return masked

addresses = {}
for l in input:
	if l.startswith('mask'):
		mask = l.split()[-1]
	else:
		m = re.match('mem\[(.*)\] = (.*)', l)
		at = f'{int(m[1]):036b}'
		addresses[mergemask(mask, at)] = int(m[2]) # { at: significant-bits, value }

import itertools
def combos(a):
	off = [ i for i in range(36) if a[i] == 'X' ]
	for p in itertools.product(('0','1'), repeat=len(off)):
		ls = list(a)
		for i in range(len(off)):
			ls[off[i]] = p[i]
		yield ''.join(ls)

mem = {}
for a in addresses:
	for c in combos(a):
		mem[c] = addresses[a]

print(sum(mem.values()))
