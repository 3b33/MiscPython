'''
Tien varrella on n taloa, joista jokaisella on tietty sijainti (kohta x-akselilla). Tehtäväsi on rakentaa tielle bussipysäkkejä niin, että jokaisen talon etäisyys lähimpään pysäkkiin on enintään k. Mikä on pienin mahdollinen määrä pysäkkejä?

Tee luokka Pysakit, jossa on seuraavat metodit:

int laske(int[] t, int k): palauttaa pienimmän pysäkkien määrän
Rajat:

1 ≤ n ≤ 10**6
jokainen talon sijainti on välillä 1...10**9
1 ≤ k ≤ 10**9
Seuraava koodi esittelee luokan käyttämistä:

Pysakit p = new Pysakit();
[[3,7,1,5], 1] // 2
[[3,7,1,5], 2] // 2
[[3,7,1,5], 3] // 1
'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = [\
    [[3,7,1,5], 1],\
    [[3,7,1,5], 2],\
    [[3,7,1,5], 3],\
    [[random.randint(1,10**9) for x in range(10**6)],10]]
if debug: tests = test[:2]
functions = []



# method 1
def stopCount(l,k):
    s = sorted(l)
    if debug: print(s)
    fi = 0 # first house or stop index in current loop
    stops = [s[0]+k] # locations of stops
    for i in range(1,len(s)):
        if debug: print(i,stops)
        if s[i]-stops[-1] > k:
            stops.append(s[i]+k)
    return len(stops)
functions.append(stopCount)


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
        if len(test[0]) < 10: print('input:', test)
        else:
            print('input list length: '+ toPow(len(test[0])))
            print('k:', test[1])
            print('first two values:',test[0][:2])
        startTime = time.time()
        print(f(test[0],test[1]))
        print('%ss\n' % round(time.time()-startTime,4))


'''
results

function: stopCount

input: [[3, 7, 1, 5], 1]
[1, 3, 5, 7]
1 [2]
2 [2]
3 [2, 6]
[2, 6]
2
0.0001s

input: [[3, 7, 1, 5], 2]
[1, 3, 5, 7]
1 [3]
2 [3]
3 [3]
[3, 9]
2
0.0001s

input: [[3, 7, 1, 5], 3]
[1, 3, 5, 7]
1 [4]
2 [4]
3 [4]
[4]
1
0.0001s

input list length: 10**6
k: 10
first two values: [144272510, 611178003]
980104
1.02s
'''