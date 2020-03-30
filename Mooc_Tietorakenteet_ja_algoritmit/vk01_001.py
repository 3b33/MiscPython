'''
https://tira-s19.mooc.fi/viikko-01

Seuraava koodi esittelee luokan käyttämistä:

Numerot n = new Numerot();
System.out.println(n.summa(4075)); // 16
System.out.println(n.summa(3)); // 3
System.out.println(n.summa(999999999)); // 81
'''

# standard function method
'''
def charSum(n):
    sn = 0
    for c in str(n): sn += int(c)
    return sn
'''

# harder to read one liner
def charSum(n): return sum([int(x) for x in str(n)])

print(charSum(4075), charSum(3), charSum(999999999)) # 16, 3, 81

# lambda version
lambdaTest = (lambda x: sum([int(c) for c in str(x)]))(999999999)

print(lambdaTest) # 81