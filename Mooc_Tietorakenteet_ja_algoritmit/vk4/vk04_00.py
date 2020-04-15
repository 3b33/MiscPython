'''

'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = []
tests.append([0])
tests.append([0])
tests.append([0])
#tests.append([random.randint(1,9) for x in range(10**2)])
#if debug: tests = tests[:1]
functions = []


# method 1
def temp(l):
    if debug: print(f'')
    return l

functions.append(temp)


# tests
def toPow(n):
    c = 0
    while n >= 10:
        n /= 10
        c += 1
    return (f'10**{str(c)}')

if debug: print('\nresults with debug')
else: print('\nresults')
for f in functions:
    print(f'\nfunction: {f.__name__}\n')
    for test in tests:
        if len(test) < 10: print(f'input:{test}')
        else:
            print(f'\ninput list length: {toPow(len(test))}')
            print(f'first two values:{test[:2]}')
        startTime = time.time()
        print(f(test))
        print(f'{round(time.time()-startTime,4)}\n')
        if debug or test[0] < 10: print(f'resulting list:{sl}')
        else:
            print(f'first values from resulting list:\n{sl[:5]}')
            print(f'last values from resultng list:\n{sl[-5:]}')


'''d


'''