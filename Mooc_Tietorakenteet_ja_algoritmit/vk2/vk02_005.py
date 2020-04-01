'''
Annettuna on taulukko, jossa on jokainen luku väliltä 1...n tasan kerran. Haluat kerätä luvut pienimmästä suurimpaan tekemällä yhden tai useamman kierroksen taulukossa. Joka kierroksella käyt läpi taulukon vasemmalta oikealle ja poimit mahdollisimman monta seuraavaksi tulevaa lukua. Montako kierrosta teet yhteensä?

Esimerkiksi taulukossa [4,1,3,2,5] kierrosten määrä on kolme, koska poimit ensimmäisellä kierroksella luvut 1 ja 2, toisella kierroksella luvun 3 ja kolmannella kierroksella luvut 4 ja 5.

Tee luokka Kierrokset, jossa on seuraavat metodit:

int laske(int[] t): palauttaa kierrosten määrän
Rajat:

1 ≤ n ≤ 106
Seuraava koodi esittelee luokan käyttämistä:

[4,1,3,2,5] // 3
[1,2,3,4,5] // 1
[5,4,3,2,1] // 5
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = [\
    [4,1,3,2,5],\
    [1,2,3,4,5],\
    [5,4,3,2,1]]

randomList = [x for x in range(1,10**4+1)]
random.shuffle(randomList)
tests.append(randomList)

if debug: tests = [tests[0]]
functions = []


# v1
def loopSortCountSlow(l):
    #s = [] # sorted list
    g = [x+1 for x in range(len(l))] # goal list
    c = 0 # count of loops
    while g != []:
        for n in l:
            if n == g[0]:
                if debug: print(c+1,n,g)
                g.pop(0)
                if g == []: break
        c += 1
    return c
functions.append(loopSortCountSlow)

# tests
print('\nresults')
for f in functions:
    print('\nfunction: '+f.__name__+'\n')
    for test in tests:
        startTime = time.time()
        if len(test) < 10: print('input:', test)
        else:
            print('input list length:', len(test))
            print('first five values:',test[:5])
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))

'''
results

function: sortLoopCountSlow

input: [4, 1, 3, 2, 5]
3
0.0001s

input: [1, 2, 3, 4, 5]
1
0.0s

input: [5, 4, 3, 2, 1]
5
0.0s

input list length: 10000
first five values: [8710, 8574, 3062, 7880, 5677]
5011
2.663s
'''