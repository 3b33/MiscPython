'''
Merkkijonon osajono (substring) on merkkijonon osana oleva toinen merkkijono. Esimerkiksi merkkijonon aybabtu osajonoja ovat bab ja abtu.

Tee luokka Osajonot, jossa on seuraavat metodit:

int laske(String a, String b): palauttaa, montako kertaa merkkijono b esiintyy osajonona merkkijonossa a
Rajat:

kummassakin merkkijonossa on 1...100 merkkiä
kaikki merkit ovat välillä a...z
Seuraava koodi esittelee luokan käyttämistä:

Osajonot o = new Osajonot();
System.out.println(o.laske("aybabtu","bab")); // 1
System.out.println(o.laske("aaaaa","aa")); // 4
System.out.println(o.laske("apina","banaani")); // 0
'''

# print('aaaaa'.count('aa')) # = 2, does not return overlapping results

import math
import time
import random
from random import choice
from string import ascii_lowercase


random.seed(1)
searchTarget = ''.join([choice(ascii_lowercase) for i in range(100)])
searchString = ''.join([choice(searchTarget) for i in range(1)])


print('\n')

debug = 0

tests = [\
    ["aybabtu","bab"],\
    ["aaaaa","aa"],\
    ["apina","banaani"],\
    [searchTarget,searchString]]
if debug: tests = tests[:1]
functions = []

# method 1
def partialLoc(a,b):
    c = 0 # count
    lb = len(b)
    for x in range(0,len(a)-1):
        if a[x:x+lb] == b: c += 1
    return c
functions.append(partialLoc)


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
        print('input:', test)
        startTime = time.time()
        print(f(test[0],test[1]))
        print('%ss\n' % round(time.time()-startTime,4))

'''
results

function: partialLoc

input: ['aybabtu', 'bab']
1
0.0s

input: ['aaaaa', 'aa']
4
0.0s

input: ['apina', 'banaani']
0
0.0s

input: ['eszycidpyopumzgdpamntyyawoixzhsdkaaauramvgnxaqhyoprhlhvhyojanrudfuxjdxkxwqnqvgjjspqmsbphxzmnvflrwyvx', 'y']
7
0.0001s
'''
