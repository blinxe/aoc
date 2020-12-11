from intcode import Proc, State
import itertools


########
# Day 2
print('Day 2', flush=True)

with open('input-02.txt') as f:
	input = f.read()
prog = list(map(int, input.split(',')))

# Part One
p = Proc(prog)
p.mem[1] = 12
p.mem[2] = 2
p.run()
print('Part One:', p.mem[0], flush=True)

# Part Two
for n, v in itertools.product(range(100), range(100)):
	p = Proc(prog)
	p.mem[1] = n
	p.mem[2] = v
	p.run()
	if p.mem[0] == 19690720:
		print('Part Two:', 100*n + v, flush=True)
		break
print()


########
# Day 5
print('Day 5', flush=True)

with open('input-05.txt') as f:
	input = f.read()
prog = list(map(int, input.split(',')))

# Part One
p = Proc(prog, io_in=[1])
p.run()
print('Part One:', p.io_out, flush=True)

# Part Two
p = Proc(prog, io_in=[5])
p.run()
print('Part Two:', p.io_out[0], flush=True)
print()


########
# Day 7
print ('Day 7', flush=True)

with open('input-07.txt') as f:
	prog = [int(s) for s in f.read().split(',')]

# Part One
M = 0
pM = None
for p in itertools.permutations(range(5)):
	throughput = 0

	for i in range(5):
		amp = Proc(prog, [p[i], throughput])
		amp.run()
		throughput = amp.io_out[0]
	if throughput > M:
		M = throughput
		pM = p

print('Part One:', pM, M, flush=True)

# Part Two
M = 0
pM = None
for init in itertools.permutations(range(5, 10)):
	throughput = 0

	amps = [ Proc(prog, [i, 0]) for i in init ]
	amps[-1].io_out = [0] # initial input
	for i in range(5):
		amps[i].step() # read phase setting
		amps[i].io_in = amps[(i+4)%5].io_out
	i = 0
	while amps[i].state is not State.HALTED:
		amps[i].run()
		i = (i+1) % 5

	throughput = amps[-1].io_out[0]
	if throughput > M:
		M = throughput
		pM = init

print('Part Two:', pM, M, flush=True)
print()


########
# Day 9
print ('Day 9', flush=True)

with open('input-09.txt') as f:
	prog = [ int(s) for s in f.read().split(',') ]

# Part One
boost = Proc(prog, io_in=[1])
boost.run()
print('Part One:', boost.io_out[0], flush=True)

# Part Two
boost = Proc(prog, io_in=[2])
boost.run()
print('Part Two:', boost.io_out[0], flush=True)
print()
