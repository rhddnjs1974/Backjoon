mi = 1
ma = 1000000000
for i in range(29):
    mid = (mi+ma)//2
    a = int(input())
    if mid<a:
        print("<",flush=True)
        ma = min(ma,a-1)
    else:
        print(">",flush=True)
        mi = max(mi,a+1)
        
mid = (mi+ma)//2    
for i in range(71):
    a = int(input())
    if mid<a:
        print("<",flush=True)
    elif mid==a:
        print("=",flush=True)
    else:
        print(">",flush=True)
