with open('input-4.txt') as f:
	input = f.read()

records = input.replace('\n', ' ').split('  ')
records = [{kv.split(':')[0]:kv.split(':')[1] for kv in r.split()} for r in records]

# Part One
no_cid = [{k:v for (k,v) in r.items() if k != 'cid'} for r in records]
complete = [r for r in no_cid if len(r) == 7]
print(len(complete))

# Part Two
import re
def isValid(r):
	byr = int(r['byr'])
	if byr < 1920 or byr > 2002: return False

	iyr = int(r['iyr'])
	if iyr < 2010 or iyr > 2020: return False

	eyr = int(r['eyr'])
	if eyr < 2020 or eyr > 2030: return False

	hgt = re.match('([0-9]+)(cm|in)$', r['hgt'])
	if not hgt: return False
	h = int(hgt[1])
	u = hgt[2]
	if u == 'cm' and (h < 150 or h > 193):
		return False
	elif u == 'in' and (h < 59 or h > 76):
		return False

	hcl = re.match('#[0-9a-fA-F]{6}$', r['hcl'])
	if not hcl: return False

	if r['ecl'] not in [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth', ]:
		return False

	pid = re.match('[0-9]{9}$', r['pid'])
	if not pid: return False

	return True

valid = [r for r in complete if isValid(r)]
print(len(valid))
