X = []
Y = []

for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]
    elif Y.count(Y[i]) == 1:
        y = Y[i]

print(x, y)