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
test.append([1,2,2,3])
test.append([1,2,3,4])
test.append([1,2,2,3,3,1])
#test.append([random.randint(1,9) for x in range(10**2)])
if debug: tests = tests[:1]
functions = []


# method 1
def delDups(l):
    popped = True
    while popped:
        popped = False
        for i in range(1,len(l)):
            if l[i-1] == l[i]:
                l.pop(0)
                popped = True
    return l

functions.append(temp)


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
        if len(test) < 10: print('input:', test)
        else:
            print('\ninput list length: '+ toPow(len(test)))
            print('first two values:',test[:2])
        startTime = time.time()
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))
        if debug or test[0] < 10: print('resulting list:', sl)
        else:
            print('first values from resulting list:\n',sl[:5])
            print('last values from resultng list:\n',sl[-5:])

'''


'''