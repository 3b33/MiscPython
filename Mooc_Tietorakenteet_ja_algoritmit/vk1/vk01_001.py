'''
Tehtäväsi on laskea annetun positiivisen kokonaisluvun numeroiden summa. Esimerkiksi luvun 4075 numeroiden summa on 4 + 0 + 7 + 5 = 16.

Tee luokka Numerot, jossa on seuraavat metodit:

int summa(int x): palauttaa luvun x numeroiden summan
Rajat:

1 ≤ x ≤ 10**9
Seuraava koodi esittelee luokan käyttämistä:

Numerot n = new Numerot();
System.out.println(n.summa(4075)); // 16
System.out.println(n.summa(3)); // 3
System.out.println(n.summa(999999999)); // 81, huolehtii 10**9 vaatimuksesta
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = [4075, 3, 999999999]
if debug: tests = [tests[0]]
functions = []

print('\n')




# standard function method
def charSum(n):
    sn = 0
    for c in str(n): sn += int(c)
    return sn
functions.append(charSum)


# harder to read one liner
def charSumOL(n): return sum([int(x) for x in str(n)])
functions.append(charSumOL)


# lambda version (shorter way?)
def charSumL(n): return (lambda x: sum([int(c) for c in str(x)]))(n)
functions.append(charSumL)


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
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))

'''
results

function: charSum

input: 4075
16
0.0s

input: 3
3
0.0s

input: 999999999
81
0.0s

input: 244272510
27
0.0s


function: charSumOL

input: 4075
16
0.0s

input: 3
3
0.0s

input: 999999999
81
0.0s

input: 244272510
27
0.0s


function: charSumL

input: 4075
16
0.0s

input: 3
3
0.0s

input: 999999999
81
0.0s

input: 244272510
27
0.0s
'''