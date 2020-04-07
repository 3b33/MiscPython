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

debug = 1

tests = [\
    [x for x in range(5)],\
    [random.randint(1,10**6) for x in range(10**4)],\
    [random.randint(1,10**6) for x in range(10**6)]]
random.shuffle(tests[0])
if debug: tests = tests[:1]
functions = []


# merge sort, lomitusjarjestaminen

def splits(l):
    i = math.floor(len(l)/2)
    if len(l) > 2: return [splits(l[:i]), splits(l[i:])]
    elif len(l) == 2: return [l[0], l[1]]
    else: return [l[0]]

def combineSort(l1,l2):
    l = []
    while l1 != [] and l2 != []:
        if l1[0] < l2[0]:
            l.append(l1[0])
            l1.pop(0)
        elif l1[0] > l2[0]:
            l.append(l2[0])
            l2.pop(0)
        else:
            l.append(l1[0],l2[0])
            l1.pop(0)
            l2.pop(0)
    if l1 != []: l += l1
    if l2 != []: l += l2
    return l

def deepCombine(l):
    if type(l[0]) is list:
        return [deepCombine(l[0]), deepCombine(l[1])]
    elif len(l) == 2: return combineSort([l[0]], [l[1]])
    else: return [l[0]]

def mergeSort(l):
    return deepCombine(splits(l))

functions.append(mergeSort)


# school book quick sort version, banned
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


# quick sort is slow ??
#sys.setrecursionlimit(10**6)
def quickSort(l):
    if len(l) > 2:
        if debug: print('samples', samples)
        left = []
        right = []
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
#functions.append(quickSort)


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

''' # even slower version
def twoSort(l):
    s = [0 for x in range(len(l))] # 0 = check, 1 = skip
    while 0 in s[1:]:
        for i in range(1,len(l)):
            if s[i] == 0:
                if l[i] < l[i-1]:
                    l[i], l[i-1] = l[i-1], l[i]
                    s[i] = s[i-1] = 0
                else: s[i] = 1
            if debug: print('%s\n%s\n' % (l[:6],s[:6]))
            if 0 not in s[1:]: break
    return l
functions.append(twoSort)
'''

# python sorted()
def pythonSorted(l):
    return sorted(l)
#functions.append(pythonSorted)


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