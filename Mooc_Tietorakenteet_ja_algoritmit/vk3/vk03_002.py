'''
Annettuna on taulukko, jossa on n kokonaislukua, missä n on pariton. Jokainen taulukon luku esiintyy tasan kahdesti, paitsi yksi luku esiintyy vain kerran. Mikä on tämä luku?

Tee luokka VainYksi, jossa on seuraavat metodit:

int etsi(int[] t): palauttaa luvun, joka esiintyy vain kerran
Rajat:

1 ≤ n ≤ 10**6
jokainen alkio on välillä 1...10**9
Seuraava koodi esittelee luokan käyttämistä:

VainYksi v = new VainYksi();
[5,2,5,3,2] // 3
[1] // 1
[1,10,10,100,100] // 1

Lisähaaste: Tässä tehtävässä riittää mainiosti O(n log n)-aikainen järjestämistä käyttävä ratkaisu, mutta jos haluat vaikeamman tehtävän, koeta keksiä parempi ratkaisu, jonka aikavaativuus on O(n) ja tilavaativuus on O(1).
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = [\
    [5,2,5,3,2],\
    [1],\
    [1,10,10,100,100]]

bigTestListSize = 10**6

dupList = [1]
for x in range(int(bigTestListSize/2)):
    dupList.append(dupList[x-1]+random.randint(1,3))
singleDigit = random.randint(1,10**9)
while singleDigit in dupList: dupList.pop(dupList.index(singleDigit))
dupList *= 2
dupList.append(singleDigit)
random.shuffle(dupList)
random.seed(4)
random.shuffle(dupList)

tests.append(dupList)

if debug: tests = [tests[0]]
functions = []

# method 2
def findUnique2(l):
    if len(l) >= 1:
        s = sorted(l)
        if debug: print(s)
        for i in range(1,len(s),2):
            if s[i] != s[i-1]: return s[i-1]
        return s[-1]
functions.append(findUnique2)


# method 1, too slow.
def findUnique(l):
    ex = [] # existing
    for n in l:
        if debug: print(n, ex)
        if n in ex:
            ex.pop(ex.index(n))
        else: ex.append(n)
    return ex[0]
#functions.append(findUnique)


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

function: findUnique2

input: [5, 2, 5, 3, 2]
3
0.0s

input: [1]
1
0.0s

input: [1, 10, 10, 100, 100]
1
0.0s

input list length: 10**6
first two values: [15174, 243162]
965867901
0.644s


function: findUnique

input: [5, 2, 5, 3, 2]
3
0.0s

input: [1]
1
0.0s

input: [1, 10, 10, 100, 100]
1
0.0s

input list length: 10**5
first two values: [30340, 12526]
923644785
26.245s

'''