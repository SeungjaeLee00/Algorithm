n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, n+1):
    if i % 2 == 0:  # 짝수일 때, 벽 가로가 홀수면 가득 못채움
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else:
        dp[i] = 0
print(dp[n])