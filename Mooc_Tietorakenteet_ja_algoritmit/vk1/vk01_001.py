'''
Tehtäväsi on laskea annetun positiivisen kokonaisluvun numeroiden summa. Esimerkiksi luvun 4075 numeroiden summa on 4 + 0 + 7 + 5 = 16.

Tee luokka Numerot, jossa on seuraavat metodit:

int summa(int x): palauttaa luvun x numeroiden summan
Rajat:

1 ≤ x ≤ 109
Seuraava koodi esittelee luokan käyttämistä:

Numerot n = new Numerot();
System.out.println(n.summa(4075)); // 16
System.out.println(n.summa(3)); // 3
System.out.println(n.summa(999999999)); // 81
'''

print('\n')

debug = 0

tests = [4075, 3, 999999999]
if debug: tests = tests[:1]
functions = []


# standard function method
def charSum(n):
    sn = 0
    for c in str(n): sn += int(c)
    return sn
functions.append(charSum)


# harder to read one liner
def charSumOL(n): return sum([int(x) for x in str(n)])
functions.append(charSumOL)


# lambda version (shorter way?)
def charSumL(n): return (lambda x: sum([int(c) for c in str(x)]))(n)
functions.append(charSumL)





for f in functions:
    results = []
    print('\n'+f.__name__)
    for test in tests: results.append(f(test))
    print(results) # 16, 3, 81