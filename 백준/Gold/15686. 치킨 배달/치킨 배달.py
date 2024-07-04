import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

chicken = []
home = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

result = n * 2 * len(home)  # 모든 집이 가장 멀리 있는 경우로 설정
for comb in list(combinations(chicken, m)):  # 가능한 모든 조합 생성
    dist = 0
    for a, b in home:
        temp = n * 2  # 일단 최대 거리로 설정함
        for c, d in comb:
            temp = min(temp, abs(a - c) + abs(b - d))
        dist += temp
    result = min(result, dist)

print(result)