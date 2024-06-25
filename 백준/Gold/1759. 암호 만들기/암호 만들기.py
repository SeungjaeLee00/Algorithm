from itertools import combinations

vows = ['a', 'e', 'i', 'o', 'u']

def is_possible(word):
	global l, c, alpa_list

	vow = 0
	for w in word:
		vow += (w in vows)
	con = l - vow 

	return (vow >= 1 and con >= 2)

l, c = map(int, input().split())
alpa_list = input().split()

alpa_list.sort()

for word in combinations(alpa_list, l):
	if is_possible(word):
		print(''.join(word))