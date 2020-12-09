from enum import Enum, auto


class State(Enum):
	SUSPENDED = auto(),
	RUNNING = auto(),
	HALTED = auto(),
	CRASHED = auto(),


class Proc:
	def __init__(self, prog, p_in=None, p_out=None):
		self.mem = prog.copy()
		self.pc = 0
		self.p_in = p_in if p_in is not None else []
		self.p_out = p_out if p_out is not None else []
		self.state = State.SUSPENDED

	def get(self, mode):
		self.pc += 1
		if mode == 0: return self.mem[self.mem[self.pc-1]]
		elif mode == 1: return self.mem[self.pc-1]

	def set(self, mode, val):
		if mode == 0: self.mem[self.mem[self.pc]] = val
		elif mode == 1: self.mem[self.pc] = val # never?
		self.pc += 1


	def add(self, mode):
		op1 = self.get(mode[0])
		op2 = self.get(mode[1])
		self.set(mode[2], op1+op2)

	def mul(self, mode):
		op1 = self.get(mode[0])
		op2 = self.get(mode[1])
		self.set(mode[2], op1*op2)

	def read(self, mode):
		if not self.p_in:
			self.pc -= 1 # back to ins 'read'
			self.state = State.SUSPENDED
			return
		self.set(mode[0], self.p_in.pop(0))

	def write(self, mode):
		self.p_out.append(self.get(mode[0]))

	def jeq(self, mode):
		if self.get(mode[0]) == 0:
			self.pc += 1
			return
		self.pc = self.get(mode[1])

	def jne(self, mode):
		if self.get(mode[0]) != 0:
			self.pc += 1
			return
		self.pc = self.get(mode[1])

	def lt(self, mode):
		p1 = self.get(mode[0])
		p2 = self.get(mode[1])
		self.set(mode[2], 1 if p1<p2 else 0)

	def eq(self, mode):
		p1 = self.get(mode[0])
		p2 = self.get(mode[1])
		self.set(mode[2], 1 if p1==p2 else 0)

	def halt(self, _):
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
			print(f'err: proc is {self.state}')
			return
		ins = self.mem[self.pc]
		op = ins % 100
		mode = [int(c) for c in f'{ins//100:03}'[::-1]]
		if op not in Proc.ops:
			self.state = State.CRASHED
			print(f'err @{self.pc}: {ins}')
			return
		self.pc += 1
		Proc.ops[op](self, mode)

	def run(self):
		if self.state is not State.SUSPENDED:
			print(f'err: proc is {self.state}')
			return
		self.state = State.RUNNING
		while self.state is State.RUNNING:
			self.step()
