import sys
input = sys.stdin.readline

a11,a10,a9,a8,a7,a6,a5,a4,a1,a2,a3 = map(int,input().split())


for x11 in range(a11):
    for x10 in range(a10):
        for x9 in range(a9):
            for x8 in range(a8):
                for x7 in range(a7):
                    for x6 in range(a6):
                        for x5 in range(a5):
                            for x4 in range(a4):
                                for x1 in range(a1):
                                    for x2 in range(a2):
                                        x = list(map(int,input().split()))
                                        if x1==x2==x4==x5==x6==x7==x8==x9==x10==x11==0:
                                            start = x[0]
                                        
                                        for x3 in range(a3):
                                            if (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11)%2==0 and x[x3]!=start:
                                                print("No")
                                                exit()
                                            if (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11)%2==1 and x[x3]==start:
                                                print("No")
                                                exit()
                                    
print("Yes")