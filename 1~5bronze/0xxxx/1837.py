p, k = map(int,input().split())
a=0
flag = "GOOD"
for i in range(2,k):
    if p%i==0:
        flag = "BAD"
        a = i
        break

if a==0:
    print(flag)
else:
    print(flag,a)