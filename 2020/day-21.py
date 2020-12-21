with open('input-21.txt') as f:
	input = f.read().splitlines()

input = [ l.replace(')', '') for l in input ]
recipes = [ l.split('(contains ') for l in input ]
recipes = [ (l[0].split(), [] if len(l)==0 else l[1].split(', ')) for l in recipes ]

ingredients = list(set( i for ii,_ in recipes for i in ii ))
allergens = list(set( a for _,aa in recipes for a in aa ))


# Part One

alling = {}
for ii,aa in recipes:
	for a in aa:
		if a not in alling:
			alling[a] = set(ii)
		else:
			alling[a] &= set(ii)

known = set()
for ii in alling.values():
	known.update(ii)

occ = [
	sum(1 for i in ii if i not in known)
	for ii,rr in recipes
]

print(sum(occ))


# Part Two

for a,ii in alling.items():
	print(a, list(ii))
print()

# sort by number of possibilities
import itertools
while any(len(aa) > 1 for aa in alling.values()):
	sorted_aa = sorted([ a for a in alling ], key=lambda a: len(alling[a]))
	for a1,a2 in itertools.combinations(sorted_aa, 2):
		if len(alling[a1]) > 1: break
		alling[a2] -= alling[a1]

sorted_aa = sorted(sorted_aa)
print(*(list(alling[a])[0] for a in sorted_aa), sep=',')
