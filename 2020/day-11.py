with open('input-11.txt') as f:
	input = f.read().splitlines()

class Automaton:
	def __init__(self, pattern, p2=False):
		self.W = len(pattern[0])
		self.H = len(pattern)
		self.grid = [[c for c in row] for row in pattern]
		if p2:
			self.isawkard = lambda n: n>=5
		else:
			self.isawkard = lambda n: n>=4
			self.getfar = lambda r,c,dr,dc: self.get(r+dr, c+dc)
		self.turns = 0

	def get(self, r, c):
		if r<0 or r>=self.H or c<0 or c>=self.W:
			return None
		return self.grid[r][c]

	def getfar(self, r, c, dr, dc):
		n = '.'
		while n == '.':
			r += dr
			c += dc
			n = self.get(r, c)
		return n

	def neighbors(self, r, c):
		n = []
		for dr in (-1, 0, 1):
			for dc in (-1, 0, 1):
				if dr==0 and dc==0: continue
				nn = self.getfar(r, c, dr, dc)
				if nn is not None:
					n.append(nn)
		return n

	def step(self):
		self.turns += 1
		updt = False
		swap = [[c for c in row] for row in self.grid]
		for r in range(self.H):
			for c in range(self.W):
				state = self.grid[r][c]
				if state == '.': continue
				n = list(self.neighbors(r, c))
				occ = n.count('#')
				if state == 'L':
					if occ == 0:
						swap[r][c] = '#'
						updt = True
				elif state == '#':
					if self.isawkard(occ):
						swap[r][c] = 'L'
						updt = True
		self.grid = swap
		return updt

	def run(self):
		running = True
		while running:
			running = self.step()

	def disp(self):
		for row in self.grid:
			print(*row, sep='')

# Part One
a = Automaton(input)
a.run()
print(sum(row.count('#') for row in a.grid), flush=True)

# Part Two
a = Automaton(input, True)
a.run()
print(sum(row.count('#') for row in a.grid))
