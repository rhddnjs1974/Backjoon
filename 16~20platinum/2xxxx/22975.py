import sys
input = sys.stdin.readline

def left_key(k,j,hj,H):
    return ((hj-H[k])*4000001)//(j-k)

def right_key(i,j,hj,H):
    return ((H[i]-hj)*4000001)//(i-j)

n = int(input())
H = list(map(int,input().split()))

arr = [[] for _ in range(n)]
ans = 1

for j in range(n):
    hj = H[j]

    left = list(range(j))
    left.sort(key=lambda k: left_key(k,j,hj,H))

    right = list(range(j+1,n))
    right.sort(key=lambda i: right_key(i,j,hj,H))

    p = 0
    now = 1
    arrj = arr[j]

    for i in right:
        while p<j and (hj-H[left[p]])*(i-j) <= (H[i]-hj)*(j-left[p]):
            now = max(now,arrj[left[p]])
            p += 1

        v = now+1
        arr[i].append(v)
        
        ans = max(ans,v)

print(n-ans)