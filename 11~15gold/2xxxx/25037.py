from random import choice, shuffle
from math import log2, ceil

Q1 = 0
Q2 = 1

class Student:
    def __init__(self, n):
        self.__n = n
        self.__S = [choice([Q1, Q2]) for i in range(n)]
        self.__asked = 0
        self.__askedmax = n + ceil(n * log2(n)) 
        # add 1 for testing if it gets to max value when printing out the result
        
        self.__askseq = list(range(n))
        shuffle(self.__askseq)
        
    def ask(self, Q):
        assert type(Q) == list and len(Q) == self.__n

        if self.__asked >= self.__askedmax:
            assert False, "Maximum number of ask used."
            
        for q in Q:
            assert q in [Q1, Q2], "Something different from Q1 and Q2 is contained in Q."
        
        self.__asked += 1
        A = []
        for i in range(self.__n):
            if Q[ self.__askseq[i] ] == self.__S[i]:
                A.append('YES')
            else:
                return A
        return A
    
    def n(self):
        return self.__n

    def seq(self, seq):
        return self.__askseq == seq

######### SUBMIT THE BELOW CODE ONLY #########

def question(student):
    n = student.n()
    S = [0]*n  
    seq = [-1]*n  
    owner = [-1]*n  

    for k in range(n):
        J = [j for j in range(n) if owner[j] == -1]

        Q = [0]*n
        for j in range(n):
            if owner[j] != -1:
                Q[j] = S[owner[j]]
        if len(student.ask(Q)) > k:
            S[k] = 0 
        else:
            S[k] = 1

        cand = J
        while len(cand) > 1:
            mid = len(cand)//2
            left = cand[:mid]
            leftset = set(left)

            Q = [0]*n
            for j in range(n):
                if owner[j] != -1:
                    Q[j] = S[owner[j]]
                else:
                    if j in leftset:
                        Q[j] = S[k]  
                    else:
                        Q[j] = 1 - S[k]

            if len(student.ask(Q)) > k:
                cand = left
            else:
                cand = cand[mid:]

        idx = cand[0]
        seq[k] = idx
        owner[idx] = k

    Q = [0]*n
    for j in range(n):
        Q[j] = S[owner[j]]
    return Q, seq

######### SUBMIT THE ABOVE CODE ONLY #########

S = Student(3)
Q, seq = question(S)
print(len(S.ask(Q)), S.seq(seq)) # 3 True

S = Student(5)
Q, seq = question(S)
print(len(S.ask(Q)), S.seq(seq)) # 5 True

S = Student(7)
Q, seq = question(S)
print(len(S.ask(Q)), S.seq(seq)) # 7 True
