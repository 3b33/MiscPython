'''

'''

import math
import time
import random
random.seed(1)

print('\n')

debug = 0

tests = [\
    0,\
    0,\
    0]#,\
    #[random.randint(1,106) for x in range(10**2)]]
if debug: tests = [tests[0]]
functions = []


# v1



# tests
print('\nresults')
for f in functions:
    print('\nfunction: '+f.__name__+'\n')
    for test in tests:
        startTime = time.time()
        print('input:', test)
        print(f(test))
        print('%ss\n' % round(time.time()-startTime,4))