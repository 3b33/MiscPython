'''
Annettuna on taulukko, jossa on n kokonaislukua. Joka vuorolla poistat taulukosta kaksi vierekkäistä alkiota, jotka ovat samat, kunnes et voi enää poistaa mitään. Jos poiston voi tehdä monella tavalla, poistat alkiot mahdollisimman vasemmalta. Montako alkiota on lopullisessa taulukossa?

Esimerkiksi jos taulukko on [1,2,2,3,3,1], siitä tulee ensin [1,3,3,1], sitten [1,1] ja lopuksi [], eli tässä tapauksessa taulukossa ei ole yhtään alkiota lopuksi.

Tee luokka Poistot, jossa on seuraavat metodit:

int laske(int[] t): palauttaa lopullisen taulukon alkioiden määrän
Rajat:

1 ≤ n ≤ 10**6
jokainen alkio on välillä 1...10**9
Seuraava koodi esittelee luokan käyttämistä:

Poistot p = new Poistot();
System.out.println(p.laske(new int[] {1,2,2,3})); // 2
System.out.println(p.laske(new int[] {1,2,3,4})); // 4
System.out.println(p.laske(new int[] {1,2,2,3,3,1})); // 0
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 1

tests = []
tests.append([1,2,2,3])
tests.append([1,2,3,4])
tests.append([1,2,2,3,3,1])
tests.append([1])
for i in range(10**4-1):
    tests[-1].append(tests[-1][-1]+random.randint(-2,4))
    if tests[-1][-1] < 1: tests[-1][-1] = 1
tests.append([1])
for i in range(10**6-1):
    tests[-1].append(tests[-1][-1]+random.randint(-2,4))
    if tests[-1][-1] < 1: tests[-1][-1] = 1

if debug: tests = tests[:-2]
functions = []



# method 3
'''
- instead of popping, combine lists?
- ie. l = [1,2,2,3,3,4] -> l[:0] + l[5:] after the first sweep
'''
def delDupsPlus(l):
    si = 1
    ssi = -1
    for i in range(si,len(l)):
        if not skip:
            if l[i-1] == l[i]:
                if ssi == -1: ssi = i-1 # split start index
                sse = i # split end index, to be confirmed
                skip = True
            elif ssi != -1:
                l = l[:ssi] + l[sse:]
                # WIP
        else:
            if l[i] == l[ssi]: sse = i
            # if not, don't end removal split yet. See example up top.
            skip = False



# method 2, don't start from beginning after popping, but from i-2
def delDups(l):
    if debug: print(l)
    popped = True
    si = 1
    while popped:
        popped = False
        for i in range(si,len(l)):
            if debug: print(f'i: {i}, l: {l}')
            if l[i-1] == l[i]:
                l.pop(i)
                l.pop(i-1)
                popped = True
                si = i-2
                if si < 1: si = 1
                break
    return l
functions.append(delDups)


# method 1, brute, very slow
def delDupsBrute(l):
    if debug: print(l)
    popped = True
    while popped:
        popped = False
        for i in range(1,len(l)):
            if debug: print(f'i: {i}, l: {l}')
            if l[i-1] == l[i]:
                l.pop(i)
                l.pop(i-1)
                popped = True
                break
    return l
functions.append(delDupsBrute)


# tests
def powLen(n):
    if type(n) is list: n = len(n)
    c = 0
    if n > 1000:
        while n >= 10:
            n /= 10
            c += 1
        return (f'10**{str(c)}')
    else: return n

if debug: print('\nresults with debug')
else: print('\nresults')
for f in functions:
    print(f'\nfunction: {f.__name__}')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'\n')
    for test in tests:
        if len(test) < 10: print(f'\ninput:{test}')
        else:
            print(f'\ninput list length: {powLen(test)}')
            print(f'first values:{test[:5]}')
            print(f'last values:{test[-5:]}')
        toTest = test.copy()
        startTime = time.time()
        sl = f(toTest)
        print(f'{round(time.time()-startTime,4)}s')
        if debug or len(test) < 10: print(f'resulting list:{sl}')
        else:
            print(f'first values:{sl[:5]}')
            print(f'last values:{sl[-5:]}')
        print(f'length: {powLen(sl)}')
print('\n')

'''
results

function: delDups
2020-04-15 11:42:28

input:[1, 2, 2, 3]
0.0s
resulting list:[1, 3]
length: 2
input:[1, 2, 3, 4]
0.0s
resulting list:[1, 2, 3, 4]
length: 4
input:[1, 2, 2, 3, 3, 1]
0.0s
resulting list:[]
length: 0

input list length: 10**4
first values:[1, 1, 3, 7, 11]
last values:[10029, 10032, 10034, 10033, 10031]
0.0081s
first values:[3, 7, 11, 15, 11]
last values:[10029, 10032, 10034, 10033, 10031]
length: 10**3

input list length: 10**6
first values:[1, 1, 2, 1, 1]
last values:[999898, 999901, 999901, 999899, 999900]
123.3043s
first values:[1, 5, 6, 9, 12]
last values:[999899, 999897, 999898, 999899, 999900]
length: 10**5

function: delDupsBrute
2020-04-15 11:44:31

input:[1, 2, 2, 3]
0.0059s
resulting list:[1, 3]
length: 2
input:[1, 2, 3, 4]
0.0s
resulting list:[1, 2, 3, 4]
length: 4
input:[1, 2, 2, 3, 3, 1]
0.0s
resulting list:[]
length: 0

input list length: 10**4
first values:[1, 1, 3, 7, 11]
last values:[10029, 10032, 10034, 10033, 10031]
0.885s
first values:[3, 7, 11, 15, 11]
last values:[10029, 10032, 10034, 10033, 10031]
length: 10**3

input list length: 10**6 # way too slow to wait

'''