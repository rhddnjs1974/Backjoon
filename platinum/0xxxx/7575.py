import sys
input = sys.stdin.readline

def make_pi(pattern):
    l = len(pattern)
    arr = [0 for _ in range(l)]

    pidx = 0
    for idx in range(1, l):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = arr[pidx - 1]

        if pattern[idx] == pattern[pidx]:
            pidx += 1
            arr[idx] = pidx

    return arr


def KMP(word, pattern):
    pi_table = make_pi(pattern)

    results = []
    pidx = 0

    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = pi_table[pidx - 1]

        if word[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                results.append(idx - len(pattern) + 2)
                pidx = pi_table[pidx]
            else:
                pidx += 1
    return results

n,k = map(int,input().split())
A = []
for i in range(n):
    m = int(input())
    A.append(list(map(int,input().split())))

ans = 0
for i in range(len(A[0])-k+1):
    B = A[0][i:i+k]
    C = B[::-1]
    flag = 0
    for j in range(1,n):
        if not KMP(A[j],B) and not KMP(A[j],C):
            flag=1
    if flag==0:
        ans=1
        break
if ans==1:
    print('YES')
else:
    print("NO")