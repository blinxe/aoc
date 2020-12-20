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

# r0 = r8, r11
# r0 = r42+, (r42, r31)+

ok = []
for msg in messages:
	r42 = 0
	off = 0
	while m := match(msg[off:], '42'):
		r42 += 1
		off += m
	r31 = 0
	while m := match(msg[off:], '31'):
		r31 += 1
		off += m
	if off == len(msg) and r42>r31>0:
		ok.append(msg)

print(len(ok))
