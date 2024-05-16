import sys
input = sys.stdin.readline

n = int(input())
arr= list(map(int,input().split()))

a = 0
for i in arr:
    a^=i

if a==0:
    print(0)
else:
    ans = 0
    for i in arr:
        b = a^i
        for j in range(i):
            if b^j==0:
                ans+=1
    print(ans)