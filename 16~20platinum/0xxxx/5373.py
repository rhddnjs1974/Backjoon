import sys
input = sys.stdin.readline

FACE_VEC = {
    'U': (0, 1, 0),
    'D': (0, -1, 0),
    'F': (0, 0, 1),
    'B': (0, 0, -1),
    'L': (-1, 0, 0),
    'R': (1, 0, 0),
}

FACE_COLOR = {'U': 'w', 'D': 'y', 'F': 'r', 'B': 'o', 'L': 'g', 'R': 'b'}

def rot_x(p, s):
    x, y, z = p
    if s == 1:
        return (x, z, -y)
    else:
        return (x, -z, y)

def rot_y(p, s):
    x, y, z = p
    if s == 1:
        return (z, y, -x)
    else:
        return (-z, y, x)

def rot_z(p, s):
    x, y, z = p
    if s == 1:
        return (y, -x, z)
    else:
        return (-y, x, z)

def rotate(p, axis, s):
    if axis == 'x':
        return rot_x(p, s)
    if axis == 'y':
        return rot_y(p, s)
    return rot_z(p, s)

MOVE_AXIS_SIGN = {
    'U': ('y', -1),
    'D': ('y', 1),
    'F': ('z', 1),
    'B': ('z', -1),
    'L': ('x', -1),
    'R': ('x', 1),
}


T = int(input())
for _ in range(T):
    n = int(input())
    ops = input().split()
    st = {}

    for cx in (-1, 0, 1):
        for cy in (-1, 0, 1):
            for cz in (-1, 0, 1):
                if cx == cy == cz == 0:
                    continue
                if cy == 1:
                    st[(cx, cy, cz, 0, 1, 0)] = 'w'
                if cy == -1:
                    st[(cx, cy, cz, 0, -1, 0)] = 'y'
                if cz == 1:
                    st[(cx, cy, cz, 0, 0, 1)] = 'r'
                if cz == -1:
                    st[(cx, cy, cz, 0, 0, -1)] = 'o'
                if cx == -1:
                    st[(cx, cy, cz, -1, 0, 0)] = 'g'
                if cx == 1:
                    st[(cx, cy, cz, 1, 0, 0)] = 'b'

    for op in ops:
        face = op[0]
        dirc = op[1]

        axis, base = MOVE_AXIS_SIGN[face]
        s = base if dirc == '+' else -base

        nx, ny, nz = FACE_VEC[face]

        def in_layer(cx, cy, cz):
            if face == 'U':
                return cy == 1
            if face == 'D':
                return cy == -1
            if face == 'F':
                return cz == 1
            if face == 'B':
                return cz == -1
            if face == 'L':
                return cx == -1
            return cx == 1

        moved = {}
        stay = {}

        for key, col in st.items():
            cx, cy, cz, fx, fy, fz = key
            if in_layer(cx, cy, cz):
                nc = rotate((cx, cy, cz), axis, s)
                nf = rotate((fx, fy, fz), axis, s)
                moved[(nc[0], nc[1], nc[2], nf[0], nf[1], nf[2])] = col
            else:
                stay[key] = col

        stay.update(moved)
        st = stay

    result = []
    for z in (-1, 0, 1):
        row = []
        for x in (-1, 0, 1):
            row.append(st[(x, 1, z, 0, 1, 0)])
        result.append(''.join(row))
    
    for pp in result[0]:
        print(pp,end="")
    print()
    for pp in result[1]:
        print(pp,end="")
    print()
    for pp in result[2]:
        print(pp,end="")
    print()