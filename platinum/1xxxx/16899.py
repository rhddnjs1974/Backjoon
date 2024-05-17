import sys
input = sys.stdin.readline

def xor_1_to_n(n):
    if n%4==0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n+1
    if n % 4 == 3:
        return 0

n = int(input())
arr= []
for i in range(n):
    x,m = map(int,input().split())
    arr.append((x,m))

a = 0
for i,j in arr:
    t = xor_1_to_n(i+j-1)^xor_1_to_n(i-1)
    a^=t

if a==0:
    print("cubelover")
else:
    print("koosaga")