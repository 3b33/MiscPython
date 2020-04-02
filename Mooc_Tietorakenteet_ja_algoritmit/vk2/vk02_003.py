'''
Annettuna on taulukko, jossa on n kokonaislukua. Haluat muuttaa taulukkoa niin, että missään kohdassa ei ole kahta samaa lukua peräkkäin. Saat joka siirrolla muuttaa minkä tahansa taulukossa olevan luvun joksikin muuksi. Mikä on pienin määrä siirtoja?

Esimerkiksi taulukossa [1,1,2,2,2] pienin mahdollinen siirtojen määrä on kaksi. Yksi ratkaisu on muuttaa taulukon sisällöksi [1,3,2,1,2].

Tee luokka Muutokset, jossa on seuraavat metodit:

int laske(int[] t): palauttaa pienimmän siirtojen määrän
Rajat:

1 ≤ n ≤ 10**6
jokainen alkio on välillä 1...10**6
Seuraava koodi esittelee luokan käyttämistä:

[1,1,2,2,2] // 2
[1,2,3,4,5] // 0
[1,1,1,1,1] // 2
'''

import math
import time
import random


print('\n')

debug = 0

tests = [\
    [1,1,2,2,2],\
    [1,2,3,4,5],\
    [1,1,1,1,1],\
    [random.randint(1,10**6) for x in range(10**6)],\
    [random.randint(1,10) for x in range(10**6)]]
if debug: tests = tests[0]
functions = []

def sameLenCount(l): # returns list of repeat counts
    o = -1 # old num
    maxCList = [] # max count list
    c = 1 # count of this succession
    for n in l:
        if n == o: c += 1
        else:
            if o != -1: maxCList.append(c)
            c = 1
        o = n
    if l[-1] == l[-2]: maxCList.append(c)
    return maxCList

'''
v1. This was made with no actual replacements taking place. Logic:
n length repeats can be replaced in
3: 111 -> 121 -> 1
4: 1111 -> 1212 -> 2
5: 11111 -> 12121 -> 2
6: 111111 -> 121212 -> 3 moves.
so let's say floor(n/2)
The assignment should've stated if numbers > 9 will suffice. If yes, this should work.
'''
def addToRemoveRepCount(l):
    slc = sameLenCount(l)
    return sum([math.floor(x/2) for x in slc])
functions.append(addToRemoveRepCount)

# tests
print('\nresults')
for f in functions:
    print('\nfunction: '+f.__name__+'\n')
    for test in tests:
        startTime = time.time()
        if len(test) < 10: print('input:', test)
        else:
            print('input list length:', len(test))
            print('first two values:',test[:2])
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))

'''
results

function: addToRemoveRepCount

input: [1, 1, 2, 2, 2]
2
0.0001s

input: [1, 2, 3, 4, 5]
0
0.0s

input: [1, 1, 1, 1, 1]
2
0.0s

input list length: 1000000
first two values: [977121, 285534]
2
0.2789s

input list length: 1000000
first two values: [6, 7]
90710
0.2571s
'''