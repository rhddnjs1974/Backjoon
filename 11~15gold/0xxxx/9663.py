import sys

def bt(x):
    global ans,n
    if x>n:
        ans +=1
        return

    for i in range(1,n+1): #i값을 arr에 넣기 (그 줄의 i칸에 퀸)
        flag = 0 # flag가 0일시 넣기
        for j in range(1,x):
            if i==arr[j]:
                flag=1
                break
            if abs(x-j)==abs(i-arr[j]):
                flag=1
                break
        if flag==0:
            arr[x] = i
            bt(x+1)
    
    
n = int(input())
arr = [0]*(n+1)
ans = 0
bt(1)
print(ans)