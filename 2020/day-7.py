with open('input-7.txt') as f:
	input = f.read().split('\n')

def parseAllowed(bt):
	n, adj, col, _ = bt.split()
	return ((adj, col), int(n))

# Part One
permissions = {}

def addPermissions(r):
	adjcol, allowed = r.split(' bags contain ')
	adj, col = tuple(adjcol.split(' '))
	if allowed == 'no other bags.':
		return
	allowed = [parseAllowed(bt) for bt in allowed.split(', ')]
	for a in allowed:
		if a[0] not in permissions:
			permissions[a[0]] = []
		permissions[a[0]].append(((adj, col), a[1]))

for r in input:
	addPermissions(r)

ancestors = set()
more = [p[0] for p in permissions[('shiny', 'gold')]]
while more:
	ancestors.update(more)
	latest = more
	more = []
	for l in latest:
		if l not in permissions:
			continue
		more += [p[0] for p in permissions[l] if p not in ancestors]

print(len(ancestors))

# Part Two
def parseRules(r):
	adjcol, allowed = r.split(' bags contain ')
	adj, col = tuple(adjcol.split(' '))
	if allowed == 'no other bags.':
		allowed = []
	else:
		allowed = [parseAllowed(bt) for bt in allowed.split(', ')]
	return (adj, col), allowed

def bagsInBag(rules, bt):
	return sum(n + n*bagsInBag(rules, b) for b, n in rules[bt])

rules = {r[0]: r[1] for r in [parseRules(r) for r in input]}
print(bagsInBag(rules, ('shiny', 'gold')))
