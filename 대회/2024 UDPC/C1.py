import sys
input = sys.stdin.readline

N,M,D = map(int,input().split())
test = [-1e6]*M

flag= 0
for i in range(N):
    arr= list(map(int,input().split()))
    arr.sort()
    for j in range(M):
        if test[j]>=arr[j]+D:
            print("NO")
            flag=1
            break
    if flag==1:
        break

    for j in range(M):
        test[j] = arr[j]

if flag==0:
    print("YES")