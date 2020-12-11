with open('input-05.txt') as f:
	input = f.read()
input = list(map(int, input.split(',')))

mem = []
p_in = []
p_out = []

def get(pc, mode):
	if mode == 0: return mem[mem[pc]]
	elif mode == 1: return mem[pc]

def set(pc, mode, val):
	if mode == 0: mem[mem[pc]] = val
	elif mode == 1: mem[pc] = val # never?


def add(pc, mode):
	op1 = get(pc, mode[0])
	op2 = get(pc+1, mode[1])
	set(pc+2, mode[2], op1+op2)
	return 3

def mul(pc, mode):
	op1 = get(pc, mode[0])
	op2 = get(pc+1, mode[1])
	set(pc+2, mode[2], op1*op2)
	return 3

def read(pc, mode):
	set(pc, mode[0], p_in.pop(0))
	return 1

def write(pc, mode):
	p_out.append(get(pc, mode[0]))
	return 1

def jeq(pc, mode):
	if get(pc, mode[0]) == 0: return 2
	to = get(pc+1, mode[1])
	return to-pc

def jne(pc, mode):
	if get(pc, mode[0]) != 0: return 2
	to = get(pc+1, mode[1])
	return to-pc

def lt(pc, mode):
	p1 = get(pc, mode[0])
	p2 = get(pc+1, mode[1])
	set(pc+2, mode[2], 1 if p1<p2 else 0)
	return 3

def eq(pc, mode):
	p1 = get(pc, mode[0])
	p2 = get(pc+1, mode[1])
	set(pc+2, mode[2], 1 if p1==p2 else 0)
	return 3


ops = {
	1: add,
	2: mul,
	3: read,
	4: write,
	5: jeq,
	6: jne,
	7: lt,
	8: eq,
}


def run():
	pc = 0
	while mem[pc] != 99:
		op = mem[pc] % 100
		mode = [int(c) for c in f'{mem[pc]//100:03}'[::-1]]
		if op not in ops:
			print(f'err @{pc}: {mem[pc]}')
			break
		pc += 1 + ops[op](pc+1, mode)


# Part One
mem = input.copy()
p_in = [ 1 ]
p_out = []
run()
print(p_out)

# Part Two
mem = input.copy()
p_in = [ 5 ]
p_out = []
run()
print(p_out)
