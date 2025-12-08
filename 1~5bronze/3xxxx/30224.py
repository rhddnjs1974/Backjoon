a = input()
if "7" in a:
    a = int(a)
    if a%7==0:
        print(3)
    else:
        print(2)
else:
    a = int(a)
    if a%7==0:
        print(1)
    else:
        print(0)