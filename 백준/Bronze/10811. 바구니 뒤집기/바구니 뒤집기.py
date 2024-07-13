N, M = map(int, input().split())
box = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    box = box[0:i-1]+box[i-1:j][::-1]+box[j:]  # 리스트 짤라서 붙여!
for i in range(0, N):
    print(box[i], end = ' ')