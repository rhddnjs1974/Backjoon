import random
arr = [[0]*14 for i in range(8)]

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
def dfs(x,y,i,l,t):
    if i==l:
        return 1
    xxx = 0
    for d in range(8):
        nx = x+dx[d]
        ny = y+dy[d]
        if nx<0 or nx>=8 or ny<0 or ny>=14:
            continue
        if arr[nx][ny]==t[i]:
            xxx = max(xxx,dfs(nx,ny,i+1,l,t))
            if xxx==1:
                break

    return xxx

def test(n):
    q = str(n)
    
    t = []
    for i in q:
        t.append(int(i))
    
    flag=0
    for i in range(8):
        for j in range(14):
            if arr[i][j]==t[0]:
                if dfs(i,j,1,len(t),t)==1:
                    flag=1
                    break
        if flag==1:
            break
    return flag


def permute_digits(data: str) -> str:

    # 0~9 숫자 순열 만들기
    p = list(range(10))
    random.shuffle(p)
    
    # 각 자리의 숫자 k → p[k] 로 치환
    res = ''.join(str(p[int(ch)]) for ch in data)
    return res



###################################################위는 체크용 함수


now = '9210275311246026897134760375736458425897885110268925124638930217913923827935540358511046693086401514321427712207'
for i in range(8):
    for j in range(14):
        arr[i][j] = int(now[i*14+j])
        
for fcase in range(1,8141):
    if test(fcase)==0:
        break
print(fcase)

f2 = 0
for xx in range(200000):
    if xx%100==0:
        print(xx,f2)
    now = permute_digits(now)
    
    for i in range(8):
        for j in range(14):
            arr[i][j] = int(now[i*14+j])
            
    for nowcase in range(1,8141):
        if test(nowcase)==0:
            break
    
    f2 = max(f2,nowcase)
    
    if nowcase>fcase:
        print(now)
        break

print(f2)
exit()
