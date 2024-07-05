import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))

people.sort()
aws = 0

for i in range(1, n+1):
    aws += sum(people[0:i])
    
print(aws)