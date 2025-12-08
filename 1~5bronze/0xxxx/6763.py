a=int(input())
b=int(input())
if a>=b:
    print("Congratulations, you are within the speed limit!")
else:
    t = b-a
    if t<21:
        x=100
    elif t<31:
        x=270
    else:
        x=500
    print("You are speeding and your fine is $"+str(x)+".")