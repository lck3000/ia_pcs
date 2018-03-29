#6 numeros por jugada
#45 bolillas

lista = []


for a in range(1,46):
    for b in range(1,46):
        for c in range(1,46):
            for d in range(1,46):
                for e in range(1,46):
                    for f in range(1,46):
                        lista.append([a,b,c,d,e,f])

print(lista)