n = int(input())
mi = 1
ma = n
for i in range(50):
    mid = (mi+ma)//2
    print("?",mid)
    a = int(input())
    if a==0:
        print("=",mid)
        break
    if a==1:
        ma = mid-1
    else:
        mi = mid+1