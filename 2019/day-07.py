from intcode import Proc, State
import itertools

with open('input-07.txt') as f:
	input = [int(s) for s in f.read().split(',')]

NAMPS = 5
INPUT = 0

# Part One
M = 0
pM = None
for phases in itertools.permutations(range(NAMPS)):
	throughput = INPUT

	for i in range(NAMPS):
		amp = Proc(input, [phases[i], throughput])
		amp.run()
		throughput = amp.io_out[0]
	if throughput > M:
		M = throughput
		pM = phases

print(pM, M, flush=True)

# Part Two
M = 0
pM = None
for phases in itertools.permutations(range(5, 5+NAMPS)):
	ios = [ [i] for i in phases ]
	ios[0].append(INPUT)
	amps = [ Proc(input, ios[i], ios[(i+1)%NAMPS]) for i in range(NAMPS) ]

	i = 0
	while amps[i].state is State.SUSPENDED:
		amps[i].run()
		i = (i+1) % NAMPS

	throughput = amps[-1].io_out[0]
	if throughput > M:
		M = throughput
		pM = phases

print(pM, M)
