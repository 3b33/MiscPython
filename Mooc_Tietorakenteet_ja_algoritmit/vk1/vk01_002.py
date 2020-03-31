'''
Merkkijonon osajono (substring) on merkkijonon osana oleva toinen merkkijono. Esimerkiksi merkkijonon aybabtu osajonoja ovat bab ja abtu.

Tee luokka Osajonot, jossa on seuraavat metodit:

int laske(String a, String b): palauttaa, montako kertaa merkkijono b esiintyy osajonona merkkijonossa a
Rajat:

kummassakin merkkijonossa on 1...100 merkkiä
kaikki merkit ovat välillä a...z
Seuraava koodi esittelee luokan käyttämistä:

Osajonot o = new Osajonot();
System.out.println(o.laske("aybabtu","bab")); // 1
System.out.println(o.laske("aaaaa","aa")); // 4
System.out.println(o.laske("apina","banaani")); // 0
'''

# print('aaaaa'.count('aa')) # = 2, does not return overlapping results

def partialLoc(a,b):
    c = 0 # count
    lb = len(b)
    for x in range(0,len(a)-1):
        if a[x:x+lb] == b: c += 1
    return c

print("\n")
print(partialLoc("aybabtu","bab"))
print(partialLoc("aaaaa","aa"))
print(partialLoc("apina","banaani"))
