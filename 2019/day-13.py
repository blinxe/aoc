from intcode import Proc, State

with open('input-13.txt') as f:
	input = [ int(s) for s in f.read().split(',') ]

class IoProviderScreen:
	def __init__(self):
		self.tiles = {}
		self.out = []

	def pop(self, index):
		return 0

	def append(self, ins):
		self.out.append(ins)
		if len(self.out) == 3:
			x,y,t = self.out
			self.tiles[(x,y)] = t
			self.out = []

gfx = {
	0: '  ',
	1: '[]',
	2: '{}',
	3: '<>',
	4: '()',
}

def paintscreen(tiles):
	xx, yy = zip(*tiles)
	mx = min(xx)
	Mx = max(xx)
	my = min(yy)
	My = max(yy)
	for y in range(my, My+1):
		for x in range(mx, Mx+1):
			t = tiles[(x,y)] if (x,y) in tiles else 0
			print(gfx[t], end='')
		print()


# Part One
ioscreen = IoProviderScreen()
game = Proc(input, io_out=ioscreen)
game.run()
paintscreen(ioscreen.tiles)
print(sum(1 for t in ioscreen.tiles.values() if t == 2), 'BLOCK {} tiles')
