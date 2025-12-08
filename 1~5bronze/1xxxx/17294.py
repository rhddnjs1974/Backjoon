A = list(map(int, list(input())))
if len(A) == 1 :
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else :
    x = int(A[0]) - int(A[1])
    for i in range(len(A)-1) :
        if A[i] - A[i+1] != x :
            print('흥칫뿡!! <(￣ ﹌ ￣)>')        
            break
    else : 
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')