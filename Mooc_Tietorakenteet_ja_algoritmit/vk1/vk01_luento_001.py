'''
How many words can be found in both suomi.txt and in englanti.txt?
'''

import math
import time
import os # https://www.tutorialspoint.com/How-to-open-a-file-in-the-same-directory-as-a-Python-script
#startTime = time.time()

print('\n')

debug = 0

wordsFin = open(os.sys.path[0]+'/suomi.txt', 'r').readlines()
wordsEng = open(os.sys.path[0]+'/englanti.txt', 'r').readlines()

# let's organize words by their starting letters
def orgByNChar(l,nc=1): # nc = amount of starting letters to organize by
    r = {} # return dict
    for w in l:
        if not r.get(w[:nc]): r[w[:nc]] = [w]
        else: r[w[:nc]].append(w)
    return r

def getSame(a,b,p = False):
    same = []
    for aKey in a.keys():
        for w1 in a[aKey]: # a word list
            if b.get(aKey): # 'ä' not present in the english word list
                for w2 in b[aKey]: # b word list
                    if w1 == w2:
                        same.append(w1)
                        if p: print(w1)
    return same

'''
# method 1, organize by starting letter(s)
# an = amount of starting letters to organize by
print('')
tc = 100 # time counter
for an in range(1,20):
    startTime = time.time()
    wordsFinO = orgByNChar(wordsFin,an)
    wordsEngO = orgByNChar(wordsEng,an)
    sameWords = getSame(wordsFinO,wordsEngO)
    print(an, len(sameWords))
    tcn = round(time.time()-startTime,4)
    print('%ss\n' % tcn)
    if tcn > tc: break
    else: tc = tcn
    print('')
'''

# method 2, idea from lecture notes. Combine lists and get duplicates from that.
startTime = time.time()
wordsComb = wordsFin+wordsEng
# sameWords = set([x for x in wordsComb if wordsComb.count(x) > 1]) # too slow
wordsComb = sorted(wordsComb)
sameWords = []
for wi in range(len(wordsComb)-1):
    if wordsComb[wi] == wordsComb[wi+1]:
        sameWords.append(wordsComb[wi])
        wi += 1

print('\nmethod 2, combine lists')
print(len(sameWords))
tcn = round(time.time()-startTime,4)
print('%ss\n' % tcn)


# method 3: using a set (mimicing hashset in java example)
c = 0 # count
wordsEngSet = set(wordsEng)
for wordFin in wordsFin:
    if wordFin in wordsEngSet:
        c += 1
        #print(wordFin)
print('\nmethod 3, set')
print(c)
tcn = round(time.time()-startTime,4)
print('%ss\n' % tcn)

# super slow version. Didn't wait for this to finish.
'''
c = 0 # count
for wordFin in wordsFin:
    for wordEng in wordsEng:
        if wordFin == wordEng:
            c += 1
            print(wordFin)
print('\n',c,'\n')
'''

print('')

'''
results (an, amount of words):

1 788
16.7207s

2 788
2.0408s

3 788
0.3046s

4 788
0.1722s

5 788
0.16s

6 788
0.1875s

method 2, combine lists
788
0.0789s

method 3, set
788
0.1237s
'''