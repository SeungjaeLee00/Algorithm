import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    com = input().split()
    l = len(queue)

    if com[0] == '1':
        queue.appendleft(com[1])
    elif com[0] == '2':
        queue.append(com[1])
    elif com[0] == '3':
        print(queue.popleft() if l else -1)
    elif com[0] == '4':
        print(queue.pop() if l else -1)
    elif com[0] == '5':
        print(len(queue))
    elif com[0] == '6':
        print(0 if l else 1)
    elif com[0] == '7':
        print(queue[0] if l else -1)
    elif com[0] == '8':
        print(queue[-1] if l else -1)
        