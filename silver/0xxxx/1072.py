import sys
input = sys.stdin.readline
########################################

def binary_search(target,start,end):
    ans = 0
    global Y
    global X
    while(start<=end):
        mid = (start+end)//2
        get = int((100*(Y+mid)/(X+mid)))

        if get <= target:
            start = mid+1
        else:
            end = mid-1
            ans = mid
    if ans==0:
        ans=-1
    return ans

X,Y = map(int,input().split())
Z = int(100*Y/X)

print(int(binary_search(Z,0,1e9)))
