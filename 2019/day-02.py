with open('input-02.txt') as f:
	input = f.read()
input = list(map(int, input.split(',')))

# Part One
def add(prog, pc):
	in1 = prog[pc+1]
	in2 = prog[pc+2]
	out = prog[pc+3]
	prog[out] = prog[in1]+prog[in2]
def mul(prog, pc):
	in1 = prog[pc+1]
	in2 = prog[pc+2]
	out = prog[pc+3]
	prog[out] = prog[in1]*prog[in2]

ops = {
	1: add,
	2: mul,
}

def run(prog):
	pc = 0
	while prog[pc] != 99:
		if prog[pc] not in ops:
			print(f'err @{pc}: {prog[pc]}')
			break
		ops[prog[pc]](prog, pc)
		pc += 4

mem = input.copy()
mem[1] = 12
mem[2] = 2
run(mem)
print(mem[0])

# Part Two
import itertools
for n, v in itertools.product(range(100), range(100)):
	mem = input.copy()
	mem[1] = n
	mem[2] = v
	run(mem)
	if mem[0] == 19690720:
		print(100*n + v)
		break
