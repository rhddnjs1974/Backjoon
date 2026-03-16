

def push(x,left,right):
    if not arr[x]:
        arr[x].append([left,right])
        return
    
    copyarr = []
    now = 0

    f=0
    while(arr[x]):
        i,j = arr[x].pop()
        if j<left:
            arr[x].append((i,j))
            arr[x].append((left,right))
            f=1
            break
        
        if right<i:
            copyarr.append((i,j))
            continue
        
        left = min(i,left)
        right = max(j,right)

        now+=1
    
    if f==0:
        arr[x].append((left,right))
    
    while(copyarr):
        i,j = copyarr.pop()
        arr[x].append((i,j))

mm = 50000 ##############
arr = [[] for i in range(mm*2)]

n = int(input())
for i in range(n):
    a,b,c,d = map(int,input().split())
    for x in range(a,c):
        push(x+mm,b,d)
    
ans = 0
for i in range(mm*2):
    for a,b in arr[i]:
        ans+=(b-a)


print(ans)