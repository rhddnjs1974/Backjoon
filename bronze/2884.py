H,M = map(int,input().split())
time = (H*60 + M - 45)%1440

print(time//60,time%60)