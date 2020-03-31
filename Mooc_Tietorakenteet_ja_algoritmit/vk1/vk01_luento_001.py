'''
How many words can be found in both suomi.txt and in englanti.txt?
'''

import math
import time
import os # https://www.tutorialspoint.com/How-to-open-a-file-in-the-same-directory-as-a-Python-script
startTime = time.time()

print('\n')

debug = 0

os.path

wordsFin = open(os.sys.path[0]+'/suomi.txt', 'r').readlines()
wordsEng = open(os.sys.path[0]+'/englanti.txt', 'r').readlines()

# first try, let's confine words by their starting letters
def orgByFirstChar(l):
    r = {} # return dict
    for w in l:
        if !r[w[0]]: r[w[0]] = [w]
        else: r[w[0]].append(w)

wordsFinO = orgByFirstChar(wordsFin)
wordsEngO = orgByFirstChar(wordsEng)

def getSame(a,b,p=0):
    same = []
    for w1 in a:
        for w2 in b:
            if w1 == w2:
                same.append(w1)



# super slow version
'''
c = 0 # count
for wordFin in wordsFin:
    for wordEng in wordsEng:
        if wordFin == wordEng:
            c += 1
            print(wordFin)
print('\n',c,'\n')
'''


results.append(f(test))
print('%ss\n' % round(time.time()-startTime,4))
