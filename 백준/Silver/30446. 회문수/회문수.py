n = int(input())
count = 0

# if n >= 9:
#     count += 9

for i in range(1, 10):
    if i <= n:
        count += 1

for i in range(1, 100001):
    s = str(i)
    if int(s + s[::-1]) <= n:
        count += 1

    for j in range(10):
        if int(s + str(j) + s[::-1]) <= n:
            count += 1
print(count)