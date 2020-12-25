pk_card = 2959251
pk_door = 4542595
# pk_card = 5764801
# pk_door = 17807724

def find_sk(pk, subject=7):
	v = 1
	n = 0
	while v != pk:
		v = (subject*v) % 20201227
		n += 1
	return n

def transform(sk, subject=7):
	v = 1
	for _ in range(sk):
		v = (subject*v) % 20201227
	return v


sk_card = find_sk(pk_card)
enc = transform(sk_card, subject=pk_door)
print(enc)
