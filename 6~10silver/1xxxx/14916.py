n = int(input())
ans =0
while(n%5!=0 and n>0):
    n-=2
    ans+=1
if n>0:
    ans += (n//5)
if n<0:
    print(-1)
else:
    print(ans)