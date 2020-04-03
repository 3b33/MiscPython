'''
1
Kokonaisluku on onnenluku, jos sen jokainen numero on 3 tai 7. Esimerkiksi luvut 7, 37 ja 73373 ovat onnenlukuja. Tehtäväsi on laskea onnenlukujen määrä välillä a...b.

Tee luokka Onnenluvut, jossa on seuraavat metodit:

int laske(int a, int b): palauttaa onnenlukujen määrän välillä a...b
Rajat:

1 ≤ a ≤ b ≤ 10**9
Seuraava koodi esittelee luokan käyttämistä:

Onnenluvut o = new Onnenluvut();
System.out.println(o.laske(1,10)); // 2
System.out.println(o.laske(123,321)); // 0
System.out.println(o.laske(1,1000000)); // 126
Huomaa, että tehtävän aikaraja on yksi sekunti, joten olisi liian hidasta käydä läpi kaikki välin a...b luvut, vaan sinun tulee keksiä tehokkaampi ratkaisutapa.
'''


import math
import time
import random
random.seed(1)


print('\n')

debug = 0

tests = [[1,10],[123,321],[1,1000000],[1,10**9]]
if debug: tests = tests[:-1]
functions = []


# for fun, slow simple version
def luckyNumbersSlow(a,b):
    c = 0 # count
    for n in range(a,b+1):
        for s in str(n):
            if s not in ['3','7']:
                isLucky = False
                break
            isLucky = True
        if isLucky: c += 1
    return c
#functions.append(luckyNumbersSlow)


# itertools version. 'combinations_with_replacement' did not consider repeating values, switched to 'product' instead.
# https://docs.python.org/2/library/itertools.html
import itertools

def luckyNumbersI(a,b):
    luckies = []
    for i in range(len(str(a)),len(str(b))+1):
        combs = itertools.product('37', repeat=i)
        combs = [int(''.join(list(x))) for x in combs]
        luckies += combs
    if debug: print(luckies)
    try:
        while luckies[0] < a:
            luckies.pop(0)
        while luckies[-1] > b:
            luckies.pop(-1)
    except: pass
    return len(luckies)
functions.append(luckyNumbersI)

print('\n')
for f in functions:
    print('\nfunction: '+f.__name__+'\n')
    for test in tests:
        startTime = time.time()
        print('input:', test[0], test[1])
        print(f(test[0],test[1]))
        print('%ss\n' % round(time.time()-startTime,4))

'''
results

function: luckyNumbersI

input: 1 10
2
0.0001s

input: 123 321
0
0.0001s

input: 1 1000000
126
0.0005s

input: 1 1000000000
1022
0.0018s
'''