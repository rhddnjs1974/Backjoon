import sys
input = sys.stdin.readline

def calcu(x):
    if x <= 1:
        return (1, 0, 1)
    
    y = 0
    z = sp[x]
    while x % z == 0:
        x //= z
        y += 1
    if x != 1:
        return (0, 0, 0)
    
    return (1, z, y)

MA = 1000000

sp = list(range(MA + 1))

p = 2
while p*p <= MA:
    if sp[p] == p:
        j = p*p
        while j <= MA:
            if sp[j] == j:
                sp[j] = p
            j += p
    p += 1

for testcase in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    ok = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            ok = False
            break
    if ok:
        print("Bob")
        continue

    flag = 0
    for x in arr:
        a,b,c = calcu(x)
        if a == 0:
            flag = 1
            break
        
    if flag == 1:
        print("Alice")
        continue

    now = 0
    ok2 = True
    for x in arr:
        a,b,c = calcu(x)
        for _ in range(c):
            if now > b:
                ok2 = False
                break
            now = b
        if not ok2:
            break

    if ok2:
        print("Bob")
    else:
        print("Alice")
