import sys
import heapq

input = sys.stdin.readline

for testcase in range(int(input())):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    n = len(arr)
    arr0 = arr[0] % 6
    
    ffff=0
    for i in range(n):
        if arr[i] % 6 != arr0:
            print(-1)
            ffff = 1
            break
    if ffff==1:
        continue

    add6 = (-arr0) % 6
    b = [0] * n
    for i in range(n):
        b[i] = (arr[i] + add6) // 6

    C = 1
    mod = 7
    while (mod <= n) and (C < 7):
        C += 1
        mod *= 7

    pow7 = [1] * (C+1)
    pow6 = [1] * (C+1)
    for x in range(1, C+1):
        pow7[x] = (pow7[x-1] * 7)
        pow6[x] = (pow6[x-1] * 6)

    need = [0] * (C+1)
    for x in range(1, (C + 1)):
        mp = {}
        for i in range(n):
            t = (-b[i]) % pow7[x]
            v = (-b[i]) % pow6[x]
            if t not in mp:
                mp[t] = v
            elif mp[t] != v:
                mp[t] = -1
        need[x] = mp

    heap = []

    for x in range(mod):
        rm = 1
        rv = 0
        bad = 0

        for c in range(1, C+1):
            v = need[c].get(x % pow7[c], 0)
            if v == 0:
                continue
            if v == -1:
                bad = 1
                break

            if rm < pow6[c]:
                if rv % rm != v % rm:
                    bad = 1
                    break
                
                rm = pow6[c]
                rv = v
            else:
                if rv % pow6[c] != v:
                    bad = 1
                    break

        if bad == 1:
            continue

        if rm == 1:
            kk = x
        else:
            inv = pow((mod % rm), -1, rm)
            tt = (((rv - x) % rm) * inv) % rm
            kk = (x + (mod * tt))

        if len(heap) < 80: ######## 조절해가면서 쓰기
            heapq.heappush(heap, (-kk, kk, rm, rv))
        else:
            if kk < heap[0][1]:
                heapq.heapreplace(heap, (-kk, kk, rm, rv))

    if not heap:
        print(-1)
        continue

    cand = sorted(heap, key=lambda y: y[1])

    bestk = None
    bestx = None

    for idx in range(len(cand)):
        k0 = cand[idx][1]
        
        kan = mod
        for q in range(60):
            k = k0 + (kan * q)
            
            flag = 1
            for i in range(len(b)):
                x = b[i] + k
                while (x % 7) == 0:
                    if (x % 6) != 0:
                        flag = 0
                        break
                    x //= 42
            
            if flag==1:
                x = add6 + 6 * k
                if bestx is None or x < bestx:
                    bestx = x
                    bestk = k
                break

    if bestx is None:
        print(-1)
    else:
        print(bestx)

