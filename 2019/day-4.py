input = range(231832, 767346)

# Part One
# def isValid(i):
# 	s = str(i)
# 	double = False
# 	for i in range(5):
# 		if s[i] > s[i+1]:
# 			return False
# 		if s[i] == s[i+1]:
# 			double = True
# 	return double

# valid = [i for i in input if isValid(i)]
# print(len(valid))

# Part Two
def isValid(i):
	s = str(i)
	for i in range(5):
		if s[i] > s[i+1]:
			return False
	for c in set(s):
		if s.count(c) == 2: # part one alt: >=
			return True

valid = [i for i in input if isValid(i)]
print(len(valid))
