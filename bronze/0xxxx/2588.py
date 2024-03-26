a = int(input())
b = int(input())

bb = b
x = b%10
b = b//10
y = b%10
b = b//10
z = b

print(a*x)
print(a*y)
print(a*z)
print(a*bb)