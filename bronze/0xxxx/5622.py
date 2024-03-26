a = input()
arr2=["A","B","C"]
arr3=["D","E","F"]
arr4=["G","H","I"]
arr5=["J","K","L"]
arr6=["M","N","O"]
arr7=["P","Q","R","S"]
arr8=["T","U","V"]
arr9=["W","X","Y","Z"]
ans=0
for i in a:
    if i in arr2:
        ans+=3
    if i in arr3:
        ans+=4
    if i in arr4:
        ans+=5
    if i in arr5:
        ans+=6
    if i in arr6:
        ans+=7
    if i in arr7:
        ans+=8
    if i in arr8:
        ans+=9
    if i in arr9:
        ans+=10
print(ans)