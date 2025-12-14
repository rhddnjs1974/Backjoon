import re

n = int(input())
rr = '[A-F]?A+F+C+[A-F]?'
p = re.compile(rr)

for i in range(n):
    sign = input()
    if p.fullmatch(sign):
        print("Infected!")
    else:
        print("Good")