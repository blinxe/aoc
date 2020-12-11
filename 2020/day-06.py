with open('input-06.txt') as f:
	input = f.read()
input = input.split('\n\n')
input = [ g.split() for g in input ]

# Part One
def handleGroup(g):
	az = set()
	for p in g:
		for l in p:
			az.add(l)
	return az

az = map(handleGroup, input)
s = map(len, az)
print(sum(s))

# Part Two
import string
def handleGroupCommon(g):
	az = list(string.ascii_lowercase)
	for p in g:
		tmp = az.copy()
		for l in az:
			if l not in p:
				tmp.remove(l)
		az = tmp
	return az

az = map(handleGroupCommon, input)
s = map(len, az)
print(sum(s))

handleGroupCommon(input[0])
