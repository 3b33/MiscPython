'''
Tehtäväsi on laskea, monellako tavalla luvun x voi esittää kolmen eri positiivisen kokonaisluvun summana. Esimerkiksi jos x = 9, oikea vastaus on 3, koska mahdolliset tavat ovat 1+2+6, 1+3+5 ja 2+3+4.

Tee luokka KolmenSumma, jossa on seuraavat metodit:

int laske(int x): palauttaa luvun x esitystapojen määrän
Rajat:

1 ≤ x ≤ 100
Seuraava koodi esittelee luokan käyttämistä:

KolmenSumma k = new KolmenSumma();
System.out.println(k.laske(9)); // 3
System.out.println(k.laske(2)); // 0
System.out.println(k.laske(99)); // 768
'''
import math

print('\n')

debug = 0
debug2 = 1

tests = [9,2,99]
if debug: tests = [9]

def SumOfThreeAmt(n):
    cnt = 0 # count (result)
    aMax = (n-3)/3 # a + (a+1) + (a+2) can't be > n. Derived from 3a+3 = n.
    aMax = math.floor(aMax)
    for a in range(1,aMax+1):
        bMax = math.floor((n-a)/2) # b only goes up to c-1
        if (n-a) % 2 == 0: bMax -= 1 # if c is even number, bMax must be lowered
        for b in range(a+1,bMax+1):
            if debug: print(a,b, n-a-b, '  ', aMax, bMax)
            cnt += 1
    return cnt

results = []
for test in tests: results.append(SumOfThreeAmt(test))
print(results) # 3, 0, 768
print('\n')