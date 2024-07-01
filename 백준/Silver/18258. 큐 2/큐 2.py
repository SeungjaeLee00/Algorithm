import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    com = input().split()

    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        print(-1) if len(queue) == 0 else print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        print(1) if len(queue) == 0 else print(0)
    elif com[0] == 'front':
        print(-1) if len(queue) == 0 else print(queue[0])
    elif com[0] == 'back':
        print(-1) if len(queue) == 0 else print(queue[-1])