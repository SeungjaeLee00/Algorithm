# import sys
# input = sys.stdin.readline

# n = int(input())
# A = list(map(int, input().split()))
# LIS = [A[0]]

# for i in range(1, n):
#     if A[i] > LIS[-1]:
#         LIS.append(A[i])
#         continue

#     start = 0
#     end = len(LIS) - 1
#     m = (start + end) // 2
#     while start < end:
#         if LIS[m] == A[i]:
#             break
#         elif LIS[m] > A[i]:
#             end = m
#         else:
#             start = m + 1
#         m = (start + end) // 2
#     LIS[m] = A[i]

# print(len(LIS))

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

LIS = [A[0]]

for item in A:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = bisect_left(LIS, item)
        LIS[idx] = item

print(len(LIS))