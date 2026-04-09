import sys
input = sys.stdin.readline

T = 75
R6 = 1.0 / 6.0

f = [[0.0] * (T+1) for _ in range(T+1)]
g = [[0.0] * (T+1) for _ in range(T+1)]

for h in range(T+1):
    f[T][h] = 1.0
    g[T][h] = 1.0

for s in range((T-1) * 2, -1, -1):
    for c in range(min(s, T-1), -1, -1):
        h = s-c
        if h > T-1:
            continue

        needc = T-c
        needh = T-h
        fc = f[c]
        gv = 0.5

        for _ in range(3):
            for _ in range(3):
                bestc = [0.0] * (needc+7)
                
                for turn in range(needc, 1, -1):
                    now = c+turn
                    hold = 1.0
                    if now != T:
                        hold = g[now][h]
                    cont = gv * R6
                    
                    for d in range(2, 7):
                        nxt = now+d
                        if nxt == T:
                            cont += R6
                        elif nxt > T:
                            cont += gv * R6
                        else:
                            cont += bestc[turn+d] * R6
                            
                    bestc[turn] = max(hold, cont)

                fv = gv * R6
                for d in range(2, 7):
                    nxt = c+d
                    if nxt == T:
                        fv += R6
                    elif nxt > T:
                        fv += gv * R6
                    else:
                        fv += bestc[d] * R6

                besth = [0.0] * (needh+7)
                
                for turn in range(needh, 1, -1):
                    now = h+turn
                    hold = 0.0
                    if now != T:
                        hold = fc[now]
                    cont = fv * R6
                    for d in range(2, 7):
                        nxt = now+d
                        if nxt > T:
                            cont += fv * R6
                        elif nxt < T:
                            cont += besth[turn+d] * R6
                            
                    besth[turn] = min(hold, cont)

                gv = fv * R6
                
                for d in range(2, 7):
                    nxt = h+d
                    if nxt > T:
                        gv += fv * R6
                    elif nxt < T:
                        gv += besth[d] * R6

            ac = [0.0] * (needc+7)
            bc = [0.0] * (needc+7)
            
            for turn in range(needc, 1, -1):
                now = c+turn
                hold = 1.0
                if now != T:
                    hold = g[now][h]
                    
                a = R6
                b = 0.0
                
                for d in range(2, 7):
                    nxt = now+d
                    if nxt == T:
                        b += R6
                    elif nxt > T:
                        a += R6
                    else:
                        a += ac[turn+d] * R6
                        b += bc[turn+d] * R6
                        
                if hold > a * gv+b:
                    bc[turn] = hold
                else:
                    ac[turn] = a
                    bc[turn] = b

            al = R6
            be = 0.0
            
            for d in range(2, 7):
                nxt = c+d
                
                if nxt == T:
                    be += R6
                elif nxt > T:
                    al += R6
                else:
                    al += ac[d] * R6
                    be += bc[d] * R6

            ah = [0.0] * (needh+7)
            bh = [0.0] * (needh+7)
            
            for turn in range(needh, 1, -1):
                now = h+turn
                hold = 0.0
                if now != T:
                    hold = fc[now]
                a = R6
                b = 0.0
                
                for d in range(2, 7):
                    nxt = now+d
                    if nxt > T:
                        a += R6
                    elif nxt < T:
                        a += ah[turn+d] * R6
                        b += bh[turn+d] * R6
                        
                if hold < a * fv+b:
                    bh[turn] = hold
                else:
                    ah[turn] = a
                    bh[turn] = b

            ga = R6
            de = 0.0
            for d in range(2, 7):
                nxt = h+d
                if nxt > T:
                    ga += R6
                elif nxt < T:
                    ga += ah[d] * R6
                    de += bh[d] * R6

            den = 1.0-al * ga
            if abs(den) > 1e-30:
                fv = (al * de+be) / den
                gv = ga * fv+de

        f[c][h] = fv
        g[c][h] = gv

q = int(input())
for _ in range(q):
    c, h, x = map(int, input().split())
    if c+x == T:
        print('H')
        continue

    gv = g[c][h]
    ph = gv
    if c+x <= T:
        if c+x == T:
            ph = 1.0
        else:
            ph = g[c+x][h]

    bestc = [0.0] * (T-c+7)
    for turn in range(T-c, 1, -1):
        now = c+turn
        hold = 1.0
        if now != T:
            hold = g[now][h]
        cont = gv * R6
        
        for d in range(2, 7):
            nxt = now+d
            if nxt == T:
                cont += R6
            elif nxt > T:
                cont += gv * R6
            else:
                cont += bestc[turn+d] * R6
                
        bestc[turn] = max(hold, cont)

    pc = gv * R6
    
    for d in range(2, 7):
        nxt = c+x+d
        if nxt == T:
            pc += R6
        elif nxt > T:
            pc += gv * R6
        else:
            pc += bestc[x+d] * R6

    if ph >= pc:
        print('H')
    else:
        print('C')