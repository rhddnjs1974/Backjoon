import math
n,p = map(int, input().split())
alpha = p / 360.0

log2P = math.log2(n) + (n - 1) * math.log2(alpha)

print("%.6f"%(abs(-log2P)))