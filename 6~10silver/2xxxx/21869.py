N = int(input())

ans = N
ans += max(0,N-2)

print(ans)
for i in range(1,N+1):
    print(1,i)

for i in range(2,N):
    print(N,i)

