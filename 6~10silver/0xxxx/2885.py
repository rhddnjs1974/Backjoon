import sys
input = sys.stdin.readline

k = int(input())

ans = 0
while(2**ans<k):
    ans+=1

print(2**ans,end=" ")

arr = []

for i in range(ans+1):
    arr.append(2**i)
arr.reverse()

ans2 = -1
for i in arr:
    if k==0:
        break
    ans2+=1
    k %= i

print(ans2)