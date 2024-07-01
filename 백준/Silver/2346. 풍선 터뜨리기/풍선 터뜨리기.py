import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque(enumerate(map(int, input().split()), start=1))

for i in range(n):
    p = queue.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        queue.rotate(-(p[1] - 1))
    else:
        queue.rotate(-p[1])