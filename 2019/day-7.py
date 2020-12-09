from intcode import Proc, State
import itertools

with open('input-7.txt') as f:
	input = [int(s) for s in f.read().split(',')]

# Part One
M = 0
pM = None
for p in itertools.permutations(range(5)):
	throughput = 0

	for i in range(5):
		amp = Proc(input, [p[i], throughput])
		amp.run()
		throughput = amp.p_out[0]
	if throughput > M:
		M = throughput
		pM = p

print(pM, M, flush=True)

# Part Two
M = 0
pM = None
for init in itertools.permutations(range(5, 10)):
	throughput = 0

	amps = [ Proc(input, [i, 0]) for i in init ]
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

print(pM, M)
