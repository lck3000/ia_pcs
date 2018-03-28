# -*- coding: cp1252 -*-

def cube_checker(num):
    if (num % 3) == 0:
        cycles=0
        while num != 153:
            p1 = 0
            numst = str(num)
            for it in numst:
                p1 += pow(int(it),3)
            cycles += 1
            num = p1
        return cycles
    else:
        print("La propiedad del número 153 solo se cumple para números multiplos de 3")
        pass

print(cube_checker(40))