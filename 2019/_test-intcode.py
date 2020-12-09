from intcode import Proc, State
import itertools


########
# Day 2
print('Day 2', flush=True)

with open('input-2.txt') as f:
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
	# while p.state != State.HALTED:
	# 	p.step()
	p.run()
	if p.mem[0] == 19690720:
		print('Part Two:', 100*n + v, flush=True)
		break
print()


########
# Day 5
print('Day 5', flush=True)

with open('input-5.txt') as f:
	input = f.read()
prog = list(map(int, input.split(',')))

# Part One
p_out = []
p = Proc(prog, p_in=[1], p_out=p_out)
p.run()
print('Part One:', p_out, flush=True)

# Part Two
p_out = []
p = Proc(prog, p_in=[5], p_out=p_out)
p.run()
print('Part Two:', p_out[0], flush=True)
print()


########
# Day 7
print ('Day 7', flush=True)

with open('input-7.txt') as f:
	prog = [int(s) for s in f.read().split(',')]

# Part One
M = 0
pM = None
for p in itertools.permutations(range(5)):
	throughput = 0

	for i in range(5):
		amp = Proc(prog, [p[i], throughput])
		amp.run()
		throughput = amp.p_out[0]
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
	amps[-1].p_out = [0] # initial input
	for i in range(5):
		amps[i].step() # read phase setting
		amps[i].p_in = amps[(i+4)%5].p_out
	i = 0
	while amps[i].state is not State.HALTED:
		amps[i].run()
		i = (i+1) % 5

	throughput = amps[-1].p_out[0]
	if throughput > M:
		M = throughput
		pM = init

print('Part Two:', pM, M, flush=True)
print()
