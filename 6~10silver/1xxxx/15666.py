import itertools

def bt(now,x,num): #x개 채움 숫자 num까지 씀
    global m
    if x>=m:
        if x==m:
            ans.append(now)
        return
    for i in range(num+1,10001):
        if numarr[i]!=0:
            for j in range(0,m-x+1):
                bt(now+(","+str(i))*j,x+j,i)
            return    

n,m = map(int,input().split())
arr = list(map(int,input().split()))
numarr = [0]*10001
for i in arr:
    numarr[i]+=1
ans = []
bt("",0,0)


for i in range(len(ans)):
    x = ans[i].split(",")
    for j in range(1,len(x)):
        x[j] = int(x[j])
    ans[i] = x[1:]
    
ans.sort()

for i in ans:
    print(*i)