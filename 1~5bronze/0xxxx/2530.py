a,b,c = map(int,input().split())
time = a*3600 + b*60 + c
time += int(input())

print((time//3600) %24, (time%3600)//60,time%60)