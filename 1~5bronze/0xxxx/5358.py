while(True):
    try:
        a = input()
        b = ""
        for i in a:
            if i=="i":
                b+="e"
            elif i=="e":
                b+="i"
            elif i=="I":
                b+="E"
            elif i=="E":
                b+="I"
            else:
                b+=i
        print(b)
    except:
        break