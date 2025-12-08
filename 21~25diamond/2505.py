import sys
input = sys.stdin.readline

def ERROR():
    error = []
    for i in range(1,n+2):
        if arr[i]-arr[i-1]!=1 and arr[i]-arr[i-1]!=-1:
            error.append((i-1,i))
    for i in range(1,n+1):
        if arr[i-1]<arr[i]<arr[i+1] or arr[i+1]<arr[i]<arr[i-1]:
            continue
        else:
            error.append((i,i))
    return error

def bt(N):
    e_arr = ERROR()
    if len(e_arr)==0:
        for i in range(2-len(ans)):
            ans.append((1,1))
        for i in ans:
            print(*i)
        exit()
    if N==2:
        return
    
    for i in range(len(e_arr)):
        for j in range(len(e_arr)):
            x = e_arr[i][1]
            y = e_arr[j][0]
            if x>y:
                continue
            arr2 = []
            for k in range(y,x-1,-1):
                arr2.append(arr[k])
            for k in range(x,y+1):
                arr[k] = arr2[k-x]
            ans.append((x,y))
            bt(N+1)
            for k in range(y,x-1,-1):
                arr[k] = arr2[y-k]
            ans.pop()
    
n = int(input())
arr = [0]+list(map(int,input().split()))+[n+1]
ans =[]
bt(0)