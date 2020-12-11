with open('input-08.txt') as f:
	input = f.read().split('\n')
input = [ [op[0], int(op[1])] for op in [l.split() for l in input] ]

def run(prog):
	pc = 0
	mem = 0

	def acc(n):
		nonlocal mem
		mem += n
	def jmp(n):
		nonlocal pc
		pc += n-1
	def nop(n):
		pass

	ops = {
		'acc': acc,
		'jmp': jmp,
		'nop': nop,
	}

	hasRun = []
	while pc < len(prog):
		if pc in hasRun:
			return 1, mem
		else:
			hasRun.append(pc)
		op = prog[pc][0]
		arg = prog[pc][1]
		ops[op](arg)
		pc += 1
	if pc > len(prog):
		return 2, mem
	return 0, mem

# Part One
print(run(input)[1])

# Part Two
def swap(ins):
	if   ins[0] == 'nop': ins[0] = 'jmp'; return True
	elif ins[0] == 'jmp': ins[0] = 'nop'; return True
	return False

prog = input.copy()
for ins in prog:
	if not swap(ins):
		continue
	res = run(prog)
	if res[0] == 0:
		print(f'acc: {res[1]}')
		break
	else:
		swap(ins) # restore for next run
