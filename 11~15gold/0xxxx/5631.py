import bisect
aa=0
while(True):
    aa+=1
    n = int(input())
    if n==0:
        break
    
    arr = []
    for i in range(n):
        x,y = map(int,input().split())
        arr.append((x,y))

    ax,ay,bx,by,q = map(int,input().split())

    dista = []
    distb = []
    for i,j in arr:
        dista.append( (ax-i)**2 + (ay-j)**2 )
        distb.append( (bx-i)**2 + (by-j)**2 )

    dista.sort()
    distb.sort()

    ans = []
    for i in range(q):
        x,y = map(int,input().split())
        a = bisect.bisect_right(dista,x*x)
        b = bisect.bisect_right(distb,y*y)

        ans.append(max(0,n-a-b))
    print("Case "+str(aa)+":")
    for i in ans:
        print(i)