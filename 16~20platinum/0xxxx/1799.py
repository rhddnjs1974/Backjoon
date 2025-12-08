n = int(input())
arr = []
ans = 0

def bt(a,b,num,array):
    global ans,n

    for i in range(a,n):
        flag = b%2
        flag += (i-a)%2
        flag %= 2
        for j in range(flag,n,2):
            if i==a and j<b:
                continue
            if array[i][j]==1:
                array2 = [[1]*n for i in range(n)]
                for ii in range(n):
                    for jj in range(n):
                        if array[ii][jj]==0:
                            array2[ii][jj] = 0
                for ii in range(n):
                    if i+ii>=n or j+ii>=n:
                        break
                    array2[i+ii][j+ii] = 0
                for ii in range(n):
                    if i-ii<0 or j-ii<0:
                        break
                    array2[i-ii][j-ii] = 0
                for ii in range(n):
                    if i+ii>=n or j-ii<0:
                        break
                    array2[i+ii][j-ii] = 0
                for ii in range(n):
                    if i-ii<0 or j+ii>=n:
                        break
                    array2[i-ii][j+ii] = 0
                
                bt(i,j+2,num+1,array2)

    ans = max(ans,num)

    
for i in range(n):
    arr.append(list(map(int,input().split())))



bt(0,0,0,arr)
realans = ans
ans=0
bt(0,1,0,arr)

#print(realans,ans)#
print(realans+ans)