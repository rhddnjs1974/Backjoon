import sys
input = sys.stdin.readline

a = input().rstrip()
t = input().rstrip()

n = len(a)
ra = a[::-1]

l = 0
r = len(t)-1

left = []
right = []

turn = 0

while l <= r:
    if turn == 0:
        left.append(t[l])
        l += 1
        if len(left) >= n:
            ok = True
            i = 0
            while i < n:
                if left[len(left)-n+i] != a[i]:
                    ok = False
                    break
                i += 1
            if ok:
                i = 0
                while i < n:
                    left.pop()
                    i += 1
                turn = 1
    else:
        right.append(t[r])
        r -= 1
        if len(right) >= n:
            ok = True
            i = 0
            while i < n:
                if right[len(right)-n+i] != ra[i]:
                    ok = False
                    break
                i += 1
            if ok:
                i = 0
                while i < n:
                    right.pop()
                    i += 1
                turn = 0

while right:
    left.append(right.pop())
    if len(left) >= n:
        ok = True
        i = 0
        while i < n:
            if left[len(left)-n+i] != a[i]:
                ok = False
                break
            i += 1
        if ok:
            i = 0
            while i < n:
                left.pop()
                i += 1

for x in left:
    print(x, end="")
print()