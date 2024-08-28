for i in range(int(input())):
    s = input()
    for z in s:
        s = s.replace('()', '')

    print("NO" if s else "YES")