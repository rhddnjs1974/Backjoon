import sys
input = sys.stdin.readline

T = int(input())

for test in range(T):
    N = int(input())
    
    arr = []
    
    for i in range(N):
        a = input().rstrip()
        arr.append(a)
    
    if "CodeRace" in arr and "Chung-Ang_Programming_Contest" in arr:
        print(2017)
    elif "CodeRace" in arr and "SCAL-MOOKJA" in arr:
        print(2018)
    elif "Newbie_Programming_Contest" in arr and "Chung-Ang_Programming_Contest" in arr:
        print(2019)
    elif "Chung-Ang_Programming_Contest" in arr and len(arr)==1:
        print(2020)
    elif "Newbie_Programming_Challenge" in arr and len(arr)==1:
        print(2021)
    elif "ChAOS_Hello{Year}_Algorithm_Contest" in arr and "Chung-Ang_Programming_Contest" in arr:
        print(2022)
    elif "Kookmin_Chung-Ang_Programming_Contest" in arr and "ChAOS_Hello{Year}_Algorithm_Contest" in arr:
        print(2023)
    elif "Kookmin_Chung-Ang_Programming_Contest" in arr and "Chung-Ang_Programming_Contest" in arr:
        print(2024)
    elif "Centroid_Cup" in arr and "Chung-Ang_Programming_Contest" in arr:
        print(2025)
    else:
        print("Goodbye, ChAOS!")
        