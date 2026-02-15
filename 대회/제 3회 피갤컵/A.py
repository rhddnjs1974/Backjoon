N = int(input())
S = input()
target = "eagle"

ans = 1000
for i in range(N - 4):
    x = 0
    for j in range(5):
        if S[i + j] != target[j]:
            x += 1
    ans = min(ans,x)

print(ans)
