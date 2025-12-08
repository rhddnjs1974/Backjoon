while(True):
    a = int(input())
    if a==-1:
        break
    now = 0
    arr = []
    for i in range(1,a):
        if a%i==0:
            now+=i
            arr.append(i)
    
    if now==a:
        print(str(a)+" = ",end="")
        for i in range(len(arr)):
            if i==len(arr)-1:
                print(arr[i])
            else:
                print(arr[i],end=" + ")
    else:
        print(str(a)+" is NOT perfect.")