import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))


def rot(L):
    a[:L] = a[L-2:L] + a[:L-2]
    ans.append(L - 1)
    
    
inv = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            inv += 1

if inv%2 == 1:
    print("NO")
else:
    ans = []

    L = n
    while L >= 3:
        if a[L - 1] == L:
            L -= 1
            continue
        
        # L 홀수
        
        if L % 2 == 1:
            while a[L - 1] != L:
                rot(L)
            L -= 1
            continue
        
        # L 짝수
        
        for i in range(L):
            if a[i] == L:
                pos = i + 1
                break

        if pos % 2 == 1:
            while True:
                pos = 0
                for i in range(L):
                    if a[i] == L:
                        pos = i + 1
                        break

                if pos % 2 == 0:
                    break
                rot(L - 1)

        if pos != L:
            while a[L - 1] != L:
                rot(L)

        L -= 1

    if a != list(range(1, n + 1)):
        print("NO")
    else:
        print("YES")
        print(len(ans))
        print(*ans)