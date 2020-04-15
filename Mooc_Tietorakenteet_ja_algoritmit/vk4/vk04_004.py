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
for i in range(10**4)):

    tests[-1].append(r)

if debug: tests = tests[:-2]
functions = []


# method 1, brute
def delDups(l):
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
functions.append(delDups)


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
    print(f'\nfunction: {f.__name__}\n')
    for test in tests:
        if len(test) < 10: print(f'input:{test}')
        else:
            print(f'\n\ninput list length: {powLen(test)}')
            print(f'first two values:{test[:2]}')
        startTime = time.time()
        sl = f(test)
        print(f'{round(time.time()-startTime,4)}s')
        if debug or test[0] < 10: print(f'resulting list:{sl}')
        else:
            print(f'first values from resulting list:\n{sl[:5]}')
            print(f'last values from resultng list:\n{sl[-5:]}')
        print(f'length: {powLen(sl)}')
print('\n')

'''


'''