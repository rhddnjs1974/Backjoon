t=0
while(True):
    t+=1
    x = map(int,input().split())
    
    a,*arr = x
    
    if a==0:
        break
    
    if a%2==1:
        x = arr[a//2]
    else:
        x = arr[(a-1)//2]+arr[a//2]
        x /= 2
    
    print("Case %d: %.1f"%(t,x))