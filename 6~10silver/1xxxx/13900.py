n = int(input())
ans,now = 0,0
for i in list(map(int,input().split())):
    ans+= now*i
    now +=i
print(ans)