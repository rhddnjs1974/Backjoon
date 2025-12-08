import sys
import math
input = sys.stdin.readline

mod = 1000007
w,h = map(int,input().split())
x,y = map(int,input().split())

a = math.comb(x+y-1-1,y-1)%mod
b = math.comb(w-x+h-y,h-y)%mod
print((a*b)%mod)