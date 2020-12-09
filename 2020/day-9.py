with open('input-9.txt') as f:
	input = [int(s) for s in f.read().split()]

import itertools

# Part One
for i, n in enumerate(input[25:]):
	if n not in (n1+n2 for (n1,n2) in itertools.combinations(input[i:i+25], 2)):
		weakness = n
		break
print('weakness:', weakness)

# Part Two
for start in range(len(input)):
	s = input[start]
	if s == weakness:
		continue
	i = start
	while s < weakness:
		i += 1
		s += input[i]
	if s == weakness:
		contiguous = range(start, i+1)

print(contiguous)
m = min(input[c] for c in contiguous)
M = max(input[c] for c in contiguous)
print(m+M)
