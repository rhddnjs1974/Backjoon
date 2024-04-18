import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(9):
    arr.append({})

ip = []

for i in range(n):
    a = input().rstrip()
    ip.append([])
    for j in a:
        ip[i].append(j)
    l = len(a)
    for j in range(l):

        if a[j] in arr[l-j-1]:
            arr[l-j-1][a[j]]+=1
        else:
            arr[l-j-1][a[j]]=1


use = {}
idx = 9

for i in range(9):
    for j in arr[i]:
        if j in use:
            use[j] += arr[i][j]*(10**i)
        else:
            use[j] = arr[i][j]*(10**i)

f = []
for i in use:
    f.append((use[i],i))

f.sort()
f.reverse()

use = {}
for i,j in f:
    use[j] = idx
    idx-=1


ans = 0
for i in ip:
    for j in range(len(i)):
        i[j] = use[i[j]]

    a = ""

    for j in i:
        a += str(j)
    ans += int(a)
print(ans)