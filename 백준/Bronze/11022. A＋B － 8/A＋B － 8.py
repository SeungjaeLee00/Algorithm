n=int(input())
sum=0
for i in range(n):
    sum+=1
    a,b=input().split()
    c=int(a)+int(b)
    print("Case #%d: %d + %d = %d" %(sum,int(a),int(b),c))