'''
Annettuna on taulukko, jossa on kokonaislukuja. Joka askeleella muodostat taulukosta uuden taulukon, jonka jokainen alkio on summa kahdesta vierekkäisestä alkiosta alkuperäisessä taulukossa. Jatkat näin, kunnes taulukossa on vain yksi alkio.

Esimerkiksi jos taulukko on [1,2,3,2], se muuttuu ensin taulukoksi [3,5,5], sitten taulukoksi [8,10] ja lopuksi taulukoksi [18].

Tee luokka Taulukko, jossa on seuraavat metodit:

int laske(int[] t): palauttaa lopullisen taulukon ainoan alkion
Rajat:

taulukossa on enintään 20 alkiota
jokainen alkio on välillä 1...100
Seuraava koodi esittelee luokan käyttämistä:

Taulukko t = new Taulukko();
System.out.println(t.laske(new int[] {1,2,3,2})); // 18
System.out.println(t.laske(new int[] {5})); // 5
System.out.println(t.laske(new int[] {4,2,9,1,9,2,5})); // 323
'''

import math

print('\n')
functions = []

debug = 0

tests = [[1,2,3,2],[5],[4,2,9,1,9,2,5]]
if debug: tests = [tests[0]]


# standard custom function
def twoSum(l):
    while len(l) > 1:
        if debug: print(l)
        for i in range(len(l)-1):
            l[i] += l[i+1]
        l.pop(-1)
    return l[0]
functions.append(charSum)


# googled zip method
'''
def twoSumZ(n):
    new = [int(x) for x in str(n)]
    while len(new) > 1:
        z = zip(new[:-1],new[1:])
        new = sum(z)
    return new[0]
functions.append(charSumZ)
'''

results = []
for test in tests: results.append(twoSum(test))
print(results) # 3, 0, 768
print('\n')