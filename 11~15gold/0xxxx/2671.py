import re

sign = input()
p = re.compile('(100+1+|01)+')

if p.fullmatch(sign):
    print("SUBMARINE")
else:
    print("NOISE")