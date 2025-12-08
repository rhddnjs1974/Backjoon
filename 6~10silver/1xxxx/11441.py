def prefix(arr): #1차원
    s_arr = [0]
    for i in arr:
        s_arr.append(s_arr[-1]+i)
    return s_arr # 첫 칸에 0 추가된 상태

def range_sum(parr,start,last): #1차원 구간합 계산
    return parr[last]-parr[start-1]

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
pre = prefix(arr)
for _ in range(m):
    a,b = map(int,input().split())
    print(range_sum(pre,a,b))