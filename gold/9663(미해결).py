N = int(input())
arr = [[0]*N for i in range(N)]

ans = 0

def bt(n,a,b):
    global N
    global ans
    if n==0:
        ans+=1
        return

    for i in range(a,N):
        for j in range(N):
            if i==a and j<b:
                continue

            if arr[i][j] == 0:
                flag = 0
                for k in range(1,N):
                    if i+k<N and j+k<N and arr[i+k][j+k] == 1:
                        flag= 1
                        break
                    if i+k<N and j-k>=0 and arr[i+k][j-k] == 1:
                        flag= 1
                        break
                    if i-k>=0 and j+k<N and arr[i-k][j+k] == 1:
                        flag= 1
                        break
                    if i-k>=0 and j-k>=0 and arr[i-k][j-k] == 1:
                        flag= 1
                        break
                    if i+k<N and arr[i+k][j] == 1:
                        flag= 1
                        break
                    if j+k<N and arr[i][j+k] == 1:
                        flag = 1
                        break
                    if i-k>=0 and arr[i-k][j] == 1:
                        flag= 1
                        break
                    if j-k>=0 and arr[i][j-k] == 1:
                        flag = 1
                        break


                if flag==0:
                    arr[i][j] = 1
                    bt(n-1,i,j)
                    arr[i][j] = 0

    return


bt(N,0,0)
print(ans)