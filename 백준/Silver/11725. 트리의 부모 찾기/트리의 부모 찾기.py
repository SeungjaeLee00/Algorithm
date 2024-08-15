import sys
from collections import deque
 
N = int(sys.stdin.readline())
 
# 그래프 생성
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
# 방문 여부, 각 인덱스를 노드로 사용해 방문했으면 0을 지우고, 부모 노드를 저장
visited = [0]*(N+1) 
 
def bfs(start):
    deq = deque([start])  # 방문할 노드
    
    while deq:
        node = deq.popleft()
        
        for adj in graph[node]:
            if visited[adj] == 0:
                visited[adj] = node
                deq.append(adj)


bfs(1)
answer = visited[2:]
for x in answer:
    print(x)
