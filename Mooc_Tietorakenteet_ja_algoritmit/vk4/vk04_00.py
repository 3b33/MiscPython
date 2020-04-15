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
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
    for test in tests:
        if len(test) < 10: print(f'\ninput:{test}')
        else:
            print(f'\ninput list length: {powLen(test)}')
            print(f'first values:{test[:5]}')
            print(f'last values:{test[-5:]}')
        toTest = test.copy()
        startTime = time.time()
        sl = f(toTest)
        print(f'{round(time.time()-startTime,4)}s')
        if debug or len(sl) < 10: print(f'resulting list:{sl}')
        else:
            print(f'first values:{sl[:5]}')
            print(f'last values:{sl[-5:]}')
        #print(f'length: {powLen(sl)}')
print('\n')

'''


'''