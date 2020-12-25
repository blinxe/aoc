with open('input-18.txt') as f:
	input = f.read().splitlines()

input = [ l.replace('(', '( ').replace(')', ' )').split() for l in input ]


# Part One

def evaluate(expr):
	acc = 0
	op = None
	i = 0
	while i < len(expr):
		tok = expr[i]
		val = None
		if tok in ['+', '*']:
			op = tok
		elif tok == '(':
			val, length = evaluate(expr[i+1:])
			i += length
		elif tok == ')':
			return acc, i+1
		else:
			val = int(tok)

		if val is not None:
			if op == '+':
				acc += val
			elif op == '*':
				acc *= val
			else:
				acc = val
		i += 1

	return acc

print(sum(evaluate(l) for l in input))


# Part Two

def evaluate_p2(expr):
	acc = 0
	stack = None
	op = None
	i = 0
	while i < len(expr):
		tok = expr[i]
		val = None
		if tok in ['+', '*']:
			op = tok
		elif tok == '(':
			val, length = evaluate_p2(expr[i+1:])
			i += length
		elif tok == ')':
			if stack is not None:
				acc *= stack
			return acc, i+1
		else:
			val = int(tok)

		if val is not None:
			if op == '+':
				acc += val
			elif op == '*':
				if stack is None:
					stack = acc
				else:
					stack = stack*acc
				acc = val
			else:
				acc = val
		i += 1

	if stack is not None:
		acc *= stack
	return acc

print(sum(evaluate_p2(l) for l in input))
