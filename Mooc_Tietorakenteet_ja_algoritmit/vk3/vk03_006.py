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
tests.append([5,2])
tests.append([5,7])
tests.append([5,10])
#tests.append([random.randint(1,9) for x in range(10**4), 10**3])
if debug: tests = tests[:3]
functions = []


# method 1
def listWithInversions(n,k=1):
    if k > (n**2-n)/2:
        Exception('Inversion count %s is too big for list size %s' % (k,n))
        quit()
    n2 = n-1
    k2 = k
    sc = 0 # first of ordered numbers.
    if k > 0: sc = 1
    while k2-n2 > 0:
        if debug: print('k2:', k2,'n2:',n2, 'sc:', sc)
        sc += 1
        k2 -= n2
        if n2 > 0: n2 -= 1
    k2 = math.ceil(k2)
    if debug: print('k2:', k2,'n2:',n2, 'sc:', sc)
    l = [x for x in range(sc,n)]
    if k > 0:
        if debug: print('l:', l)
        move = [x for x in range(sc)]
        if debug: print('move:', move)
        l = l[:k2] + move[-1:] + l[k2:]
        #l += move[:-1]
        if sc > 1: l += move[::-1][-1:]
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
        if len(test) < 10: print('input:', test)
        else:
            print('input list length: '+ toPow(len(test)))
            print('first two values:',test[:2])
        startTime = time.time()
        sl = f(test[0],test[1])
        print('%ss' % round(time.time()-startTime,4))
        if debug: print('resulting list:', sl)
        else:
            print('first values from resulting list:\n',sl[:5])
            print('last values from resultng list:\n',sl[-5:])
        print('inversion count check:', countInversions(sl),'\n')

'''


results with debug

function: listWithInversions

input: [5, 2]
l: [1, 2, 3, 4]
move: [0]
0.0s

resulting list: [1, 2, 0, 3, 4]
inversion count check: 2
'''