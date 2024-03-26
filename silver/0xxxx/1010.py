import math
T = int(input())
for i in range(T):
    k,n = map(int,input().split())
    print(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))