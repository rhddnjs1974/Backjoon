n = int(input())
flag=0
for i in range(1,n+1):
    x = str(i)
    t = i
    
    for a in x:
        t+=int(a)
    
    if t==n:
        print(i)
        flag=1
        break

if flag==0:
    print(0)