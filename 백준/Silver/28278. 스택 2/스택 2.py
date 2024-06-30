import sys

n = int(sys.stdin.readline()) 
stack = [] 
for i in range(n): 
    input = sys.stdin.readline().split() 
    if input[0] == '1':
        stack.append(int(input[-1]))
    elif input[0] == '2':
        if stack:
            print(stack.pop(-1))
            continue
        print(-1)
    elif input[0] == '3':
        print(len(stack))
    elif input[0] == '4':
        if stack:
            print(0)
            continue
        print(1)
    elif input[0] == '5':
        if stack:
            print(stack[-1])
            continue
        print(-1)