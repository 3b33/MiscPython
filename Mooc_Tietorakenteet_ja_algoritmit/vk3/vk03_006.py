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

tests = [\
    [5,2]]#,\
    #[random.randint(1,9) for x in range(10**4), 10**3]]
if debug: tests = tests[:1]
functions = []


# method 1
def listWithInversions(n,k=1):
    if k > n**2:
        Exception('Inversion count %s is too big for list size %s' % (k,n))
        quit()
    p = n
    c = k
    sc = 0 # start of concurrent numbers
    while c/p >= 1:
        sc += 1
        c /= p
        p -= 1
    l = [x+sc for x in range(sc,n)]
    if debug: print('l:', l)
    move = [x for x in range(sc)]
    if debug: print('move:', move)
    l + move[:-1]
    l = l[:c] + move[-1] + l[c:]
    return l

functions.append(listWithInversions)


def countInversions(l):
    inversions = 0
    for n1 in l[:-1]:
        for n2 in l[n+1:]:
            if n2 > n1: inversions += 1
    return inversions
functions.append(countInversions)


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
        il = (f(test[0],test[1]))
        print('%ss\n' % round(time.time()-startTime,4))
        print('inversion count check:', countInversions(il))
        if debug: print('resulting list:', sl)
        else:
            print('first values from resulting list:\n',sl[:5])
            print('last values from resultng list:\n',sl[-5:])

'''


'''