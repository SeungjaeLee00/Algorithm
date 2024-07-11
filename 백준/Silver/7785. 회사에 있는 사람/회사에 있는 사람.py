import sys
input = sys.stdin.readline

n = int(input())
temp = {}
for _ in range(n):
    a, b = input().rstrip().split()
    if b == 'enter':
        temp[a] = b
    else:
        del temp[a]

temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)

# print('\n'.join(sorted(temp.keys(), reverse=True)))