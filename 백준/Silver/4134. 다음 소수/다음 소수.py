num = int(input())

for _ in range(num):
    n = int(input())
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        prime = True
        for i in range(2, int(n ** 0.5) +1):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)
            break
        else:
            n += 1