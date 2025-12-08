arr = [("A+",4.5),("A0",4.0),("B+",3.5),("B0",3.0),("C+",2.5),("C0",2.0),("D+",1.5),("D0",1.0),("F",0)]
point=0
hak = 0
for i in range(20):
    a,b,c = input().split()
    b = float(b)
    for i in range(len(arr)):
        if c==arr[i][0]:
            c = arr[i][1]

    if c=="P":
        continue

    hak += b
    point += b*c

print(point/hak)