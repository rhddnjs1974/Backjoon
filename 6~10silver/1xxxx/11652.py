n = int(input())
dic = {}
ma = 0
ans = 1e20
for i in range(n):
    t = int(input())
    if t in dic:
        dic[t] +=1
    else:
        dic[t] = 1
    if dic[t]==ma:
        ans = min(ans,t)
    elif dic[t]>ma:
        ma = dic[t]
        ans = t
print(ans)