n = int(input())
arr = []
for i in range(n):
    arr.append(input())

def s_n(array):
    t = 0
    for i in array:
        if i.isdigit():
            t+=int(i)
    return t
arr.sort(key = lambda x:(len(x), s_n(x), x))
for i in arr:
    print(i)