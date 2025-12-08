n,m = map(int,input().split())

def prefix(arr):
    x = len(arr)
    y = len(arr[0])
    s_arr = [[0]*(y+1) for i in range(x+1)]
    for i in range(x):
        for j in range(y):
            s_arr[i+1][j+1] = s_arr[i+1][j] + s_arr[i][j+1] - s_arr[i][j] + arr[i][j]
    
    return s_arr # 행렬 각 첫번째 0 한줄 추가된 상태

def range_sum(parr,startx,starty,lastx,lasty):
    return parr[lastx][lasty]-parr[lastx][starty-1]-parr[startx-1][lasty]+parr[startx-1][starty-1]

arr = [[0]*(n+1) for i in range(n+1)]


for i in range(m):
    r,c = map(int,input().split())
    arr[r][c] = 1

pre = prefix(arr)

ans = m

    
for a in range(1,int(m**0.5)+1):
    
    if m%a==0:
        x = a
        y = m//a
        count = 0
        for i in range(1,n-x+3):
            for j in range(1,n-y+3):
                count=max(count,range_sum(pre,i,j,i+x-1,j+y-1))

        ans = min(ans,m-count)
print(ans)