import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
a = [int(input()) for i in range(N)]

print(round(sum(a)/N))  # 산술평균

a.sort()
print(a[N//2])  # 중앙값

cnt_a = Counter(a).most_common()
if len(cnt_a) > 1 and cnt_a[0][1] == cnt_a[1][1]: # 최빈값 2개 이상
    print(cnt_a[1][0])
else:
    print(cnt_a[0][0])  # 최빈값

print(max(a)-min(a))  # 범위