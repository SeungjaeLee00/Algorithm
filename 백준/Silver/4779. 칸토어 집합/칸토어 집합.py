def cantor(k):
	if k == 0:
		print("-", end="")
		return

	cantor(k - 1)
	print(" " * (3 ** (k - 1)), end="")
	cantor(k - 1)

while True:
	try:
		n = int(input())
		cantor(n)
		print()
	except:
		break