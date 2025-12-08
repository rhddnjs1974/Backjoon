m,n,q = map(int,input().split())
arr = [0]+list(map(int,input().split()))

ans = []

for i in range(1,m+1):
    print("?",i,i,flush=True)
    x = int(input())
    ans.append((x)%(arr[i])+1)

for i in range(n-len(ans)):
    ans.append(1)

print("!",*ans,flush=True)