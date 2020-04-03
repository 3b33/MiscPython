'''
Annettuna on taulukko, jossa on n lukua. Tehtäväsi on laskea, monessako taulukon yhtenäisessä alitaulukossa on enintään kaksi eri lukua.

Esimerkiksi taulukossa [1,2,3] yhtenäiset alitaulukot ovat [1], [2], [3], [1,2], [2,3] ja [1,2,3]. Näistä kaikissa paitsi viimeisessä on enintään kaksi eri lukua, joten oikea vastaus tälle taulukolle on 5.

Tee luokka Alitaulukot, jossa on seuraavat metodit:

long laske(int[] t): palauttaa alitaulukoiden määrän
Rajat:

1 ≤ n ≤ 10**6
jokainen alkio on välillä 1...10**6
Seuraava koodi esittelee luokan käyttämistä:

Alitaulukot a = new Alitaulukot();
[1,2,1,3,2] // 10
[1,1,1,1,1] // 15
[1,2,3,4,5] // 9
'''

# try out the debug mode here.

# 1M list values result in 1.9s, I'm gonna call it good enough.

import math
import time
import random
import itertools
random.seed(1)

print('\n')

debug = 0

tests = [\
    [1,2,1,3,2],\
    [1,1,1,1,1],\
    [1,2,3,4,5],\
    [random.randint(1,106) for x in range(10**6)]]
if debug: tests = tests[:2]
functions = []


# method 2.
# go through list, slice to groups with max 2 unique numbers, then use tri on their lengths. Can I skip temp slice lists?
def tri(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

def twoUniqueSliceCount(l):
    split = [l[0]]
    tsc = 0 # tri sum count
    # split when same values detected
    i = 1
    while i <= len(l):
        if len(set(split)) == 3:
            tsc += tri(len(split)-1)-1
            if debug: print(split,tsc)
            split = [split[-2]]
            i -= 1
        if debug: print(i, split,tsc)
        if i < len(l): split.append(l[i])
        i += 1
    tsc += tri(len(split))-1
    if debug: print('end', split,tsc)
    #print(splits)
    return tsc+1

functions.append(twoUniqueSliceCount)


'''
method 1 BANNED, got a new idea
in a list with n numbers
len(list) + sum of slices from list for 2 to len(list) members where max 2 unique members
'''
'''
def slicesWithMaxTwoUniqueValuesCount(l):
    c = 0 # count
    for si in range(len(l)-1): # slice start index
        for ei in range(si+1, len(l)-(len(l)-si)+2): # slice end index
            slice = l[si:ei]
            if len(slice) == len(set(slice)): c += 1 
    return c

functions.append(slicesWithMaxTwoUniqueValuesCount)
'''

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

function: twoUniqueSliceCount

input: [1, 2, 1, 3, 2]
10
0.0s

input: [1, 1, 1, 1, 1]
15
0.0s

input: [1, 2, 3, 4, 5]
9
0.0s

input list length: 10**6
first two values: [18, 73]
2019172
1.8971s

'''