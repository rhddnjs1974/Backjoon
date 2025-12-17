arr =[]
while(True):
    try:
        a,b,c = input().split()
        arr.append((-float(c)*int(b),-int(b),a))
    except:
        break

arr.sort()
for a,b,c in arr:
    print("$%.2f - %s/%d"%(-a,c,-b))