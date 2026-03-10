import sys
input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())
a.sort()
b.sort()
b.reverse()

n = len(a)

del a[((n+1)//2):]
del b[(n//2):]

al = 0
ar = len(a)-1
bl = 0
br = len(b)-1

ans = [''] * n
l = 0
r = n-1

for i in range(n):
    if i%2==0:
        if bl > br or a[al] < b[bl]:
            ans[l] = a[al]
            al += 1
            l += 1
        else:
            ans[r] = a[ar]
            ar -= 1
            r -= 1
    else:
        if al > ar or b[bl] > a[al]:
            ans[l] = b[bl]
            bl += 1
            l += 1
        else:
            ans[r] = b[br]
            br -= 1
            r -= 1

for i in range(n):
    print(ans[i], end='')
print()