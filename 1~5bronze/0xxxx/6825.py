a = float(input())
b = float(input())
bmi = a/(b*b)
if bmi>25:
    print("Overweight")
elif bmi>=18.5:
    print("Normal weight")
else:
    print("Underweight")