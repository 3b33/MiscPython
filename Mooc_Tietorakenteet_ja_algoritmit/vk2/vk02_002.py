'''
Annettuna on taulukko, jossa on n kokonaislukua. Tehtäväsi on laskea, kuinka pitkä on pisin samaa lukua toistava osuus taulukossa.

Tee luokka PisinToisto, jossa on seuraavat metodit:

int laske(int[] t): palauttaa pisimmän toiston pituuden
Rajat:

1 ≤ n ≤ 106
jokainen alkio on välillä 1...106
Seuraava koodi esittelee luokan käyttämistä:

PisinToisto p = new PisinToisto();
System.out.println(p.laske(new int[] {1,2,1,1,2})); // 2
System.out.println(p.laske(new int[] {1,2,3,4,5})); // 1
System.out.println(p.laske(new int[] {1,1,1,1,1})); // 5
'''

import math
import time


print('\n')

debug = 0

tests = [[1,2,1,1,2],[1,2,3,4,5],[1,1,1,1,1]]
if debug: tests = tests[0]
functions = []


# v1
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
print('\n')
for f in functions:
    print('\nfunction:'+f.__name__+'\n')
    for test in tests:
        startTime = time.time()
        print('input:', test)
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))