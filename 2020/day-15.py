input = [ 14,8,16,0,1,17 ]

n = len(input)
lastpos = { input[i]: i for i in range(n-1) }


# Part One

lastspoken = input[-1]
while n<2020:
	new = n-1-lastpos[lastspoken] if lastspoken in lastpos else 0
	lastpos[lastspoken] = n-1
	lastspoken = new
	n += 1

print(new, flush=True)


# Part Two

while n<30000000:
	if n%1000000 == 0:
		print('n:', n, flush=True)
	new = n-1-lastpos[lastspoken] if lastspoken in lastpos else 0
	lastpos[lastspoken] = n-1
	lastspoken = new
	n += 1

print(new)
