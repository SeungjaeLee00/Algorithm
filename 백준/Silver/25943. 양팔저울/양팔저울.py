import sys
input = sys.stdin.readline

n = int(input())
pebble = list(map(int, input().split()))
weights = [100, 50, 20, 10, 5, 2, 1]

left, right = pebble[0], pebble[1]

for i in range(2, n):
    if left == right:
        left += pebble[i]
    else:
        if left < right:
            left += pebble[i]
        elif left > right:
            right += pebble[i]

diff = abs(left - right)
count = 0

while diff:
    for weight in weights:
        count += diff // weight
        diff %= weight

print(count)