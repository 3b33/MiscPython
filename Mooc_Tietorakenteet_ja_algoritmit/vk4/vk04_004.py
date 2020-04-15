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

debug = 0

tests = []
tests.append([1,2,2,3])
tests.append([1,2,3,4])
tests.append([1,2,2,3,3,1])
#tests.append([random.randint(1,10**9) for x in range(10**4)])
#tests.append([random.randint(1,10**9) for x in range(10**6)])
tests.append([])
r = 1
for i in range(10**4):
    if random.random() > .15:
        r += 1
    tests[-1].append(r)

tests.append([])
r = 1
for i in range(10**6):
    if random.random() > .15:
        r += 1
    tests[-1].append(r)

if debug: tests = tests[:-2]
functions = []


# method 2
def delDups(l):
    if debug: print(l)
    popped = True
    si = 1
    while popped:
        popped = False
        for i in range(si,len(l)):
            if debug: print(f'i: {i}, l: {l}')
            if l[i-1] == l[i]:
                l.pop(i-1)
                popped = True
                si = i-2
                if si < 1: si = 1
                break
    return l
functions.append(delDups)

# method 1, brute
def delDupsBrute(l):
    if debug: print(l)
    popped = True
    while popped:
        popped = False
        for i in range(1,len(l)):
            if debug: print(f'i: {i}, l: {l}')
            if l[i-1] == l[i]:
                l.pop(i-1)
                popped = True
                break
    return l
#functions.append(delDupsBrute)


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
        if len(test) < 10: print(f'input:{test}')
        else:
            print(f'\ninput list length: {powLen(test)}')
            print(f'first values:{test[:5]}')
        startTime = time.time()
        sl = f(test)
        print(f'{round(time.time()-startTime,4)}s')
        if debug or len(test) < 10: print(f'resulting list:{sl}')
        else:
            print(f'first values from resulting list:\n{sl[:5]}')
            print(f'last values from resultng list:\n{sl[-5:]}')
        print(f'length: {powLen(sl)}')
print('\n')

'''
results

function: delDups
2020-04-15 10:57:25

input:[1, 2, 2, 3]
0.0s
resulting list:[1, 2, 3]
length: 3
input:[1, 2, 3, 4]
0.0s
resulting list:[1, 2, 3, 4]
length: 4
input:[1, 2, 2, 3, 3, 1]
0.0s
resulting list:[1, 2, 3, 1]
length: 4

input list length: 10**4
first values:[1, 2, 3, 4, 5]
0.009s
first values from resulting list:
[1, 2, 3, 4, 5]
last values from resultng list:
[8472, 8473, 8474, 8475, 8476]
length: 10**3

input list length: 10**6
first values:[2, 3, 4, 4, 5]
75.7846s
first values from resulting list:
[2, 3, 4, 5, 6]
last values from resultng list:
[849778, 849779, 849780, 849781, 849782]
length: 10**5


function: delDupsBrute

input:[1, 2, 2, 3]
0.0s
resulting list:[1, 2, 3]
length: 3
input:[1, 2, 3, 4]
0.0s
resulting list:[1, 2, 3, 4]
length: 4
input:[1, 2, 2, 3, 3, 1]
0.0s
resulting list:[1, 2, 3, 1]
length: 4


input list length: 10**4
first values:[1, 2, 3, 4, 5]
0.9215s
first values from resulting list:
[1, 2, 3, 4, 5]
last values from resultng list:
[8472, 8473, 8474, 8475, 8476]
length: 10**3


input list length: 10**6
first values:[2, 3, 4, 4, 5]
# could not bother waiting. At least 3 minutes.

'''