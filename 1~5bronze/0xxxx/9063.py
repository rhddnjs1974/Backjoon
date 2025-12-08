n = int(input())
mix = 1e9
miy = 1e9
maxx = -1e9
may = -1e9
for i in range(n):
    a,b = map(int,input().split())
    mix = min(mix,a)
    maxx = max(maxx,a)
    miy = min(miy,b)
    may = max(may,b)
    
print( (may-miy)*(maxx-mix) )
