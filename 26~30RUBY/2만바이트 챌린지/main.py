import sys
def make0(w):
    w("BOJ 20000")
def make1(w):
    w('#include <cstdio>\nint main(){\n    int N;\n    scanf("%d",&N);\n')
    for i in range(1, 20001):
        if i == 1:
            w('    if(N==1){\n        puts("4");\n    }\n')
        else:
            w(f'    else if(N=={i}){{\n        puts("{i*4}");\n    }}\n')
    w('    else{\n        puts("Still working on it...");\n    }\n    return 0;\n}\n')
def make2(w):
    s="kjoonOnlineJudge!"
    for i in range(1,1<<17): w("BaBeBaB"+s[(i&-i).bit_length()-1])
    w("BaBeBaB\n")

p = sys.stdout.write
n = int(input())
if n==0:
    make0(p)
if n==1:
    make1(p)
if n==2:
    make2(p)
    