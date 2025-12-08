while(True):
    a = input()
    if a=="0":
        break
    a = float(a)
    print("%.2f"%(1+a+a*a+a*a*a+a*a*a*a))