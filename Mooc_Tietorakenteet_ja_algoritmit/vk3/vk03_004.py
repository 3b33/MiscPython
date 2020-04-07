'''
Toteuta O(n log n)-aikainen järjestämisalgoritmi (lomitusjärjestäminen tai pikajärjestäminen) ja vertaa sen tehokkuutta Javan Arrays.sort-metodiin sopivalla testiaineistolla.

Löydät ohjeen tehokkuusvertailun toteuttamiseen tästä. Tässä tehtävässä sinun kannattaa järjestämisen jälkeen tarkastaa, että taulukko todella on järjestyksessä, jolloin pystyt varmistamaan myös, että olet toteuttanut algoritmin toimivasti.
'''

import math
import time
import random
#import sys
random.seed(1)

print('\n')

debug = 0

tests = [\
    [random.randint(1,10**6) for x in range(10**4)],\
    [random.randint(1,10**6) for x in range(10**6)]]
if debug: tests = tests[:1]
functions = []


# school book quick sort version
'''
procedure jarjesta(a, b)
    if a >= b
        return
    k = jako(a,b)
    jarjesta(a,k-1)
    jarjesta(k+1,b)
'''
def quickSortSB(l):
    if l[0] >= l[-1]: return
    k = jako(a,b)
    Org(a,k-1)
    Org(k+1,b)

'''
function jako(a,b):
    k = a
    for i = a+1 to b
        if taulu[i] < taulu[a]
            k += 1
            swap(taulu[i],taulu[k])
    swap(taulu[a],taulu[k])
    return k
'''


# modified quick sort
#sys.setrecursionlimit(10**2)
def quickSort(l):
    if len(l) > 2:
        ''' # first try in modifying quick sort - banned
        if len(l) > 1000: sampleCount = 5 # would be 1 in basic quick sort
        elif len(l) > 10: sampleCount = 3
        sampleCount = 1
        samples = []
        for s in range(sampleCount):
            samples.append(l[s])
        sample = samples[0]
        if len(samples) > 1:
            sortedSamples = quickSort(samples)
            sampleIndex = math.floor(len(samples)/2)
            sample = l[sampleIndex]
            l.pop(sampleIndex)
        else: l.pop(0)
        '''
        if debug: print('samples', samples)
        left = []
        right = []
        ''' # second try in mod - was even slower :(
        if len(l) > 6:
            samples = [l[0],l[1],l[-1]]
            if samples[1] == max(samples): sampleIndex = 1
            elif samples[2] == max(samples): sampleIndex = -1
            else: sampleIndex = 0
        else: sampleIndex = 0
        sample = l[sampleIndex]
        if sampleIndex == -1: sampleIndex = len(l)-1
        '''
        sampleIndex = 0
        sample = l[0]
        for n in l[1:]:
            if n <= sample: left.append(n)
            else: right.append(n)
        if debug: print(left, sample, right)
        if len(left) > 1: left = quickSort(left)
        if len(right) > 1: right = quickSort(right)
        return left+[sample]+right
    elif len(l) == 2:
        if l[0] < l[1]: return l
        else: return [l[1],l[0]]
    else: return l
functions.append(quickSort)


# just for fun, bruteforce
def twoSort(l):
    switched = True
    while switched == True:
        switched = False
        for i in range(1,len(l)):
            if l[i] < l[i-1]:
                l[i], l[i-1] = l[i-1], l[i]
                switched = True
        if debug: print(l[:5])
    return l
#functions.append(twoSort)

# python sorted()
def pythonSorted(l):
    return sorted(l)
functions.append(pythonSorted)


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
        if len(test) <= 10: print('input:', test)
        else:
            print('input list length: '+ toPow(len(test)))
            print('first two values:',test[:2])
        startTime = time.time()
        sl = f(test)
        print('%ss' % round(time.time()-startTime,4))
        print('first values from sorted list:\n',sl[:3])
        print('last values from sorted list:\n',sl[-3:])
        print('\n')


'''
results

function: quickSort

input list length: 10**4
first two values: [140892, 596854]
0.0318s
first values from sorted list:
 [233, 353, 518]
last values from sorted list:
 [999702, 999703, 999720]


input list length: 10**6
first two values: [821686, 788396]
5.1027s
first values from sorted list:
 [2, 3, 3]
last values from sorted list:
 [999999, 999999, 1000000]


function: pythonSorted

input list length: 10**4
first two values: [140892, 596854]
0.0028s

first values from sorted list:
 [233, 353, 518]
last values from sorted list:
 [999702, 999703, 999720]

input list length: 10**6
first two values: [821686, 788396]
0.6034s

first values from sorted list:
 [2, 3, 3]
last values from sorted list:
 [999999, 999999, 1000000


function: twoSort (for fun)

input list length: 10**4
first two values: [297963, 616123]
16.9286s

first values from sorted list:
 [233, 353, 518]
last values from sorted list:
 [999702, 999703, 999720]

'''