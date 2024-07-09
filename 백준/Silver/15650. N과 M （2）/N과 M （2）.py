import sys
input = sys.stdin.readline

def backtrcking(start):
    if len(arr) == m:
        print(" ".join(map(str, arr)))

    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            backtrcking(i + 1)
            arr.pop()

n, m = map(int, input().split())
arr = []

backtrcking(1)