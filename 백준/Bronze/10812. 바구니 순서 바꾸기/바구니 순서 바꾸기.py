import sys
N, M = map(int, sys.stdin.readline().split())
tmp = [ i+1 for i in range(N)]
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    tmp[i-1:j] = tmp[k-1:j]+tmp[i-1:k-1]
print(*tmp)