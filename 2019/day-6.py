with open('input-6.txt') as f:
	input = f.read().split()
input = { p[1]: p[0] for p in [i.split(')') for i in input] }
