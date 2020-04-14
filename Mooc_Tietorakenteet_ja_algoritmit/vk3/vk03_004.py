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
    [random.randint(1,9) for x in range(7)],\
    [random.randint(1,10**6) for x in range(10**4)],\
    [random.randint(1,10**6) for x in range(10**5)]]
random.shuffle(tests[0])
if debug: tests = tests[:1]
functions = []

# merge sort v2, even though mergeSort2.py works. Just wondered if this could be done a bit different.
def mergeSort2(inList):
    l = [[x] for x in inList]
    if len(l) % 2 == 1:
        if l[-1] > l[-2]:
            l[-2] = l[-2]+l[-1]
        else:
            l[-2] = l[-1]+l[-2]
        l.pop(-1)
    if debug: print('start')
    while len(l) > 1:
        if debug: print(l[:10])
        for i in range(0,len(l)-1,2):
            a = l[i]
            b = l[i+1]
            if debug: print(f'a: {a}, b: {b}')
            # merge
            ml = [] # merged list
            while a != []:
                if b != []:
                    if a[0] > b[0]:
                        ml.append(b[0])
                        b.pop(0)
                    else:
                        ml.append(a[0])
                        a.pop(0)
                else:
                    for rest in a: ml.append(rest)
                    break
            if b != []:
                for rest in b: ml.append(rest)
            l[i] = ml
        l = l[::2]
    return l[0]
functions.append(mergeSort2)




# merge sort, lomitusjarjestaminen, v1 too slow
def splits(l):
    i = math.floor(len(l)/2)
    if len(l) > 2: return [splits(l[:i]), splits(l[i:])]
    elif len(l) == 2:
        if l[0] <= l[1]: return [l[0], l[1]]
        else: return [l[1], l[0]]
    else: return [l[0]]

def combineSort(l1,l2):
    l = []
    #if type(l1) is not list: l1 = [l1]
    #if type(l2) is not list: l2 = [l2]
    # these next two lines even needed? (no big speed difference on a 10**4 table)
    if l1[-1] <= l2[0]: return l1+l2
    if l2[-1] <= l1[0]: return l2+l1
    while l1 != [] and l2 != []:
        if l1[0] < l2[0]:
            l.append(l1[0])
            l1.pop(0)
        elif l1[0] > l2[0]:
            l.append(l2[0])
            l2.pop(0)
        else:
            l.append(l1[0])
            l.append(l2[0])
            l1.pop(0)
            l2.pop(0)
    if l1 != []: l += l1
    if l2 != []: l += l2
    return l

def deepCombine(l):
    h1 = l[0]
    h2 = l[1]
    while type(h1[0]) is list: h1 = deepCombine(h1)
    while type(h2[0]) is list: h2 = deepCombine(h2)
    cs =  combineSort(h1, h2)
    if debug: print('csort:',cs)
    return cs

def mergeSort(l):
    spl = splits(l)
    if debug: print ('splits: %s' % spl)
    return deepCombine(spl)
# functions.append(mergeSort)


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


# quick sort
#sys.setrecursionlimit(10**6)
def quickSort(l):
    if len(l) > 2:
        #if debug: print('samples', samples)
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

mergeSort2.py on a 10**5 list: 0.7s


function: quickSort

input list length: 10**4
first two values: [140892, 596854]
0.0318s
first values from sorted list:
 [233, 353, 518]
last values from sorted list:
 [999702, 999703, 999720]

input list length: 10**5
first two values: [768486, 323726]
0.3716s
first values from sorted list:
 [5, 10, 20]
last values from sorted list:
 [999983, 999987, 999994]

input list length: 10**6
first two values: [821686, 788396]
5.1027s # MEH, mergeSort.py takes 8.6s so I'll consider this good enough.
first values from sorted list:
 [2, 3, 3]
last values from sorted list:
 [999999, 999999, 1000000]


function: mergeSort

input list length: 10**4
first two values: [495186, 683245]
0.125s
first values from sorted list:
 [233, 353, 518]
last values from sorted list:
 [999702, 999703, 999720]

input list length: 10**5
first two values: [768486, 323726]
3.1536s
first values from sorted list:
 [5, 10, 20]
last values from sorted list:
 [999983, 999987, 999994]

function: mergeSort2

input: [3, 8, 2, 8, 8, 5, 2]
0.0s
first values from sorted list:
 [2, 2, 3]
last values from sorted list:
 [8, 8, 8]


input list length: 10**4
first two values: [683245, 398056]
0.1308s
first values from sorted list:
 [233, 353, 518]
last values from sorted list:
 [999702, 999703, 999720]


input list length: 10**5
first two values: [323726, 277356]
3.0801s
first values from sorted list:
 [5, 10, 20]
last values from sorted list:
 [999983, 999987, 999994]


function: pythonSorted

input list length: 10**4
first two values: [140892, 596854]
0.0028s
first values from sorted list:
 [233, 353, 518]
last values from sorted list:
 [999702, 999703, 999720]

input list length: 10**5
first two values: [323726, 277356]
0.0491s
first values from sorted list:
 [5, 10, 20]
last values from sorted list:
 [999983, 999987, 999994]

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