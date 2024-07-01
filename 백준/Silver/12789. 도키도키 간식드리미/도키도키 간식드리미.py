N = int(input())
students = list(map(int, input().split()))

stack = []
next = 1

for student in students:
    stack.append(student)
    while stack and stack[-1] == next:
        stack.pop()
        next += 1

if stack:
    print("Sad")
else:
    print("Nice")