'''

'''

import math

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
    for test in tests: results.append(f(test))
    print(results) # 