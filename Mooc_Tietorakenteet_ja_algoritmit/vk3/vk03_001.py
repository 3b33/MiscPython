'''
Annettuna on taulukko, jossa on n kokonaislukua. Tehtäväsi on selvittää, mikä on pienin ero kahden taulukossa olevan luvun välillä.

Tee luokka PieninEro, jossa on seuraavat metodit:

int laske(int[] t): palauttaa pienimmän eron kahden luvun välillä
Rajat:

2 ≤ n ≤ 10**6
jokainen alkio on välillä 1...10**9
Seuraava koodi esittelee luokan käyttämistä:

PieninEro p = new PieninEro();
[4,1,8,5] // 1
[1,10,100] // 9
[1,1,1,1,1] // 0
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = [\
    [4,1,8,5],\
    [1,10,100],\
    [1,1,1,1,1],\
    [random.randint(1,10**9) for x in range(10**6)]]
if debug: tests = [tests[0]]
functions = []


# method 1
def smallestDifference(l):
    s = sorted(l)
    md = abs(s[1]-s[0])
    for i in range(2,len(s)):
        dif = abs(s[i]-s[i-1]) 
        if dif < md: md = dif
    return md

functions.append(smallestDifference)


# tests
def toPow(n):
    c = 0
    while n >= 10:
        n /= 10
        c += 1
    return str('10**'+str(c))

print('\nresults')
for f in functions:
    print('\nfunction: '+f.__name__+'\n')
    for test in tests:
        if len(test) < 10: print('input:', test)
        else:
            print('input list length: '+ toPow(len(test)))
            print('first two values:',test[:2])
        startTime = time.time()
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))

'''
results

function: smallestDifference

input: [4, 1, 8, 5]
1
0.0s

input: [1, 10, 100]
9
0.0s

input: [1, 1, 1, 1, 1]
0
0.0s

input list length: 10**6
first two values: [144272510, 611178003]
0
0.9582s
'''