n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(input())
    
mi = 1e9

def Bcount(a,b):
    count=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if arr[a+i][b+j]=="W":
                    count+=1
            else:
                if arr[a+i][b+j]=="B":
                    count+=1
    return count

def Wcount(a,b):
    count=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if arr[a+i][b+j]=="B":
                    count+=1
            else:
                if arr[a+i][b+j]=="W":
                    count+=1
    return count
   
for i in range(n-7):
    for j in range(m-7):
        mi = min(mi,Bcount(i,j))
        mi = min(mi,Wcount(i,j))
        
print(mi)