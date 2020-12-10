from intcode import Proc, State

with open('input-9.txt') as f:
	prog = [ int(s) for s in f.read().split(',') ]

# Part One
boost = Proc(prog, io_in=[1])
boost.run()
print(boost.io_out, flush=True)

# Part Two
boost = Proc(prog, io_in=[2])
boost.run()
print(boost.io_out, flush=True)
