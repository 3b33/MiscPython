'''
Toteuta O(n)-aikainen laskemisjärjestäminen ja vertaa sen tehokkuutta Javan Arrays.sort-metodiin sopivalla testiaineistolla.

Tässä tehtävässä sinun kannattaa järjestämisen jälkeen tarkastaa, että taulukko todella on järjestyksessä, jolloin pystyt varmistamaan myös, että olet toteuttanut algoritmin toimivasti.

Miksei tässä ole annettu n vaatimuksia? Sovitaan vaikka, että
1 <= n <= 1000
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

maxN = 10**3

tests = [\
    [random.randint(1,9) for x in range(6)],\
    [random.randint(1,maxN) for x in range(10**4)],\
    [random.randint(1,maxN) for x in range(10**6)]]
random.shuffle(tests[0])
if debug: tests = tests[:1]
functions = []


# method 1
def countSort(l):
    p = [0 for x in range(maxN+1)]
    for n in l: p[n] += 1
    rl = []
    for i in range(len(p)):
        for d in range(p[i]): rl.append(i)
    return rl

functions.append(countSort)


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
        sl = f(test)
        print('%ss' % round(time.time()-startTime,4))
        print('first values from sorted list:\n',sl[:3])
        print('last values from sorted list:\n',sl[-3:])
        print(sl == sorted(test),'\n')


'''
results

function: countSort

input: [2, 5, 3, 8, 2, 8]
0.0004s

first values from sorted list:
 [2, 2, 3]
last values from sorted list:
 [5, 8, 8]
True

input list length: 10**4
first two values: [484, 668]
0.0029s
first values from sorted list:
 [1, 1, 1]
last values from sorted list:
 [1000, 1000, 1000]
True

input list length: 10**6
first two values: [44, 144]
0.1834s
first values from sorted list:
 [1, 1, 1]
last values from sorted list:
 [1000, 1000, 1000]
True

'''