# dp[i][j] = max(dp[이전 물건][현재 가방 무게], 현재 물건 가치 + dp[이전 물건][현재 가방 무게 - 현재 물건 무게])

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = []
dp = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = items[i-1][0]
        v = items[i-1][1]
        if j < w:  # 물건을 못 넣는 경우(무게 초과)
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[n][k])