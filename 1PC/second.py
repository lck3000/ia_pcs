#6 numeros por jugada
#45 bolillas
import random
BALLS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45)

def write_comb():
    op = open('jugadas.txt',mode='w+')
    for a in range(1,46):
        for b in range(1,46):
            for c in range(1,46):
                for d in range(1,46):
                    for e in range(1,46):
                        for f in range(1,46):
                            if len(set([a,b,c,d,e,f]))==len([a,b,c,d,e,f]):    
                                op.write(str(a)+','+str(b)+','+str(c)+','+str(d)+','+str(e)+','+str(f)+'\n')
    op.close()

def draw(prnt=False):
    a = random.choices(BALLS,k=6)
    while len(set(a)) != len (a):
        a=random.choices(BALLS,k=6)
    if prnt:
        print(a)
    else:
        return a

draw(True)
