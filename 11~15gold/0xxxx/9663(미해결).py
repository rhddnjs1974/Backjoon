N = int(input())
arr = [[0]*N for i in range(N)]

ans = 0

def bt(n,a):
    global N
    global ans
    if n==0:
        ans+=1
        return

    i = a+1
    for j in range(N):
        flag = 0
        for k in range(1,a+2):
            if i-k>=0 and j+k<N and arr[i-k][j+k] == 1:
                flag= 1
                break
            if i-k>=0 and j-k>=0 and arr[i-k][j-k] == 1:
                flag= 1
                break
            if i-k>=0 and arr[i-k][j] == 1:
                flag= 1
                break

        if flag==0:
            arr[i][j] = 1
            bt(n-1,i)
            arr[i][j] = 0

    return

bt(N,-1)
print(ans)