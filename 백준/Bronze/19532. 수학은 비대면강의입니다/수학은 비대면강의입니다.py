a, b, c, d, e, f = map(int, input().split())
# print(a, b, c, d, e, f)
print((e*c - b*f) // (a*e - b*d), (a*f - c*d) // (a*e - b*d))