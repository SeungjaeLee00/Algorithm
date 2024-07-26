n = int(input())
player = [list(map(int, input().split())) for _ in range(n)]

player = sorted(player, key=lambda x: (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

print(" ".join(str(player[i][0]) for i in range(0, 3, 1)))
