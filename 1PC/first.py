# -*- coding: cp1252 -*-
import pandas as pd

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

#print(cube_checker(40))
df=pd.DataFrame(columns=['num','ciclos'])

for x in range(1,100000,1):
    df.at[x,'num'] = x*3
    df.at[x,'ciclos'] = cube_checker(x*3)

df.to_excel('cubo153.xlsx')
    

