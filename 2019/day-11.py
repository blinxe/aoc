from intcode import Proc, State

with open('input-11.txt') as f:
	program = [ int(s) for s in f.read().split(',') ]

dirs = [
	(0, -1),
	(1, 0),
	(0, 1),
	(-1, 0),
]

class IoProviderHull:
	def __init__(self):
		self.hull = {}
		self.botx = 0
		self.boty = 0
		self.unique = 0
		self.inputmode = 0 # 0: receive color, 1: receive move instruction
		self.dir = 0 # up

	def pop(self, index):
		if (self.botx, self.boty) in self.hull:
			return self.hull[self.botx, self.boty]
		return 0

	def append(self, ins):
		if self.inputmode == 0:
			self.paint(ins)
			self.inputmode = 1
		elif self.inputmode == 1:
			self.move(ins)
			self.inputmode = 0
		else:
			print('IoProvider error')

	def paint(self, col):
		if (self.botx, self.boty) not in self.hull:
			self.unique += 1
		self.hull[self.botx, self.boty] = col

	def move(self, ins):
		self.dir = (self.dir + (3 if ins==0 else 1)) % 4
		self.botx += dirs[self.dir][0]
		self.boty += dirs[self.dir][1]


def showHull(hull):
	xx, yy = zip(*hull)
	mx = min(xx)-2
	Mx = max(xx)+2
	my = min(yy)-2
	My = max(yy)+2
	for y in range(my, My+1):
		for x in range(mx, Mx+1):
			if (x, y) in hull and hull[x, y] == 1:
				print('  ', end='')
			else:
				print('[]', end='')
		print()

# Part One:
iohull = IoProviderHull()
robot = Proc(program, iohull, iohull, dbgflags=['io'])
robot.run()
showHull(iohull.hull)
print('Unique painted panes:', iohull.unique)
print()

# Part Two:
iohull = IoProviderHull()
iohull.paint(1)
robot = Proc(program, iohull, iohull, dbgflags=['io'])
robot.run()
showHull(iohull.hull)
