with open('input-19.txt') as f:
	input = f.read().replace('"', '').splitlines()

sep = input.index('')
rules = input[:sep]
messages = input[sep+1:]


rules = {
	r[0]: [
		seq.split(' ') for seq in r[1].split(' | ') 
	]
	for r in ( s.split(': ') for s in rules )
}

bases = [ r for r,v in rules.items() if v in [[['a']], [['b']]] ]
for b in bases:
	rules[b] = rules[b][0][0]

def match(s, r):
	if not s:
		return 0
	if r in bases:
		return 1 if s[0] == rules[r] else 0
	for seq in rules[r]:
		pos = 0
		for sub in seq:
			m = match(s[pos:], sub)
			if m == 0:
				pos = 0
				break
			else:
				pos += m
		if pos != 0:
			return pos
	return 0


# Part One

print(sum(1 for m in messages if match(m, '0') == len(m)))


# Part Two

rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]

rules['8'] = [ ['42']*n for n in range(1, 0, -1) ]
rules['11'] = [ ['42']*n + ['31']*n for n in range(1, 0, -1) ]

# print(sum(1 for m in messages if match(m, '0') == len(m)))
print(match('babbbbabbbbbbaa', '0'))

rules['lol'] = [ ['42','42'], ['42'] ]
print(match('babbbbabbb', 'lol'))
