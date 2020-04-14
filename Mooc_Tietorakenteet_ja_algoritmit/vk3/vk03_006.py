'''
Tehtäväsi on muodostaa n-kokoinen taulukko, joka sisältää luvut 1...n ja siinä on tasan k inversiota. Voit muodostaa minkä tahansa taulukon, joka täyttää nämä vaatimukset.

Tee luokka Inversiot, jossa on seuraavat metodit:

int[] muodosta(int n, long k): palauttaa taulukon
Rajat:

1 ≤ n ≤ 10**6
k on valittu niin, että ratkaisu on olemassa
Seuraava koodi esittelee luokan käyttämistä:

Inversiot i = new Inversiot();
int[] t = i.muodosta(5,2);
System.out.println(Arrays.toString(t)); // [2, 1, 3, 5, 4]
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 1

tests = []
testNum = 5
for n in range(1,(testNum*(testNum-1))//2):
    tests.append([testNum,n])
tests.append([10**4, 10**3])
tests.append([10**6, 10**6+10**3])
if debug: tests = tests[:-2]
functions = []

# method 1
def trianglePos(n,k=1): # or moveShiftCount
    t = n*(n-1)//2 # (max) triangle number
    if k == t: return [n-1,0]
    elif k == 0: return [0,0]
    else:
        lvl = 0 # pyramid level from top
        lvlMax = n-1
        lvlMin = 0
        if debug: print(f'in tp k: {k}, t: {t}, levelMax: {lvlMax}')
        while k < t-lvlMax:
            lvl += 1
            lvlMax -= lvl
            lvlMin -= (lvl-1)
        #lvl = n-lvl+1 # pyramid level from bottom, start at 1. Y Pos.
        x = k-lvlMin # X Pos
    return [lvl, x]


def listWithInversions(n,k=1):
    if k > n*(n-1)/2:
        print(f'Inversion count {k} is too big for list size {n}')
        k = n*(n-1)/2
        print(f'Using inversion count {k}')
    tp = trianglePos(n,k)
    if debug: print(f'triangle position y,x: {tp}')
    m = tp[0]-1 # move this many digits inverted to the right side
    if m < 0: m = 0
    s = tp[1] # shift the last (or only) one this many digits
    sd = m+1 # digit to shift
    l = [x+1 for x in range(sd,n)] # list of the "stationary" digits, or the ones shifted to the left side
    move = [x+1 for x in range(m)][::-1] # list of digits inverted and fully shifted to the right side
    if debug: print(f'{move} + {[sd]} + {l}')
    l = l[:s] + [sd] + l[s:]
    if m > 1: l += move[1:]
    return l

functions.append(listWithInversions)


def countInversions(l):
    inversions = 0
    for i1 in range(len(l[:-1])):
        for i2 in range(i1+1,len(l)):
            if l[i1] > l[i2]: inversions += 1
    return inversions


# tests
def toPow(n):
    c = 0
    while n >= 10:
        n /= 10
        c += 1
    return str('10**'+str(c))

if debug: print('\nresults with debug')
else: print('\nresults')
for f in functions:
    print('\nfunction: '+f.__name__+'\n')
    for test in tests:
        if len(test) < 10: print('\ninput:', test)
        else:
            print('\ninput list length: '+ toPow(len(test)))
            print('first two values:',test[:2])
        startTime = time.time()
        sl = f(test[0],test[1])
        print('%ss' % round(time.time()-startTime,4))
        if debug or test[0] < 10: print('resulting list:', sl)
        else:
            print('first values from resulting list:\n',sl[:5])
            print('last values from resultng list:\n',sl[-5:])
        print('inversion count check:', countInversions(sl),'\n')

'''
results

function: listWithInversions

input: [5, 2]
0.0s
resulting list: [1, 2, 0, 3, 4]

input: [5, 7]
0.0s
resulting list: [2, 3, 4, 1, 0]

input: [5, 9]
0.0s
resulting list: [3, 4, 2, 1, 0]

input: [5, 10]
0.0s
resulting list: [5, 4, 3, 2, 1]

input: [1000000, 1000]
0.0968s
first values from resulting list:
 [1, 2, 0, 3, 4]
last values from resultng list:
 [999995, 999996, 999997, 999998, 999999]

input: [1000000, 1001000]
0.1088s
first values from resulting list:
 [2, 3, 4, 1, 5]
last values from resultng list:
 [999996, 999997, 999998, 999999, 0]
'''