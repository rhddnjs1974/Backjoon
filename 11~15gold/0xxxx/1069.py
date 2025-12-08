x,y,d,t = map(int,input().split())
dist = (x**2 + y**2)**0.5

if t>=d:
    print(dist)
else:
    distt = dist%d
    ans=(dist//d)*t
    anshubo = ans+t
    ans+=min(distt,d-distt+t)
    ans = min(ans,max(anshubo,t*2))
    print(ans)
    
    
    