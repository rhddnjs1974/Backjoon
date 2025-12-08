def prefix(arr): #2차원
    x = len(arr)
    y = len(arr[0])
    s_arr = [[0]*(y+1) for i in range(x+1)]
    for i in range(x):
        for j in range(y):
            s_arr[i+1][j+1] = s_arr[i+1][j] + s_arr[i][j+1] - s_arr[i][j] + arr[i][j]
    
    return s_arr # 행렬 각 첫번째 0 한줄 추가된 상태

def range_sum(parr,startx,starty,lastx,lasty): #2차원 구간합 계산
    return parr[lastx][lasty]-parr[lastx][starty-1]-parr[startx-1][lasty]+parr[startx-1][starty-1]

##############################################################################

def prefix(arr): #1차원
    s_arr = [0]
    for i in arr:
        s_arr.append(s_arr[-1]+i)
    return s_arr # 첫 칸에 0 추가된 상태

def range_sum(parr,start,last): #1차원 구간합 계산
    return parr[last]-parr[start-1]