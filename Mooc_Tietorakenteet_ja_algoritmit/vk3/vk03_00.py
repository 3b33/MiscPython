'''

'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = []
test.append([0])
test.append([0])
test.append([0])
#test.append([random.randint(1,9) for x in range(10**2)])
if debug: tests = tests[:1]
functions = []


# method 1
def temp(l):
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


'''


'''