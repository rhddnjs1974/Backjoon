import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

s_arr = [0,arr[0]%m]
for i in arr[1:]:
    s_arr.append((i+s_arr[-1])%m)

t = [0]*m
for i in s_arr:
    t[i]+=1

ans = 0
for i in t:
    ans+= i*(i-1) //2
    
print(ans)