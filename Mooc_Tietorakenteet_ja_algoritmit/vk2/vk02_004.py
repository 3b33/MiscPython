'''
Annettuna on taulukko, jossa on n kokonaislukua. Monellako tavalla voit halkaista taulukon vasempaan ja oikeaan osaan niin, että kummankin osan lukujen summat ovat yhtä suuret?

Esimerkiksi taulukossa [1,2,-1,4,0] mahdolliset halkaisutavat ovat:

[1] ja [2,-1,4,0]
[1,2] ja [-1,4,0]
[1,2,-1] ja [4,0]
[1,2,-1,4] ja [0]
Tässä taulukossa oikea vastaus on 1, koska vasemman ja oikean osan summat ovat samat vain silloin, kun osat ovat [1,2] ja [-1,4,0]. Tällöin kummankin osan summa on 3.

Tee luokka Halkaisu, jossa on seuraavat metodit:

int laske(int[] t): palauttaa tapojen määrän
Rajat:

1 ≤ n ≤ 106
jokainen alkio on välillä –100...100
Seuraava koodi esittelee luokan käyttämistä:

Halkaisu h = new Halkaisu();
[1,2,-1,4,0] // 1
[1,2,3,4,5] // 0
[0,0,0,0,0] // 4
'''

import math
import time


print('\n')

debug = 0

tests = [\
    [1,2,-1,4,0],\
    [1,2,3,4,5],\
    [0,0,0,0,0]]
if debug: tests = tests[0]
functions = []


# v1
def splitsToSameSumCount(l):
    c = 0 # count
    for i in range(1,len(l)):
        if sum(l[:i]) == sum(l[i:]): c += 1
    return c
functions.append(splitsToSameSumCount)


# tests
print('\n')
for f in functions:
    print('\nfunction:'+f.__name__+'\n')
    for test in tests:
        startTime = time.time()
        print('input:', test)
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))