with open('input-16.txt') as f:
	input = f.read().splitlines()

sep = input.index('')
field_ranges = { d: [ range(*( int(b) + (1 if i==1 else 0) for i,b in enumerate(v.split('-')) )) for v in r.split(' or ') ] for d, r in (l.split(': ') for l in input[:sep]) } # comprehension goes brrrt
ticket = [ int(v) for v in input[sep+2].split(',') ]
nearby_tickets = [ [ int(v) for v in l.split(',') ] for l in input[sep+5:] ]


# Part One

print(
	sum(v
		for t in nearby_tickets
			for v in t
				if all(
					v not in r
					for fr in field_ranges.values()
						for r in fr)
	)
)


# Part Two

nearby_valid = [ t
	for t in nearby_tickets
		if all(
			any(v in r
				for fr in field_ranges.values()
					for r in fr
			) for v in t) ]

possible_columns = { f: list(range(len(ticket))) for f in field_ranges }

for i, column in enumerate(zip(*nearby_valid)):
	for f, fr in field_ranges.items():
		if any(
			all(v not in r
				for r in fr)
			for v in column
		):
			possible_columns[f].remove(i)

ordered = sorted([ (d, possible_columns[d]) for d in possible_columns ], key=lambda e: len(e[1]) )

import itertools
for o, onext in itertools.combinations(ordered, 2):
	onext[1].remove(o[1][0])

field_column = { o[0]: o[1][0] for o in ordered }

import functools
print(
	functools.reduce(
		lambda p,v: p*v,
		(ticket[c] for f, c in field_column.items() if f.startswith('departure'))
	)
)
