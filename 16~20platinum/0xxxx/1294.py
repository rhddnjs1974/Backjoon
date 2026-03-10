import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(input().strip())

while True:
    t=-1
    for i in range(n):
        if len(a[i])==0:
            continue
        if t==-1 or a[i]+a[t]<a[t]+a[i]:
            t=i
    if t==-1:
        break
    print(a[t][0],end="")
    a[t]=a[t][1:]

print()