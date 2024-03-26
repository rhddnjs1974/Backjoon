import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################


N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split()))+[0,0,0])
for i in range(3):
    arr.append([0]*M)

ans = 0
for i in range(N):
    for j in range(M):

        try:
           point = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
        except:
           point=0
        ans = max(ans,point)

        try:
           point = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
        except:
           point=0
        ans = max(ans,point)


        ################################ ^ 직선

        try:
           point = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
        except:
           point=0
        ans = max(ans,point)

        ################################ ^ 네모

        try:
            point = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
        except:
            point = 0
        ans = max(ans, point)


        try:
            point = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+2]
        except:
            point = 0
        ans = max(ans, point)


        try:
            point = arr[i][j] + arr[i][j-1] + arr[i][j-2] + arr[i+1][j-2]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i][j-1] + arr[i][j-2] + arr[i-1][j-2]
        except:
            point = 0
        ans = max(ans, point)


        try:
            point = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i-1][j] + arr[i-2][j] + arr[i-2][j+1]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i-1][j] + arr[i-2][j] + arr[i-2][j-1]
        except:
            point = 0
        ans = max(ans, point)


        ################################ ^ L자

        try:
            point = arr[i][j] + arr[i][j + 1] + arr[i+1][j + 1] + arr[i + 1][j + 2]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i][j + 1] + arr[i-1][j + 1] + arr[i - 1][j + 2]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i + 2][j - 1]
        except:
            point = 0
        ans = max(ans, point)


        ################################ ^ ㄹ자

        try:
            point = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i][j + 2]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i+1][j] + arr[i + 1][j + 1] + arr[i+2][j]
        except:
            point = 0
        ans = max(ans, point)

        try:
            point = arr[i][j] + arr[i+1][j] + arr[i + 1][j - 1] + arr[i+2][j]
        except:
            point = 0
        ans = max(ans, point)



print(ans)