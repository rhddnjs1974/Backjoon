d,p,q = map(int,input().split())
a = max(p,q)
b = min(p,q)

ans = 1e15
for i in range((d//a) +1):
    x = d-a*i
    t = x//b
    s = x%b
    if s==0:
        ans=0
    else:
        ans = min(ans,b-s)
ans = min (ans, (a-(d%a)) %a  )
print(d+ans)