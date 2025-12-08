import sys
import math
input = sys.stdin.readline
n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
diff=[]
for i in range(1,n):
    diff.append(arr[i]-arr[i-1])

g = diff[0]
for i in range(n-1):
    g = math.gcd(diff[i],g)
ans = 0

for i in diff:
    ans += i//g
    ans -=1
print(ans)