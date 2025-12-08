import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################
N,M = map(int,input().split())
arr= [0]+list(map(int,input().split()))

s_arr = [0]*(N+1)

for i in range(1,N+1):
    s_arr[i] = s_arr[i-1] + arr[i]

for i in range(M):
    a,b = map(int,input().split())
    print(s_arr[b]-s_arr[a-1])