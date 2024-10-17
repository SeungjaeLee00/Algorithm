import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr2 = []
arr2 = list(sorted(set(arr)))

dic = {arr2[i]: i for i in range(len(arr2))}  # {key:value} 딕셔너리 쓰면 자체적으로 중복 제거 가능! 시간 복잡도 O(1)

for i in arr:
  print(dic[i], end=' ')