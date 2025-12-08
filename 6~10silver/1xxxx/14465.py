import sys
input = sys.stdin.readline

N,K,B =map(int,input().split())
dp = [0]*N
for i in range(B):
    dp[int(input())-1]=1

ans=K
def prefix(arr): #1차원
    s_arr = [0]
    for i in arr:
        s_arr.append(s_arr[-1]+i)
    return s_arr # 첫 칸에 0 추가된 상태

pre = prefix(dp)


for i in range(N-K+1):
    now = pre[i+K]-pre[i+1]
    ans= min(ans,now)
print(ans)