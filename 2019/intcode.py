from enum import Enum, auto


class State(Enum):
	SUSPENDED = auto(),
	RUNNING = auto(),
	HALTED = auto(),
	CRASHED = auto(),


class Proc:
	def __init__(self, prog, io_in=None, io_out=None):
		self.mem = prog.copy()
		self.pc = 0
		self.io_in = io_in if io_in is not None else []
		self.io_out = io_out if io_out is not None else []
		self.state = State.SUSPENDED

	def get(self, mode):
		self.pc += 1
		if mode == 0: return self.mem[self.mem[self.pc-1]]
		elif mode == 1: return self.mem[self.pc-1]

	def set(self, mode, val):
		if mode == 0: self.mem[self.mem[self.pc]] = val
		elif mode == 1: self.mem[self.pc] = val # never?
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
		99: halt,
	}


	def step(self):
		if self.state not in [ State.SUSPENDED, State.RUNNING ]:
			print('err: proc is', self.state)
			return

		ins = self.mem[self.pc]
		op = ins % 100
		mode = [ int(c) for c in f'{ins//100:03}' ][::-1] # 11xx -> '011' -> [0,1,1] -> [1,1,0]

		if op not in Proc.ops:
			self.state = State.CRASHED
			print(f'err @{self.pc}: {ins}')
			return

		self.pc += 1 # move to first param / next ins
		Proc.ops[op](self, *mode)


	def run(self):
		if self.state is not State.SUSPENDED:
			print('err: proc is', self.state)
			return
			
		self.state = State.RUNNING
		while self.state is State.RUNNING:
			self.step()
