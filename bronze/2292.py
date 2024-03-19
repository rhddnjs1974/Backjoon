now = 1
ans = 1
N = int(input())
while(now<N):
    now+=(ans*6)
    ans+=1
print(ans)