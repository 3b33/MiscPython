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

1 ≤ n ≤ 10**6
jokainen alkio on välillä –100...100
Seuraava koodi esittelee luokan käyttämistä:

Halkaisu h = new Halkaisu();
[1,2,-1,4,0] // 1
[1,2,3,4,5] // 0
[0,0,0,0,0] // 4
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = [\
    [1,2,-1,4,0],\
    [1,2,3,4,5],\
    [0,0,0,0,0],\
    [random.randint(-100,100) for x in range(10**6)]]
if debug: tests = tests[0]
functions = []


# method 2, should be O(n)
def splitsToSameSumCount2(l):
    sum1 = l[0]
    sum2 = sum(l[1:])
    c = 0 # count
    for i in range(1,len(l)):
        if sum1 == sum2: c += 1
        sum1 += l[i]
        sum2 -= l[i]
    return c
functions.append(splitsToSameSumCount2)


# method 1, too slow
def splitsToSameSumCount(l):
    c = 0 # count
    for i in range(1,len(l)):
        if sum(l[:i]) == sum(l[i:]): c += 1
    return c
# functions.append(splitsToSameSumCount)


# tests
print('\nresults')
for f in functions:
    print('\nfunction: '+f.__name__+'\n')
    for test in tests:
        if len(test) < 10: print('input:', test)
        else:
            print('input list length:', len(test))
            print('first two values:',test[:2])
        startTime = time.time()
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))

'''
results

function: splitsToSameSumCount2

input: [1, 2, -1, 4, 0]
1
0.0s

input: [1, 2, 3, 4, 5]
0
0.0s

input: [0, 0, 0, 0, 0]
4
0.0s

input list length: 10**6
first two values: [-66, 45]
25
0.21s


function: splitsToSameSumCount

input: [1, 2, -1, 4, 0]
1
0.0s

input: [1, 2, 3, 4, 5]
0
0.0s

input: [0, 0, 0, 0, 0]
4
0.0s

input list length: 10000
first two values: [4, 65]
0
0.9964s
'''