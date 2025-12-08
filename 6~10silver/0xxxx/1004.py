for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())

    ans = 0
    for _ in range(int(input())):
        cx,cy,r = map(int,input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        r = r*r
        
        if r>d1 and r>d2:
            continue
        if r>d1:
            ans+=1
        elif r>d2:
            ans+=1
    print(ans)