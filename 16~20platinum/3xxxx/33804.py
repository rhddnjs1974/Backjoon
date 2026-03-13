import sys
input=sys.stdin.readline

n=int(input())

x=1
k=0
while x<n:
    x *= 2
    k += 1

if x!=n:
    print(0)
    exit()

print(1)
for i in range(n):
    for j in range(n):
        t=i^j
        ans=0
        for _ in range(k):
            ans = ans*2+(t%2)
            t //= 2
        print(ans+1,end=" ")
    print()