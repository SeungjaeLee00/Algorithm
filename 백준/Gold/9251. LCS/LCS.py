A = list(input())
B = list(input())
len_A = len(A)
len_B = len(B)
# dp = []
# dp = [[0] * (len_B + 1)] * (len_A + 1)
dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if A[i-1] == B[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len_A][len_B])  # dp table 맨 마지막 값 출력