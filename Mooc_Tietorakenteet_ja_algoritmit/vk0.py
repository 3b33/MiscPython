'''

'''

import math
import time


print('\n')

debug = 0

tests = []
if debug: tests = tests[0]
functions = []


# functions here


print('\n')
for f in functions:
    results = []
    print('\n'+f.__name__)
    for test in tests:
        startTime = time.time()
        results.append(f(test))
        print('%ss\n' % round(time.time()-startTime,4))
    print(results) #