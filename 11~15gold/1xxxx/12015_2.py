import sys
input = sys.stdin.readline
import bisect

n = int(input())
arr = list(map(int,input().split()))

now = []
for i in arr:
    t = bisect.bisect_left(now,i)
    if len(now)<=t:
        now.append(i)
    else:
        now[t] = i
print(len(now))