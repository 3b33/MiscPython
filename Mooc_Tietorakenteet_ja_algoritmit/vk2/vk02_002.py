'''
Annettuna on taulukko, jossa on n kokonaislukua. Tehtäväsi on laskea, kuinka pitkä on pisin samaa lukua toistava osuus taulukossa.

Tee luokka PisinToisto, jossa on seuraavat metodit:

int laske(int[] t): palauttaa pisimmän toiston pituuden
Rajat:

1 ≤ n ≤ 10**6
jokainen alkio on välillä 1...10**6
Seuraava koodi esittelee luokan käyttämistä:

PisinToisto p = new PisinToisto();
System.out.println(p.laske(new int[] {1,2,1,1,2})); // 2
System.out.println(p.laske(new int[] {1,2,3,4,5})); // 1
System.out.println(p.laske(new int[] {1,1,1,1,1})); // 5
'''

import math
import time
import random

print('\n')

debug = 0

tests = [[1,2,1,1,2],\
    [1,2,3,4,5],\
    [1,1,1,1,1],\
    [random.randint(1,10**6) for x in range(10**6)],\
    [random.randint(1,10) for x in range(10**6)]]
if debug: tests = tests[0]
functions = []


# v1, O(n) I guess
def sameLen(l):
    maxC = o = -1 # max count, old num
    c = 1 # count of this succession
    for n in l:
        if n == o: c += 1
        else: c = 1
        if c > maxC: maxC = c
        o = n
    return maxC
functions.append(sameLen)


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

function: sameLen

input: [1, 2, 1, 1, 2]
2
0.0s

input: [1, 2, 3, 4, 5]
1
0.0s

input: [1, 1, 1, 1, 1]
5
0.0s

input list length: 1000000
first two values: [995515, 182779]
2
0.0779s

input list length: 1000000
first two values: [1, 6]
6
0.0826s
'''