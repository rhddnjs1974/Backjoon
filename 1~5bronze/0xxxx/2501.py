n,m = map(int,input().split())

for i in range(1,n+1):
    if n%i==0:
        m-=1
        if m==0:
            print(i)
            break
        
if m!=0:
    print(0)