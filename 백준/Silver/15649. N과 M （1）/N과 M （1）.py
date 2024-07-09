import sys
input = sys.stdin.readline

def backtrcking():
    if len(arr) == m:
        print(" ".join(map(str, arr)))

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            backtrcking()
            arr.pop()

n, m = map(int, input().split())
arr = []

backtrcking()