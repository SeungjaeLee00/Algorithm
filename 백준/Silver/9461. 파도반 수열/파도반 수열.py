import sys
input = sys.stdin.readline

def P(n):
    dp = [0, 1, 1, 1] + [0 for i in range(97)]
    dp[1] = dp[2] = dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(P(n))