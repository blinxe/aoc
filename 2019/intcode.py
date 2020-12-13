from enum import Enum, auto


class State(Enum):
	SUSPENDED = auto(),
	RUNNING = auto(),
	HALTED = auto(),
	CRASHED = auto(),


class VMem:
	def __init__(self, mem):
		self.vmem = [ (0, mem) ]

	def __str__(self):
		return self.vmem.__str__()

	def __getitem__(self, at):
		off, mem = next(((off, mem) for off, mem in self.vmem if at>=off and at<off+len(mem)), (at, [0]))
		return mem[at-off]

	def __setitem__(self, at, val):
		frag = next(((off, mem) for off, mem in self.vmem if at>=off and at<off+len(mem)), None)
		if frag is None:
			self.vmem.append([at, [val]])
			self.defrag()
		else:
			off, mem = frag
			mem[at-off] = val

	def defrag(self):
		# lol
		pass


class Proc:
	def __init__(self, prog, io_in=None, io_out=None, dbgflags=None):
		self.mem = VMem(prog.copy())
		self.pc = 0
		self.rb = 0
		self.io_in = io_in if io_in is not None else []
		self.io_out = io_out if io_out is not None else []
		self.state = State.SUSPENDED
		self.dbgflags = dbgflags if dbgflags is not None else []


	def get(self, mode):
		if mode == 0: val = self.mem[self.mem[self.pc]]
		elif mode == 1: val = self.mem[self.pc]
		elif mode == 2: val = self.mem[self.mem[self.pc] + self.rb]
		self.pc += 1
		return val

	def set(self, mode, val):
		if mode == 0: self.mem[self.mem[self.pc]] = val
		elif mode == 1: self.mem[self.pc] = val
		elif mode == 2: self.mem[self.mem[self.pc] + self.rb] = val
		self.pc += 1


	def add(self, m1, m2, mo, *_):
		op1 = self.get(m1)
		op2 = self.get(m2)
		self.set(mo, op1+op2)

	def mul(self, m1, m2, mo, *_):
		op1 = self.get(m1)
		op2 = self.get(m2)
		self.set(mo, op1*op2)

	def read(self, mo, *_):
		if not self.io_in:
			self.pdbg('io', 'Waiting for input')
			self.pc -= 1 # back to ins 'read'
			self.state = State.SUSPENDED
			return
		self.set(mo, self.io_in.pop(0))

	def write(self, mi, *_):
		self.io_out.append(self.get(mi))

	def jeq(self, m1, m2, *_):
		if self.get(m1) == 0:
			self.pc += 1
			return
		self.pc = self.get(m2)

	def jne(self, m1, m2, *_):
		if self.get(m1) != 0:
			self.pc += 1
			return
		self.pc = self.get(m2)

	def lt(self, m1, m2, mo, *_):
		p1 = self.get(m1)
		p2 = self.get(m2)
		self.set(mo, 1 if p1<p2 else 0)

	def eq(self, m1, m2, mo, *_):
		p1 = self.get(m1)
		p2 = self.get(m2)
		self.set(mo, 1 if p1==p2 else 0)

	def rboff(self, m1, *_):
		self.rb += self.get(m1)
		self.pdbg('rb', 'rb:', self.rb)

	def halt(self, *_):
		self.state = State.HALTED


	ops = {
		1: add,
		2: mul,
		3: read,
		4: write,
		5: jeq,
		6: jne,
		7: lt,
		8: eq,
		9: rboff,
		99: halt,
	}


	def pdbg(self, flag, *args, **kwargs):
		if flag in self.dbgflags:
			print(*args, **kwargs)


	def step(self):
		if self.state not in [ State.SUSPENDED, State.RUNNING ]:
			print('err: proc is', self.state)
			return

		ins = self.get(1)
		self.pdbg('ic', self.pc-1, ins)
		op = ins % 100
		mode = [ int(c) for c in f'{ins//100:03}' ][::-1]

		if op not in Proc.ops:
			self.state = State.CRASHED
			print(f'err @{self.pc-1}: {ins}')
			return

		Proc.ops[op](self, *mode)


	def run(self):
		if self.state is not State.SUSPENDED:
			print('err: proc is', self.state)
			return
			
		self.state = State.RUNNING
		while self.state is State.RUNNING:
			self.step()
