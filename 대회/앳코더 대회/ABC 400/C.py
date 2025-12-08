import math

N = int(input())
count = 0
a = 1

while True:
    pow2 = 2 ** a
    if pow2 > N:
        break
    max_b = int(math.isqrt(N // pow2))
    if max_b%2==0:
        count += max_b//2
    else:
        count += max_b//2
        count +=1
    
    a += 1

print(count)