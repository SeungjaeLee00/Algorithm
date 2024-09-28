total = int(input())
n = int(input())
things_num = 0
for i in range(n):
    things, num = map(int, input().split())
    things_num += things * num
if things_num == total:
    print("Yes")
else:
    print("No")

